import unittest
import word_search


PuzzleData = word_search.PuzzleData


class TestParseTest(unittest.TestCase):
    """
    Tests the ability of parse_puzzle to take in puzzle text and return a PuzzleData instance
    """

    def test_parse_empty_file(self):
        with open('test_data/empty_file.txt') as file:
            self.assertEqual(PuzzleData(words=[], field=[]),
                            word_search.parse_puzzle(file))


if __name__ == '__main__':
    unittest.main()
