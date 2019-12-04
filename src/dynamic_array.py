"""A dynamically sized array"""
import random


class DynamicArray:
    def __init__(self, capacity=8):
        self.count = 0
        self.capacity = capacity
        self.storage = [None] * self.capacity

    def __repr__(self):
        return f"DynamicArray: ({repr(self.storage)})"

    def __len__(self):
        return self.capacity

    def insert(self, index, value):
        if self.count >= self.capacity:
            self._expand()
        # Shift everything at index to right.
        if index > self.count:
            print('ERROR: Out of Range.')
            return
        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i - 1]
        self.storage[index] = value
        self.count += 1

    def _expand(self):
        self.storage += [None] * self.capacity
        self.capacity *= 2

    def delete(self, index):
        if index >= self.count:
            print('ERROR: Out of Range')
            return
        for i in range(index, self.capacity - 1):
            self.storage[i] = self.storage[i + 1]
        self.storage[-1] = None
        self.count -= 1

    def append(self, value):
        return self.insert(self.count, value)

    def prepend(self, value):
        return self.insert(0, value)


if __name__ == '__main__':
    my_array = DynamicArray()
    # my_array.insert(0, 2)
    # my_array.append(9)
    # my_array.insert(0, 4)
    # my_array.insert(2, 6)
    # my_array.insert(3, 4)
    for x in [random.randint(0, 10) for _ in range(32)]:
        my_array.insert(random.randint(0, my_array.count), x)
    print(my_array)
    my_array.delete(0)
    print(my_array)
    print(len(my_array))
