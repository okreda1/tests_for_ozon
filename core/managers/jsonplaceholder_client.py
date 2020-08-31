import allure
from requests import Session


class Client:
    def __init__(self, session: Session, host):
        self.session = session
        self.base_url = host

    @staticmethod
    def _response_general_check(response):
        assert str(response.status_code).startswith('20'), \
                    f'Expected status code: 20*. Actual code: {response.status_code}. Url: {response.url}'

    def _get_path(self, url):
        return f'{self.base_url}{url}'

    def _get(self, url, **kwargs):
        callback = self.session.get
        return self._send(url, callback, 'GET', **kwargs)

    def _post(self, url, **kwargs):
        callback = self.session.post
        return self._send(url, callback, 'POST', **kwargs)

    def _send(self, url, callback, method, **kwargs):
        request_msg = f'{method} {self._get_path(url)}'
        allure.attach(request_msg.replace('\n', '\n\n'), 'Request', allure.attachment_type.TEXT)
        body = kwargs.get('data') or kwargs.get('json')
        if body is not None:
            request_msg = f'{request_msg}\nBody: {body}'
        response = callback(self._get_path(url), **kwargs)
        allure.attach(request_msg, 'Request', allure.attachment_type.JSON)
        self._response_general_check(response)
        if response.text != '':
            allure.attach(response.text, 'Response', allure.attachment_type.JSON)
        prepared_response = response.json()
        return prepared_response
