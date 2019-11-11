import re
import reprlib


RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = re.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for word in self.words:
            yield word
        return


"""
Any Python function that has the yield keyword in its body is a generator function
"""


def gen123():
    yield 1
    yield 2
    yield 3


print(gen123)
print(gen123())


for i in gen123():
    print(i)


g = gen123()
print(next(g))
print(next(g))
print(next(g))


def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end.')


for c in gen_AB():
    print('-->', c)


"""
A lazy implementation postpones producing values to the last possible moment.
"""