import pytest
from calculator import add

def test_add_positive_numbers():
  assert add(5, 3) == 8
