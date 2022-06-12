from django.test import TestCase
from .forms import PostForm, CommentForm


""" Test for blog form """

class TestPostForm(TestCase):

    """ Tests if post title is required """
    def test_post_title_is_required(self):
        
        form = PostForm(({'title': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    """ tests if post content is required """
    def test_post_content_is_required(self):
        
        form = PostForm(({'content': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['content'][0], 'This field is required.')

    """ tests if fields are explicit in blog form """
    def test_fields_are_explicit_in_form_metaclass(self):

        form = PostForm()
        self.assertEqual(
            form.Meta.fields, ('title', 'category', 'content', 'featured_image')
        )

""" Test for comments form """

class TestCommentForm(TestCase):

    """ Tests if post body is required """
    def test_post_body_is_required(self):
        
        form = CommentForm(({'body': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    """ Tests if fields are explicit in comment form """
    def test_fields_are_explicit_in_form_metaclass(self):
        
        form = CommentForm()
        self.assertEqual(
            form.Meta.fields, ('body',)
        )

