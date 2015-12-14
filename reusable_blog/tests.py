from django.test import TestCase
from .models import Post
# Create your tests here.

class PostTest(TestCase):
    def test_str(self):
        test_title = Post(title="My latest blog post")
        self.assertEqual(
            str(test_title),
            "My latest blog post")