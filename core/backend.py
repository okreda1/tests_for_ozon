from core.api.placeholder_api import Placeholder
from requests import Session
from core.utils.config import config


class Backend:

    def __init__(self):
        self.config = config
        self.base_url = self.config['dev']['JSONPLACEHOLDER_HOST']
        self.session = Session()
        self.placeholder = Placeholder(self.session, self.base_url)
