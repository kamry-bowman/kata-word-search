import unittest
import word_search


PuzzleData = word_search.PuzzleData


class TestParseTest(unittest.TestCase):
    """
    Tests the ability of parse_puzzle to take in puzzle text and return a PuzzleData instance
    """

    def test_parse_empty_file(self):
        data = ''
        self.assertEqual(PuzzleData(words=[], field=[]),
                         word_search.parse_puzzle(data))


if __name__ == '__main__':
    unittest.main()
