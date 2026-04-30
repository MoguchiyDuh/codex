from __future__ import annotations


def insertion_sort(arr: list[int]) -> list[int]:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == "__main__":
    test_arr = [12, 11, 13, 5, 6]
    print(f"Sorted: {insertion_sort(test_arr)}")
