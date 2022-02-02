import random
import string

def get_random_message_body(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join((random.choice(letters_and_digits) for _ in range(length)))

def produce_blocking_message(prefix: str):
    return f"Task-{prefix}{'.'*random.randint(1, 10)}"