from nose.tools import *
from challenges.when_it_rains_it_pours import answer


def test_one():
	assert answer([1, 4, 2, 5, 1, 2, 3]) == 5

def test_two():
	assert answer([1, 2, 3, 2, 1]) == 0