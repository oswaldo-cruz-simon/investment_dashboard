import collections
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from extract.common import config
from extract.common import browser


def map_nested_dicts(ob, func):
    if isinstance(ob, collections.Mapping):
        return {k: map_nested_dicts(v, func) for k, v in ob.items()}
    else:
        return func(ob)


def extract_number(type_, text):
    regex = {
        "quantity": r'\$(?:\d+,?)+(?:\.\d+)?',
        "percentage": r'(?:\d+)+(?:\.\d+)?%'
    }
    num = re.findall(regex[type_], text)[0]
    num = num.replace('$', '')
    num = num.replace(',', '')
    num = num.replace('%', '')
    return float(num)


class ProjectPage(object):

    def __init__(self, investment_site_uid, home):
        self._config = config()['investment_sites'][investment_site_uid]
        self._browser = browser()
        self._soup = None
        self._home = "{}{}".format(self._config['url'], home)

    def navigate(self):
        self._browser.get(self._home)
        self._browser.implicitly_wait(
            int(config()['driver']['implicitly_wait']))

    @property
    def payload(self):
        return map_nested_dicts(
            self._config['project']['payload'],
            lambda v: self._browser.find_element_by_xpath(v).text
        )


class CumploProjectPage(ProjectPage):

    def __init__(self, home):
        ProjectPage.__init__(self, 'cumplo', home)

    def simulator(self):
        self._browser.find_element_by_xpath(
            self._config['projetc']['simulator']).click()

    def navigate(self):
        self._browser.get(self._home)
        html = self._browser.find_element_by_tag_name('html')
        html.send_keys(Keys.END)
        WebDriverWait(self._browser, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, self._config['project']['simulator']['calculate']))
        )

        WebDriverWait(self._browser, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, self._config['project']['simulator']['calculate']))
        )

        self._browser.find_element_by_xpath(
            self._config['project']['simulator']['calculate']).click()

        WebDriverWait(self._browser, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, self._config['project']['simulator']['show']))
        )
        self._browser.find_element_by_xpath(
            self._config['project']['simulator']['show']).click()
