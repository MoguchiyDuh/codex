from __future__ import annotations


def bucket_sort(arr: list[float]) -> list[float]:
    if not arr:
        return arr

    n = len(arr)
    buckets = [[] for _ in range(n)]

    for x in arr:
        index = int(n * x)
        if index == n:
            index = n - 1
        buckets[index].append(x)

    for i in range(n):
        _insertion_sort(buckets[i])

    result = []
    for bucket in buckets:
        result.extend(bucket)
    return result


def _insertion_sort(arr: list[float]):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


if __name__ == "__main__":
    test_arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
    print(f"Sorted: {bucket_sort(test_arr)}")
