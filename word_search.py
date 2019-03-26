from collections import namedtuple

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
