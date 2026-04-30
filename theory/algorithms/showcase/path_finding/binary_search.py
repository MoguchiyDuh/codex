from __future__ import annotations


def binary_search(arr: list[int], target: int) -> int:
    """Returns the index of target in sorted arr, or -1 if not found."""
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


if __name__ == "__main__":
    test_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 6
    print(f"Target {target} at index: {binary_search(test_arr, target)}")
