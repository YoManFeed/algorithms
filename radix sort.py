def radix_sort(number, digit, decimal):
    # print(f'number = {number}, digit = {digit}, decimal is {decimal}')
    number_list[int(digit)].append(number)


n = int(input())

bucket_list = [''] * n
number_list = [[], [], [], [], [], [], [], [], [], []]

for i in range(n):
    bucket_list[i] = (str(input()))

max_length = len(str(max(bucket_list)))

print('Initial array:')
print(', '.join(num for num in bucket_list))
# print('**********')

# print(bucket_list)

for decimal in reversed(range(max_length)):
    print('**********')
    print(f'Phase {max_length - decimal}')
    number_list = [[], [], [], [], [], [], [], [], [], []]
    for number in bucket_list:
        radix_sort(number, number[decimal:decimal+1], max_length - decimal)

    ans = []
    for elem in number_list:
        if elem != []:
            ans = ans + elem
    bucket_list = ans

    for i, elem in enumerate(number_list):
        if elem != []:
            print(f'Bucket {i}:', ', '.join(num for num in elem))
        else:
            print(f'Bucket {i}: empty')

print('**********')
print('Sorted array:')
print(', '.join(num for num in bucket_list))
