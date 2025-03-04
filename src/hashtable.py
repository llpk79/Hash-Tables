"""
Linked List hash table key/value pair
"""
from hashes import djb2


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table with `capacity` buckets that accepts string keys.
    """

    def __init__(self, capacity=8, load_factor=.7):
        self.capacity = capacity  # Number of buckets in the hash table.
        self.storage = [None] * capacity
        self.load_factor = load_factor
        self.max_count = self.capacity * self.load_factor
        self.count = 0  # Number of keys in hash table.

    def _hash(self, key):
        """
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        """
        return djb2(key)

    def _hash_djb2(self, key):
        """
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        """
        pass

    def _hash_mod(self, key):
        """
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        """
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.
        """
        index = self._hash_mod(key)
        if self.storage[index]:
            curr = self.storage[index]
            while True:
                if curr.key == key:
                    curr.value = value
                    return
                if curr.next:
                    curr = curr.next
                else:
                    break
            curr.next = LinkedPair(key, value)
        else:
            self.storage[index] = LinkedPair(key, value)
        self.count += 1
        if self.count >= self.max_count:
            self.resize()

    def remove(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        """
        index = self._hash_mod(key)
        if not self.storage[index]:
            print(f"KeyError: {key} Does not exist.")
            return
        curr = self.storage[index]
        if curr.key == key:
            self.storage[index] = curr.next
            self.count -= 1
            return
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                self.count -= 1
                return
        print(f'KeyError: {key} Does not exist.')

    def retrieve(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        """
        index = self._hash_mod(key)
        curr = self.storage[index]
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        print(f'KeyError: {key} Does not exist.')

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        """
        self.capacity *= 2
        self.max_count = self.capacity * self.load_factor
        new_storage = [None] * self.capacity
        for i in self.storage:
            curr = i
            while curr:
                index = self._hash_mod(curr.key)
                new_storage[index] = LinkedPair(curr.key, curr.value)
                curr = curr.next
        self.storage = new_storage


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
