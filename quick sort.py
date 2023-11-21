def median_of_three(arr, left, right):
    mid = (left + right) // 2
    if arr[left] > arr[mid]:
        arr[left], arr[mid] = arr[mid], arr[left]
    if arr[left] > arr[right]:
        arr[left], arr[right] = arr[right], arr[left]
    if arr[mid] > arr[right]:
        arr[mid], arr[right] = arr[right], arr[mid]
    return arr[mid]


def partition(arr, left, right):
    pivot = median_of_three(arr, left, right)

    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return left


def quicksort(arr, left, right):
    if left < right:
        q = partition(arr, left, right)
        quicksort(arr, left, q - 1)
        quicksort(arr, q, right)


n = int(input().strip())
numbers = list(map(int, input().split()))

quicksort(numbers, 0, n-1)
print(*numbers)