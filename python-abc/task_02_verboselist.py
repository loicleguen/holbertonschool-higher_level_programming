#!/usr/bin/env python3


class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        x = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{x}] items.")

    def remove(self, item):
        super().remove(item)
        print(f"Removed [{item}] from the list.")

    def pop(self, index=-1):
        item = self[index]
        super().pop(index)
        print(f"Popped [{item}] from the list.")
