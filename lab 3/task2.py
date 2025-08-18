from typing import Iterable, List


def sort_numbers(nums: Iterable[int]) -> List[int]:
    """Return a new list of the integers in non-decreasing order.

    Examples:
        >>> sort_numbers([3, 1, 2])
        [1, 2, 3]
        >>> sort_numbers([5, -1, 5, 2])
        [-1, 2, 5, 5]
        >>> sort_numbers([])
        []
    """
    return sorted(nums)


if __name__ == "__main__":
    # Example I/O
    example = [3, 1, 2, -4, 2]
    print("Input:", example)
    print("Output:", sort_numbers(example))


