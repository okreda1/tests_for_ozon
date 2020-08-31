import allure
import pytest
from faker import Faker
from random import randint


@allure.suite('GET /posts')
class TestGetPosts:

    @allure.title('Positive. Get all posts')
    def test_get_all_posts(self, json_client):
        response = json_client.placeholder.get_all_posts()
        assert response is not None
        assert len(response) == 100
        assert response[0].id == 1
        assert response[99].id == 100

    @allure.title('Positive. Get post by id')
    def test_get_post_by_id(self, json_client):
        response = json_client.placeholder.get_all_posts()
        assert response is not None
        postid = randint(1, len(response))
        post_from_all = response[postid - 1]
        post_by_id = json_client.placeholder.get_post_by_id(post_id=postid)
        assert post_by_id.id == postid
        assert post_by_id.title == post_from_all.title
        assert post_by_id.userId == post_from_all.userId

    @allure.title('Negative. Get post by id')
    @pytest.mark.parametrize('postid', [randint(101, 1000)])
    def test_negative_get_post_by_id(self, json_client, postid):
        with pytest.raises(AssertionError) as exception:
            json_client.placeholder.get_post_by_id(post_id=postid)
        assert exception.value.args[0].startswith('Expected status code: 20*. Actual code: 404.')


@allure.suite('POST /posts')
class TestCreatePosts:

    @allure.title('Positive. Create post')
    @pytest.mark.xfail(reason='Post wasn`t actually created')
    def test_create_post(self, json_client):
        userid = randint(1, 10)
        title = Faker().pystr()
        test = json_client.placeholder.create_post(userid=userid, title=title)
        assert test is not None
        assert test.userId == userid
        assert test.title == title
        test2 = json_client.placeholder.get_post_by_id(post_id=test.id)
        assert test.userId == test2.userid
        assert test.title == test2.title
