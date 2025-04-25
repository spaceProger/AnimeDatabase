import random


def auth_code() -> int:
    return random.randint(100_000, 1_000_000)
