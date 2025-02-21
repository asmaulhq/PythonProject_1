import random
def generate_random_integer(start, end):
    """Generate a random integer between start and end (inclusive)."""
    return random.randint(start, end)

def generate_random_float():
    """Generate a random float between 0 and 1."""
    return random.random()
