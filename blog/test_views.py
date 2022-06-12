from django.test import TestCase, Client
from django.urls import reverse

""" Testing views """

class TestViews(TestCase):
    """ Testing the response to ensure each view show the right 
        template and response """

    """ Test for PostList """
    def test_get_post_list(self):
        
        client = Client()
        response = client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    """ Test for CreatePost """
    def test_create_post(self):
        
        client = Client()
        response = client.get(reverse('create_post'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_post.html')