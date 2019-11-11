import itertools

"""
itertools.count never stops - impossible to create list of it
"""


gen = itertools.count(1, .5)

print(next(gen))
print(next(gen))
print(next(gen))


"""
itertools.takewhile produces generator that consumes another generator 
and stops when a given predicate evaluates to False
"""
gen = itertools.takewhile(lambda n: n < 3, itertools.count(1, .5))
print(list(gen))


def aritprog_gen(begin, step, end=None):
    first = type(begin + step)(step)
    ap_gen = itertools.count(first, step)
    if end is not None:
        ap_gen = itertools.takewhile(lambda n: n < end, ap_gen)
    return ap_gen