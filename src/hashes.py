import time
import hashlib
import bcrypt

key = b'Hello World!'

sha = hashlib.sha3_256(key).hexdigest()
print(sha)
xha = '0x' + sha
print(xha)
print(int(xha, 16))


def djb2(key):
    hash_value = 5381

    for char in key:
        hash_value = ((hash_value << 5) + hash_value) + char
    return hash_value


print(djb2(key))
print(f'{int(sha, 16)}')
