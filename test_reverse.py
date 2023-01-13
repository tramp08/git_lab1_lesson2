import unittest
from yandex_testing_lesson import reverse


class TestReverse(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(reverse(''), '')

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            reverse(42)

