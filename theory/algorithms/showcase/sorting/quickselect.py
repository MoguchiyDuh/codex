from __future__ import annotations
import random


def quickselect(arr: list[int], k: int) -> int:
    """Returns the k-th smallest element in arr (0-indexed)."""
    if not 0 <= k < len(arr):
        raise ValueError("Index k out of bounds")
    return _select(arr, 0, len(arr) - 1, k)


def _select(arr: list[int], left: int, right: int, k: int) -> int:
    if left == right:
        return arr[left]

    pivot_index = random.randint(left, right)
    pivot_index = _partition(arr, left, right, pivot_index)

    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return _select(arr, left, pivot_index - 1, k)
    else:
        return _select(arr, pivot_index + 1, right, k)


def _partition(arr: list[int], left: int, right: int, pivot_index: int) -> int:
    pivot_val = arr[pivot_index]
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
    store_index = left
    for i in range(left, right):
        if arr[i] < pivot_val:
            arr[store_index], arr[i] = arr[i], arr[store_index]
            store_index += 1
    arr[right], arr[store_index] = arr[store_index], arr[right]
    return store_index


if __name__ == "__main__":
    test_arr = [3, 2, 1, 5, 4]
    k = 2  # Find 3rd smallest (value 3)
    print(f"{k}-th smallest element: {quickselect(test_arr, k)}")
