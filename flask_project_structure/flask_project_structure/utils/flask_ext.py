from flask import Flask

class Mongo:
    def __init__(self, appname = None):
        self.appname = appname
    
    def init_app(self, app: Flask):
        pass

class Redis:
    def __init__(self, appname = None):
        self.appname = appname
    
    def init_app(self, app: Flask):
        pass

class Mysql:
    def __init__(self, appname = None):
        self.appname = appname

    def init_app(self, app: Flask):
        pass