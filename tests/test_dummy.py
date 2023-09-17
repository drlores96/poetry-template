import pytest
from pkg_name.dummy import Dummy


@pytest.mark.parametrize("a_input, b_input, expected", [
    (0, 0, 0),
    (0, 1, 1),
    (0, 2, 2),
    (0, 3, 3),
    (1, 0, 1),
    (1, 1, 2),
    (1, 2, 3),
    (1, 3, 4),
    (2, 0, 2),
    (2, 1, 3),
    (2, 2, 4),
    (2, 3, 5),
    (3, 0, 3),
    (3, 1, 4),
    (3, 2, 5),
    (3, 3, 6),
])
def test_multi_dummys(a_input, b_input, expected):
    assert Dummy(a_input, b_input).c is expected
