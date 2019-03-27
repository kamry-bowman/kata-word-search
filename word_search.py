from collections import namedtuple, defaultdict

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
        solutions = defaultdict(list)
        for word in self.words:
            solutions[word].extend(self._search(word))
        return solutions

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
        return solutions
