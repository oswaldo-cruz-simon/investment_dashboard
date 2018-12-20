from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re

from extract.common import config
from extract.common import browser


class ProjectListPage(object):

    def __init__(self, investment_site_uid):
        self._config = config()['investment_sites'][investment_site_uid]
        self._browser = browser()
        self._soup = None

    @property
    def project_urls(self):
        pass

    def navigate(self):
        self._browser.get(self._home)
        if 'wait' in self._config['current_projetcs']:
            WebDriverWait(self._browser, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, self._config['current_projetcs']['wait'])
                )
            )
        self._browser.implicitly_wait(50)
        html = self._browser.find_element_by_tag_name('html')
        html.send_keys(Keys.END)
        self._browser.implicitly_wait(50)
        self._soup = BeautifulSoup(self._browser.page_source, 'html.parser')


class BriqProjectListPage(ProjectListPage):

    def __init__(self):
        ProjectListPage.__init__(self, 'briq')
        self._home = "{}{}".format(self._config['url'], self._config[
                                   'current_projetcs']['url'])

    @property
    def project_urls(self):
        urls = [i.parent['href']
                for i in self._soup.find_all('img', {
                    'src': re.compile(r'label_buscando-inversion')
                })]
        return urls


class CumploProjectListPage(ProjectListPage):

    def __init__(self):
        ProjectListPage.__init__(self, 'cumplo')
        self._home = "{}{}".format(self._config['url'], self._config[
                                   'current_projetcs']['url'])

    @property
    def project_urls(self):
        project_urls = [i.find_parents('div', limit=1)[0].text[
            3:] for i in self._soup.find_all(text='ID')]
        project_urls = ['{}{}'.format('/solicitud/MX/', i)
                        for i in project_urls]

        return project_urls
