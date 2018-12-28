import yaml
from selenium import webdriver

__config = None
__credentials = None
__browser = None

def config():
    global __config
    #if not __config:
    with open('config.yaml', mode='r') as f:
        __config = yaml.load(f)
    return __config

def credentials():
    global __credentials
    if not __credentials:
        with open('.credentials.yaml', mode='r') as f:
            __credentials = yaml.load(f)
    return __credentials

def browser():
    global __browser
    if not __browser:
        __browser = webdriver.Chrome(config()['driver']['path'])
    return __browser
