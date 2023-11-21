def merge(arr1, i, arr2, j):
    buffer = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            buffer.append(arr1[i])
            i += 1
        else:
            buffer.append(arr2[j])
            j += 1
    return buffer + arr1[i:] + arr2[j:]


def divide(arr, left, right):
    # print('got', arr[left:right])
    if right - left <= 1:
        return arr[left:right]

    mid = (left + right) // 2
    arr1 = divide(arr, left, mid)
    arr2 = divide(arr, mid, right)
    return merge(arr1, 0, arr2, 0)


n = int(input().strip())
numbers = list(map(int, input().split()))

print(*divide(numbers, 0, n))
