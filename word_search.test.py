import unittest
import word_search


class SmokeTest(unittest.TestCase):

    def test_example(self):
        self.assertEqual(word_search.test(5), '5')


if __name__ == '__main__':
    unittest.main()
