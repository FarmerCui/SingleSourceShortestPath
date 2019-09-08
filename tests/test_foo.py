import unittest

from shortest_path import Foo


class TestFoo(unittest.TestCase):

    def test_foo_name(self):
        foo = Foo()
        self.assertEqual(foo.name.upper(), 'FOO')
