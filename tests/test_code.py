import unittest
from demo_code import RandomNumberGenerator


def test_random_number_generator():
    """Test random number generator."""
    if not RandomNumberGenerator().get_number():
        raise AssertionError


class Tests(unittest.TestCase):
    pass
