import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from extract.page_object_model import PageObjectModel

flogging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class LogInPage(PageObjectModel):

    def __init__(self, investment_site_uid):
        PageObjectModel.__init__(self, investment_site_uid)
        self._home = "{}{}".format(
            self._config['url'], self._config['login']['url'])

    def type_user_credential(self):
        input_ = self._browser.find_element_by_xpath(
            self._config['login']['user'])
        input_.send_keys(self._credentials['user'])

    def type_password_credential(self):
        input_ = self._browser.find_element_by_xpath(
            self._config['login']['password'])
        input_.send_keys(self._credentials['password'])

    def click_login(self):
        self._browser.find_element_by_xpath(
            self._config['login']['button']).click()

    def _auth0(self):
        if 'auth0' in self._config['login']:
            WebDriverWait(self._browser, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, self._config['login']['auth0']))
            )
            self._browser.find_element_by_xpath(
                self._config['login']['auth0']).click()

    def navigate(self):
        self._browser.get(self._home)
        self._auth0()
        self.type_user_credential()
        self.type_password_credential()
        self.click_login()
        if 'until' in self._config['login']:
            WebDriverWait(self._browser, 10).until(
                EC.text_to_be_present_in_element(
                    (By.XPATH, self._config['login']['until']),
                    self._credentials['user']
                )
            )

        logging.info("logged in at {} correctly".format(self.site))
