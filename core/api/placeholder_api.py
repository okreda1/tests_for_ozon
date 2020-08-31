import allure
from core.managers.jsonplaceholder_client import Client
from core.models.posts import Post


class Placeholder(Client):

    @allure.step('Get all posts from placeholder')
    def get_all_posts(self):
        list_posts = []
        response = self._get(url=f'/posts')
        for i in response:
            list_posts.append(Post(**i))
        return list_posts

    @allure.step('Get all posts from placeholder by post id')
    def get_post_by_id(self, post_id: int):
        response = self._get(url=f'/posts/{post_id}')
        return Post(**response)

    @allure.step('Get all posts from placeholder by post id')
    def create_post(self, userid=None, title=None, **kwargs):
        params = {'userId': userid, 'title': title, **kwargs}
        response = self._post(url=f'/posts', json=params)
        return Post(**response)
