import os

class Host:
    DEV = 'dev'
    PROD = 'prod'

    URLS = {
        DEV: 'https://dev.21yard.com/',
        PROD: 'https://example.ru/'
    }

    def __init__(self):
        try:
            self.env = os.getenv('ENV')
        except KeyError:
            self.env = self.PROD

    def get_base_url(self):
        if self.env in self.URLS:
            return self.URLS[self.env]
        else:
            raise Exception(f"Unknown value of ENV variable {self.env}")


host = Host()
