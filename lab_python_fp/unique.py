# Итератор для удаления дубликатов
from collections import Counter


class Unique(object):
    def __init__(self, items, **kwargs):
        self.ignore_case = True
        if len(kwargs) != 0:
            self.ignore_case = kwargs['ignore_case']
        if not self.ignore_case:
            self.elements = list(sorted(set([x.casefold() for x in items])))
        else:
            self.elements = list(sorted(set(items)))
        self.elements_it = iter(self.elements)

    def __next__(self):
        return next(self.elements_it)

    def __iter__(self):
        return self
