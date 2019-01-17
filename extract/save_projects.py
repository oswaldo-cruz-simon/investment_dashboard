import pymongo

from common import credentials
from common import config


host = config()['mongodb']['host']
user = credentials()['mongodb']['user']
password = credentials()['mongodb']['password']


class SaveProjects(object):

    def __init__(self):
        uri = "mongodb+srv://{}:{}@{}/test?retryWrites=true".format(
            user, password, host)
        client = pymongo.MongoClient(uri)
        self._db = client[config()['mongodb']['db']['name']]

    def save(self, projects):
        self._db.project.insert_many(projects)
