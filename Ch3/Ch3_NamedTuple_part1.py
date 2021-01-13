from collections import namedtuple

roster1 = (('Joan', ['art', 'PC'], [60, 59]),
           ('Henry', ['math'], [96]),
           ('John', ['english', 'SS'], [80, 87]))

roster2 = (('Joan', ['art', 'PC'], ['spr', 'spr'], [60, 59]),
           ('Henry', ['math'], ['fall'], [96]),
           ('John', ['english', 'SS'], ['fall', 'fall'], [80, 87]))

Roster = namedtuple('Roster', ['student', 'course', 'term', 'grade'])

roster3 = (Roster('Joan', ['art', 'PC'], ['spr', 'spr'], [60, 59]),
           Roster('Henry', ['math'], ['fall'], [96]),
           Roster('John', ['english', 'SS'], ['fall', 'fall'], [80, 87]))
