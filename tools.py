import random
import string


def get_random_text(length=10):
    t = list()
    for _ in range(length):
        t.append(random.choice(string.ascii_letters + string.digits))
    random.shuffle(t)
    return ''.join(t)


def get_random_id(length=10):
    t = list()
    for _ in range(length):
        t.append(random.choice(string.digits))
    random.shuffle(t)
    return int(''.join(t))
