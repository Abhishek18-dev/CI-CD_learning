from sum import sum
from mul import mul

def test_sum():
    assert sum(2,3) == 5
    assert sum(4,3) == 7
def test_mul():
    assert mul(2,3) == 6