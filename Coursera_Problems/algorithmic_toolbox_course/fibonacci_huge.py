# Uses python3
import sys

# n = 2015, m = 3


def pisanoPeriod(m):
    previous, current = 0, 1
    # pisano number won't be bigger than m*m, so we make it the upper bound of the loop
    for i in range(0, m * m):

        # we also here make a fibonacci, related to "m", to find when we will find 0 and 1 respectively, which is prev=0 and curr=1
        # swapping memeory address to reassign variables to each other, taking some extra memeory, reference: https://stackoverflow.com/questions/14836228/is-there-a-standardized-method-to-swap-two-variables-in-python
        previous, current = current, ((previous + current) % m)

        # swapping variables using temp
        # temp = current
        # current = ((previous + current) % m)
        # previous = temp

        # A Pisano Period starts with 01
        # if sequence reversed back to prev=0 and curr=1, then we get a sequence and we need to know it's position which is "i+1"
        if (previous == 0 and current == 1):
            return i + 1


def get_fibonacci_huge_naive(n, m):
    pisano = pisanoPeriod(m)
    n = n % pisano
    if n <= 1:
        return n
    else:
        previous, current = 0, 1
        for i in range(2, n+1):  # get fibonacci of 7 which is 13 => current == 13
            previous, current = current, (previous+current)

    return current % m  # 13 % 3 = 1


if __name__ == '__main__':
    # input = sys.stdin.read()
    # n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(2015, 3))
