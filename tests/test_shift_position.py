from shift_position import shift_list_position

import pytest


@pytest.mark.parametrize("number_list, shift_positions, expected", [
    ([1, 2, 3, 4, 5, 6, 7], 2, [3, 4, 5, 6, 7, 1, 2]),  # Basic test
    ([1, 2, 3, 4, 5, 6, 7], 8, [2, 3, 4, 5, 6, 7, 1]),  # Shift more than the length of the array
    ([1, 2, 3, 4, 5, 6, 7], 0, [1, 2, 3, 4, 5, 6, 7]),  # Shift by 0 positions
    ([1, 2, 3, 4, 5, 6, 7], 7, [1, 2, 3, 4, 5, 6, 7]),  # Shift by array length (no change)
    ([1, 2, 3, 4, 5], 3, [4, 5, 1, 2, 3]),  # Smaller array, normal case
    ([10], 1, [10]),  # Single element array (no rotation)
    ([], 3, []),  # Empty array
])
def test_shift_array_positions(number_list, shift_positions, expected):
    assert shift_list_position(number_list, shift_positions) == expected


@pytest.mark.parametrize("positions", [-1, -5, "two", 2.5])  # Invalid inputs
def test_shift_array_invalid_positions(positions):
    assert shift_list_position([1, 2, 3, 4], positions) == []


def test_shift_empty_array():
    assert shift_list_position([], 2) == []
