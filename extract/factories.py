from extract.project_list_page import CumploProjectListPage
from extract.project_list_page import BriqProjectListPage
from extract.project_page import CumploProjectPage
from extract.project_page import BriqProjectPage


class ProjectList(object):

    def factory(self, type_):
        mapper = {
            "briq": BriqProjectListPage(),
            "cumplo": CumploProjectListPage()
        }
        if type_ not in mapper:
            raise ValueError('Invalid argument type {}'.format(type_))
        return mapper[type_]


class Project(object):

    def factory(self, type_):
        mapper = {
            "briq": BriqProjectPage('/'),
            "cumplo": CumploProjectPage('/')
        }
        if type_ not in mapper:
            raise ValueError('Invalid argument type {}'.format(type_))
        return mapper[type_]
