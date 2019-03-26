import unittest
from word_search import PuzzleData, parse_puzzle, Puzzle


class TestParseFile(unittest.TestCase):
    """
    Tests the ability of parse_puzzle to take in puzzle text and return a PuzzleData instance
    """

    def test_parse_empty_file(self):
        with open('test_data/empty_file.txt') as file:
            self.assertEqual(PuzzleData(words=[], field=[]),
                             parse_puzzle(file))

    def test_parse_words_no_field(self):
        with open('test_data/words_no_field.txt') as file:
            self.assertEqual(PuzzleData(words=['BONES', 'JOHNS'], field=[]),
                             parse_puzzle(file))

    def test_parse_minimal_file(self):
        with open('test_data/minimal_file.txt') as file:
            self.assertEqual(PuzzleData(
                words=['HA'], field=[['H', 'A'], ['L', 'A']]),
                parse_puzzle(file))

    def test_make_puzzle(self):
        with open('test_data/minimal_file.txt') as file:
            self.assertEqual(repr(Puzzle(*parse_puzzle(file))),
                             "Puzzle(words=['HA'], field=[['H', 'A'], ['L', 'A']])")


if __name__ == '__main__':
    unittest.main()
