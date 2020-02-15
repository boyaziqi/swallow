"""sample test"""
from unittest import TestCase

from swallow.utils import hello


class TestHello(TestCase):
    """sample test"""

    def test_world(self):
        """sample test"""
        self.assertEqual(hello.hello('world'), 'hello world')

    def test_world_unicode(self):
        """sample test with unicode"""
        self.assertEqual('hello world', 'hello world')
