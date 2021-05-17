# Uses python3
import sys


def GCD(a, b):
    if b != 0:
        return GCD(b, a % b)
    else:
        return a


def lcm_naive(a, b):
    greatest_common_divisor = GCD(a, b)
    multiplication = a*b

    return multiplication // greatest_common_divisor


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))


# for l in range(1, a*b + 1):
#         if l % a == 0 and l % b == 0:
#             return l

#     return a*b
