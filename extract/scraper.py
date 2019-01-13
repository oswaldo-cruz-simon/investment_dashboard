import json
import sys
import argparse

from log_in_page import LogInPage
from factories import ProjectList
from factories import Project
from kinesis_producer import ScrappingProducer
from common import config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Scraper(object):

    def __init__(self, headless):
        options = Options()
        if headless:
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
        self._browser = webdriver.Chrome(config()['driver']['path'],
                                         chrome_options=options)
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
            print(payload)
            put_response = producer.put_to_stream(
                thing_id, json.dumps(payload))


def parse_arrgs():
    parser = argparse.ArgumentParser(
        description="Scrape a site"
    )

    parser.add_argument("site", help="""
        briq: Scrape briq.mx
        briq: Scrape cumplo.mx
        """, choices=["briq", "cumplo"])
    parser.add_argument("-l", "--headless", help="""
        Run selenium in headless mode
        """, action="store_true")
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_arrgs()
    site = args.site
    headless = args.headless
    print(site, headless)
    scraper = Scraper(headless=headless)
    scraper.scrape(site)
