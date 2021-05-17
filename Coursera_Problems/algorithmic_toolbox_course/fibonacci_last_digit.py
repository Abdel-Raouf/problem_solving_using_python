# Uses python3
import sys


def get_fibonacci_last_digit_naive(n):

    fibonacci_list = []

    fibonacci_list.insert(0, 0)
    fibonacci_list.insert(1, 1)

    if (n <= 1):
        return n
    else:
        for nth_number in range(2, n+1):
            fibonacci_list.insert(nth_number, (fibonacci_list[nth_number-1]
                                               + fibonacci_list[nth_number-2]) % 10)

    return fibonacci_list[-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
