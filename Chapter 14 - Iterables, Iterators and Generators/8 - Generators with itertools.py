import itertools
import operator


"""
Filtering generator functions examples
"""


def vowel(c):
    return c.lower() in 'aeiou'


print(list(filter(vowel, 'Aardvark')))

# itertools
# print(list(itertools.filterfalse(vowel, 'Aardvark')))
# print(list(itertools.dropwhile(vowel, 'Aardvark')))
# print(list(itertools.takewhile(vowel, 'Aardvark')))
#
# print(list(itertools.compress('Aardvark', (1, 0, 1, 1, 0, 1))))
#
# print(list(itertools.islice('Aardvark', 4)))
# print(list(itertools.islice('Aardvark', 4, 7)))
# print(list(itertools.islice('Aardvark', 1, 7, 2)))


# sample = [3, 4, 5, 1, 1, 2, 4, 5, 3, 2]
# print(list(itertools.dropwhile(lambda x: x >= 3, sample)))
# print(list(itertools.takewhile(lambda x: x >= 3, sample)))

# Conclusion - list(itertools.dropwhile(p, iterable) + itertools.takewhile((p, iterable)_ = iterable


"""
itertools.accumulate generator function examples
"""


sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]


# print(list(itertools.accumulate(sample)))
#
# print(list(itertools.accumulate(sample, min)))
# print(list(itertools.accumulate(sample, max)))
#
# print(list(itertools.accumulate(sample, operator.mul)))
# print(list(itertools.accumulate(range(1, 11), operator.mul)))  # factorials n!
# print(list(itertools.accumulate(range(1, 11), operator.sub)))

"""
Mapping generator function examples
"""


# print(list(enumerate('albatroz', 1)))
# print(list(enumerate('albatroz', 2)))
#
# print(list(map(operator.mul, range(11), range(11))))
# print(list(map(operator.mul, range(11), [2, 4, 8])))
# print(list(map(lambda a, b: (a, b), range(11), [2, 4, 8])))
#
# print(list(itertools.starmap(operator.mul, enumerate('albatroz', 1))))
# sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]
#
# print(list(itertools.starmap(lambda a, b: b/a,
#                              enumerate(itertools.accumulate(sample), 1))))


"""
Merging generator function examples
"""


# print(list(itertools.chain('ABC', range(2))))
# print(list(itertools.chain(enumerate('ABC'))))
# print(list(itertools.chain.from_iterable(enumerate('ABC'))))
#
# print(list(zip('ABC', range(5))))
# print(list(zip('ABC', range(5), [10, 20, 30, 40])))
# print(list(itertools.zip_longest('ABC', range(5))))
# print(list(itertools.zip_longest('ABC', range(5), fillvalue="?")))


"""
itertools.product generator function examples
"""


print(list(itertools.product('ABC', range(2))))

suits = 'spades hearts diamonds clubs'.split()
print(list(itertools.product('AK', suits)))

print(list(itertools.product('ABC', repeat=2)))
print(list(itertools.product(range(2), repeat=3)))


rows = itertools.product('AB', range(2), repeat=2)
for row in rows:
    print(row)


