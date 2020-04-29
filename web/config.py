from os.path import abspath, dirname, join

_cwd = dirname(abspath(__file__))


class BaseConfiguration(object):
    DEBUG = False
    TESTING = False


class TestConfiguration(BaseConfiguration):
    DEBUG = True
    TESTING = True