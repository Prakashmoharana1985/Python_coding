from collections import namedtuple

Roster = namedtuple('Roster', ['student', 'course', 'term', 'grade'])

roster3 = (Roster('Joan', ['art', 'PC'], ['spr', 'spr'], [60, 59]),
           Roster('Henry', ['math'], ['fall'], [96]),
           Roster('John', ['english', 'SS'], ['fall', 'fall'], [80, 87]))


