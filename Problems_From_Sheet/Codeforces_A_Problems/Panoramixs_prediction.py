# Python3 implementation of the approach
import math

# Function that returns True if n
# is prime USING 6k+1 AND 6K-1 formulas, else returns False


def is_prime(n):

    # Corner cases
    if(n <= 1):
        return False
    if(n <= 3):
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if(n % 2 == 0 or n % 3 == 0):
        return False

    for i in range(5, int(math.sqrt(n) + 1), 6):
        if(n % i == 0 or n % (i + 2) == 0):
            return False

    return True

# Function to return the smallest
# prime number greater than N


def next_prime(N):

    # Base case
    if (N <= 1):
        return 2

    prime = N
    found = False

    # Loop continuously until is_prime returns
    # True for a number greater than n
    while(not found):
        prime = prime + 1

        if(is_prime(prime) == True):
            found = True

    return prime


n, m = map(int, input().split())

if next_prime(n) == m:
    print("YES")
else:
    print("NO")
