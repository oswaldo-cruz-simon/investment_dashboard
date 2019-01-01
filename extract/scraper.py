import json
from extract.log_in_page import LogInPage
from extract.factories import ProjectList
from extract.factories import Project
from extract.kinesis_producer import ScrappingProducer

from selenium import webdriver
from extract.common import config


class Scraper(object):

    def __init__(self):
        self._browser = webdriver.Chrome(config()['driver']['path'])
        self._browser.implicitly_wait(10)

    def scrape(self, site):

        login_page = LogInPage(site)
        login_page.browser = self._browser
        login_page.navigate()
        project_list_page = ProjectList().factory(site)
        project_list_page.browser = self._browser
        project_list_page.navigate()

        project_page = Project().factory(site)
        project_page.browser = self._browser
        producer = ScrappingProducer('python-stream')
        thing_id = 'aa-bb'

        for url_project in project_list_page.project_urls:
            project_page.home = url_project
            project_page.navigate()
            payload = project_page.payload
            put_response = producer.put_to_stream(
                thing_id, json.dumps(payload))
