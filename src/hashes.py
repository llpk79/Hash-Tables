"""Hash function for hashtable."""

key = 'Hello World!'


def djb2(key):
    _key = bytes(key, encoding='UTF-8')
    hash_value = 5381

    for char in _key:
        hash_value = ((hash_value << 5) + (hash_value >> 2)) + char ^ hash_value
    return hash_value


if __name__ == '__main__':
    print(djb2(key))
