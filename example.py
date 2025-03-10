import random

def fill_list():
    full_list = []
    for _ in range(10):
        full_list.append(random.randint(1, 100))
    return full_list
