word = str(input())
n = int(input())

x = 257
p = 101021
a = [0 for _ in range(len(word) + 1)]
h = [0 for _ in range(len(word) + 1)]
x_powers = [1] + [0] * len(word)

for i in range(1, len(x_powers)):
    x_powers[i] = (x_powers[i - 1] * x) % p

for i, char in enumerate(word):
    a[i+1] = ord(char)
    h[i+1] = (h[i] * x + a[i+1]) % p

for i in range(n):
    length, from1, from2 = list(map(int, input().split()))

    if (h[from1 + length] + h[from2] * x**length) % p == (h[from2 + length] + h[from1] * x**length) % p:
        print('yes')
    else:
        print('no')

