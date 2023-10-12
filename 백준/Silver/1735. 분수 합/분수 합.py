from math import gcd

A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))

C = (A[0] * B[1] + A[1] * B[0], A[1] * B[1])

if gcd(*C) != 1:
    C = (C[0] // gcd(*C), C[1] // gcd(*C))

print(*C)
