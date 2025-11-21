"""tak_1.py

Ride-sharing ETA sorting examples using two AI-suggested algorithms:
- Merge Sort
- Quick Sort

This module provides both sorting implementations, a function to time
and choose the faster algorithm for a given input, and a small CLI demo.

It prints the fastest available driver (lowest ETA) and the fully sorted list.
"""
from __future__ import annotations
from typing import List, Tuple, Callable
import time


def merge_sort(arr: List[float]) -> List[float]:
    """Return a new list containing the sorted values using merge sort.

    Args:
        arr: list of numeric ETA values (float or int)

    Returns:
        A new list sorted in ascending order.
    """
    if len(arr) <= 1:
        return arr[:]

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    merged: List[float] = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append any remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def quick_sort(arr: List[float]) -> List[float]:
    """Return a new list containing the sorted values using quick sort.

    This implementation uses a simple recursive Lomuto-style partitioning
    (choosing the middle element as pivot) and returns a new list rather
    than sorting in-place to keep the API consistent and simple for tests.
    """
    if len(arr) <= 1:
        return arr[:]

    pivot = arr[len(arr) // 2]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    # Recurse and concatenate
    return quick_sort(less) + equal + quick_sort(greater)


def time_function(fn: Callable[[List[float]], List[float]], data: List[float]) -> Tuple[List[float], float]:
    """Run `fn` on a copy of `data`, return (result, elapsed_seconds)."""
    copy = data[:]  # avoid mutating the caller's list
    t0 = time.perf_counter()
    res = fn(copy)
    t1 = time.perf_counter()
    return res, t1 - t0


def choose_and_sort(etalist: List[float]) -> Tuple[List[float], str, float]:
    """Sort the ETA list using both algorithms, measure which is faster.

    Args:
        etalist: list of ETAs (ints/floats)

    Returns:
        A tuple of (sorted_list, fastest_algorithm_name, fastest_time_seconds).

    The sorted_list is the ascending-sorted list of ETAs. fastest_algorithm_name
    is one of 'merge' or 'quick'.
    """
    # Time merge sort
    merge_sorted, merge_time = time_function(merge_sort, etalist)

    # Time quick sort
    quick_sorted, quick_time = time_function(quick_sort, etalist)

    # Validate both returned the same sorted result (they should)
    if merge_sorted != quick_sorted:
        # As a fallback prefer the explicitly sorted Python result
        verified = sorted(etalist)
    else:
        verified = merge_sorted

    # Choose fastest
    if merge_time <= quick_time:
        fastest = "merge"
        fastest_time = merge_time
    else:
        fastest = "quick"
        fastest_time = quick_time

    return verified, fastest, fastest_time


def format_output(sorted_list: List[float]) -> str:
    """Return a human-friendly string describing the fastest driver and the list."""
    if not sorted_list:
        return "No ETA data available."
    fastest_eta = sorted_list[0]
    return f"Fastest available driver ETA: {fastest_eta}\nFull sorted ETAs: {sorted_list}"


if __name__ == "__main__":
    # Example usage: small sample list. Replace or integrate with live ETA feed.
    sample = [12.5, 3.0, 8.2, 3.0, 25.0, 7.9, 0.5]
    sorted_list, fastest_algo, fastest_time = choose_and_sort(sample)
    print(f"Chosen algorithm: {fastest_algo} (t={fastest_time:.6f}s)")
    print(format_output(sorted_list))
