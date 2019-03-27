from collections import namedtuple, defaultdict
import sys

PuzzleData = namedtuple('Puzzle_Data', ['words', 'field'])


def parse_puzzle(data):
    """Expects a file object as its data argument. Returns a PuzzleData named tuple with words
    representing words to be found, an field a 2D list array representing the search field.
    """
    first_line = data.readline()
    words = first_line.strip().split(',') if first_line else []

    field = []
    for line in data:
        field.append(line.strip().split(','))

    return PuzzleData(words=words, field=field)


class Puzzle:
    """Represents a word search puzzle. Takes as arguments a words list and a fields 2D list
    representing the words to be searched, and the letter matrix of the puzzle respectively"""

    def __init__(self, words, field):
        self.words = words
        self.field = field

    def __repr__(self):
        return f'Puzzle(words={self.words}, field={self.field})'

    def solve(self):
        """Returns a dict of each search word, pointing to a list of found word instances.
        Each word instance is a list of tuples representing coordinates in letter matrix."""
        solutions = defaultdict(list)
        for word in self.words:
            solutions[word].extend(self._search(word))
        return solutions

    def pretty_solve(self):
        """Wraps solve, and returns the solution as a string with the following format:
        BONES: (0,6),(0,7),(0,8),(0,9),(0,10)
        KHAN: (5,9),(5,8),(5,7),(5,6)
        KIRK: (4,7),(3,7),(2,7),(1,7)
        SCOTTY: (0,5),(1,5),(2,5),(3,5),(4,5),(5,5)
        SPOCK: (2,1),(3,2),(4,3),(5,4),(6,5)
        SULU: (3,3),(2,2),(1,1),(0,0)
        SULU: (3,4),(3,3),(3,2),(3,1)
        UHURA: (4,0),(3,1),(2,2),(1,3),(0,4)"""
        solutions = self.solve()
        for word in solutions:
            for case in solutions[word]:
                # converts a list of tuples into a string of comma separated str representations
                coords = ','.join(map(lambda pos: repr(pos), case))
                print(f'{word}: {coords}')

    def _search(self, word):
        """Searches self.field for word, searching horizontally left to right,
        horizontally right to left"""
        field = self.field
        solutions = []
        for r in range(len(field)):
            for c in range(len(field[r])):
                if field[r][c] == word[0]:
                   # check horizontal forward
                    solution = []
                    for i in range(len(word)):
                        try:
                            if word[i] == field[r][c + i]:
                                solution.append((c + i, r))
                            else:
                                break
                        except IndexError:
                            break
                    else:
                        solutions.append(solution)

                    # check horizontal reverse
                    solution = []
                    for i in range(len(word)):
                        try:
                            if (c - i) < 0:
                                break
                            if word[i] == field[r][c - i]:
                                solution.append((c - i, r))
                            else:
                                break
                        except IndexError:
                            break
                    else:
                        solutions.append(solution)

                    # check vertical up
                    solution = []
                    for i in range(len(word)):
                        try:
                            if (r - i) < 0:
                                break
                            if word[i] == field[r - i][c]:
                                solution.append((c, r - i))
                            else:
                                break
                        except IndexError:
                            break
                    else:
                        solutions.append(solution)

                    # check vertical down
                    solution = []
                    for i in range(len(word)):
                        try:
                            if word[i] == field[r + i][c]:
                                solution.append((c, r + i))
                            else:
                                break
                        except IndexError:
                            break
                    else:
                        solutions.append(solution)

                    # check diagonal up right
                    solution = []
                    for i in range(len(word)):
                        if (r - i) < 0:
                            break
                        try:
                            if word[i] == field[r - i][c + i]:
                                solution.append((c + i, r - i))
                            else:
                                break
                        except IndexError:
                            break
                    else:
                        solutions.append(solution)

                    # check diagonal up left
                    solution = []
                    for i in range(len(word)):
                        if (r - i) < 0 or (c - i) < 0:
                            break
                        try:
                            if word[i] == field[r - i][c - i]:
                                solution.append((c - i, r - i))
                            else:
                                break
                        except IndexError:
                            break
                    else:
                        solutions.append(solution)

                    # check diagonal down right
                    solution = []
                    for i in range(len(word)):
                        try:
                            if word[i] == field[r + i][c + i]:
                                solution.append((c + i, r + i))
                            else:
                                break
                        except IndexError:
                            break
                    else:
                        solutions.append(solution)

                   # check diagonal down left
                    solution = []
                    for i in range(len(word)):
                        if (c - i) < 0:
                            break
                        try:
                            if word[i] == field[r + i][c - i]:
                                solution.append((c - i, r + i))
                            else:
                                break
                        except IndexError:
                            break
                    else:
                        solutions.append(solution)
        return solutions


def main(argv):
    with open(argv[0]) as file:
        puzzle = Puzzle(*parse_puzzle(file))

    puzzle.pretty_solve()


if __name__ == "__main__":
    main(sys.argv[1:])
