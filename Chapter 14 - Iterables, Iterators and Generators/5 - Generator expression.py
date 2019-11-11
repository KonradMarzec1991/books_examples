"""
Generator expression can be understood as a lazy version of list comprehension
"""

import re
import reprlib


RE_WORD = re.compile('\w+')


def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end.')


res1 = [x*3 for x in gen_AB()]
for i in res1:
    print(i)


res2 = (x*3 for x in gen_AB())
for i in res2:
    print(i)


class Sentence:

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return (match.group() for match in RE_WORD.finditer(self.text))