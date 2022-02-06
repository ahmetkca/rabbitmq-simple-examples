import random, string

def get_random_message(len: int) -> str:
    return ''.join(
        random.choice(string.ascii_letters + string.digits) for _ in range(len)
    )