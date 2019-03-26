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
