import random


def chain(*iterables):
    for it in iterables:
        for i in it:
            yield i


s = 'ABC'
t = tuple(range(3))
print(list(chain(s, t)))


def chain2(*iterables):
    for it in iterables:
        yield from it  # syntactic sugar


s = 'ABC'
t = tuple(range(3))
print(list(chain2(s, t)))


def d6():
    return random.randint(1, 6)


d6_iter = iter(d6, 1)  # 1 is a sentinel value

for roll in d6_iter:
    print(roll)


class Fibonacci:

    def __iter__(self):
        return FibonacciGenerator()


class FibonacciGenerator:

    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result

    def __iter__(self):
        return self


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b