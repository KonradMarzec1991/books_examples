import re
import reprlib
from collections import abc


RE_WORD = re.compile('\w+')


"""
re.compile seperates definition of the regex from its use

prog = re.compile(pattern)
result = prog.match(string)

is equivalent to

result = re.match(pattern, string)

re.compile is more efficient when expression will be used several times
"""


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)  # finds all non-overlapping matches of pattern in string, as list of strings

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)


s = Sentence('The time has come," the Walrus said,')
print(s)

for word in s:
    print(word)


"""
Implementation is ale sequence, so we can get words by index
"""

for index in range(len(s)):
    print(s[index])


class Foo:
    def __iter__(self):
        pass


print(issubclass(Foo, abc.Iterable))

f = Foo()
print(isinstance(f, abc.Iterable))


"""
To check if object is iterable, call iter(x) - considers the legacy of __getitem__ method, 
while the abc.Iterable does not
"""

"""
Iterable - any object from which the iter built-in function can obtain iterator.
Python obtains iterators from iterables
"""

s = 'ABC'
for char in s:
    print(char)


s = 'ABC'
it = iter(s)

while True:
    try:
        print(next(it))
    except StopIteration:  # signals that the iterator is exhausted
        del it
        break

"""
The standard interface for an iterator has two methods:
    1) __next__
    2) __iter__ - returns self
    
Iterable - __iter__
Iterator - __iter__ / __next__
"""


print(hasattr(s, '__iter__'))
print(hasattr(s, '__next__'))

s3 = Sentence('Pig and Pepper')
it = iter(s3)

print(it)
print(next(it))
print(next(it))
print(next(it))

print(list(s3))
print(list(iter(s3)))


"""
Iterator - any object that implements the __next__ method and __iter__, so iterators are iterable as well
"""

