#!/usr/bin/env python3

class CountedIterator:
    def __init__(self, iterable, counter=0):
        self.iterator = iter(iterable)
        self.counter = counter

    def get_count(self):
        return self.counter

    def __next__(self):
        item = next(self.iterator)
        self.counter += 1
        return item

    def __iter__(self):
        return self
