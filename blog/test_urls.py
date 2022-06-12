from django.test import TestCase
from django.urls import reverse, resolve
from . import views

# Create your tests here.

# Urls tests

class TestUrls(TestCase):

    """ Test for home url"""
    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func.view_class, views.PostList)

    """ Test for create_post url"""
    def test_create_post_url_resolves(self):
        url = reverse('create_post')
        self.assertEqual(resolve(url).func.view_class, views.CreatePost)

    """ Test for post_detail url"""
    def test_post_detail_url_resolves(self):
        url = reverse('post_detail', args=[1234567890123456789])
        self.assertEqual(resolve(url).func.view_class, views.PostDetail)

    """ Test for post_like url"""
    def test_post_like_url_resolves(self):
        url = reverse('post_like', args=[1234567890123456789])
        self.assertEqual(resolve(url).func.view_class, views.PostLike)

    """ Test for post_dislike url"""
    def test_post_dislike_url_resolves(self):
        url = reverse('post_dislike', args=[1234567890123456789])
        self.assertEqual(resolve(url).func.view_class, views.PostDislike)
