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


class TestPuzzleSolving(unittest.TestCase):
    """
    Tests the ability of the puzzle to find proper solutions
    """

    def test_horizontal_solution(self):
        with open('test_data/horizontal_only.txt') as file:
            puzzle = Puzzle(*parse_puzzle(file))
        self.assertEqual(puzzle.solve()['BEST'], [[
                         (0, 1), (1, 1), (2, 1), (3, 1)]])
        self.assertEqual(puzzle.solve()['STEP'], [[
                         (2, 1), (3, 1), (4, 1), (5, 1)]])


if __name__ == '__main__':
    unittest.main()
