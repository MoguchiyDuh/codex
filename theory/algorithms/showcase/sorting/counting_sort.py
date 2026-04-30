from __future__ import annotations


def counting_sort(arr: list[int]) -> list[int]:
    if not arr:
        return arr

    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1

    count = [0] * range_of_elements
    output = [0] * len(arr)

    for x in arr:
        count[x - min_val] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1

    return output


if __name__ == "__main__":
    test_arr = [4, 2, 2, 8, 3, 3, 1]
    print(f"Sorted: {counting_sort(test_arr)}")
