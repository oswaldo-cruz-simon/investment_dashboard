from common import config
from common import credentials


class PageObjectModel(object):

    def __init__(self, investment_site_uid):
        self.site = investment_site_uid
        self._config = config()['investment_sites'][investment_site_uid]
        self._credentials = credentials()['investment_sites'][
            investment_site_uid]
        self._browser = None
        self._home = "{}".format(self._config['url'])

    @property
    def browser(self):
        return self._browser

    @browser.setter
    def browser(self, browser):
        self._browser = browser
