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

    def test_make_rectangle_puzzle(self):
        with open('test_data/rectangle.txt') as file:
            with self.assertRaisesRegex(Exception, 'Only square fields are acceptable.'):
                Puzzle(*parse_puzzle(file))


class TestPuzzleSolving(unittest.TestCase):
    """
    Tests the ability of the puzzle to find proper solutions
    """

    def test_horizontal_forward_solution(self):
        with open('test_data/horizontal_forward.txt') as file:
            puzzle = Puzzle(*parse_puzzle(file))
        self.assertEqual(puzzle.solve()['BEST'], [
            [(0, 1), (1, 1), (2, 1), (3, 1)],
            [(1, 5), (2, 5), (3, 5), (4, 5)]
        ])
        self.assertEqual(puzzle.solve()['STEP'], [[
                         (2, 1), (3, 1), (4, 1), (5, 1)]])

    def test_horizontal_backward_solution(self):
        with open('test_data/horizontal_backward.txt') as file:
            puzzle = Puzzle(*parse_puzzle(file))
        self.assertEqual(puzzle.solve()['BEST'], [
            [(3, 4), (2, 4), (1, 4), (0, 4)]
        ])
        self.assertEqual(puzzle.solve()['STEP'], [[
                         (3, 5), (2, 5), (1, 5), (0, 5)]])

    def test_vertical_up_solution(self):
        with open('test_data/vertical_up.txt') as file:
            puzzle = Puzzle(*parse_puzzle(file))
        self.assertEqual(puzzle.solve()['BEST'], [
            [(1, 5), (1, 4), (1, 3), (1, 2)],
            [(2, 5), (2, 4), (2, 3), (2, 2)]
        ])
        self.assertEqual(puzzle.solve()['STEP'], [[
                         (5, 4), (5, 3), (5, 2), (5, 1)]])

    def test_vertical_down_solution(self):
        with open('test_data/vertical_down.txt') as file:
            puzzle = Puzzle(*parse_puzzle(file))
        self.assertEqual(puzzle.solve()['BEST'], [
            [(1, 2), (1, 3), (1, 4), (1, 5)],
        ])
        self.assertEqual(puzzle.solve()['STEP'], [[
                         (5, 1), (5, 2), (5, 3), (5, 4)]])

    def test_diagonal_up(self):
        with open('test_data/diagonal_up.txt') as file:
            puzzle = Puzzle(*parse_puzzle(file))
        self.assertEqual(puzzle.solve()['DORK'], [
            [(3, 5), (2, 4), (1, 3), (0, 2)],
        ])
        self.assertEqual(puzzle.solve()['DOG'], [
            [(3, 5), (4, 4), (5, 3)]
        ])

    def test_diagonal_down(self):
        with open('test_data/diagonal_down.txt') as file:
            puzzle = Puzzle(*parse_puzzle(file))
        self.assertEqual(puzzle.solve()['DOG'], [
            [(2, 0), (1, 1), (0, 2)],
        ])
        self.assertEqual(puzzle.solve()['DORK'], [
            [(2, 0), (3, 1), (4, 2), (5, 3)]
        ])

    def test_combined(self):
        with open('test_data/combined.txt') as file:
            puzzle = Puzzle(*parse_puzzle(file))
        solution = puzzle.solve()
        self.assertEqual(solution['BONES'], [[
                         (0, 6), (0, 7), (0, 8), (0, 9), (0, 10)]])
        self.assertEqual(solution['KHAN'], [[(5, 9), (5, 8), (5, 7), (5, 6)]])
        self.assertEqual(solution['KIRK'], [[(4, 7), (3, 7), (2, 7), (1, 7)]])
        self.assertEqual(solution['SCOTTY'], [
                         [(0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5)]])
        self.assertEqual(solution['SPOCK'], [
                         [(2, 1), (3, 2), (4, 3), (5, 4), (6, 5)]])
        self.assertEqual(solution['SULU'], [[(3, 3), (2, 2), (1, 1), (0, 0)]])
        self.assertEqual(solution['UHURA'], [
                         [(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)]])


if __name__ == '__main__':
    unittest.main()
