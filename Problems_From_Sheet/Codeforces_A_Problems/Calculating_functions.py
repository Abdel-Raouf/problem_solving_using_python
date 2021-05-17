n = int(input())

if n & 1:  # using bitwise and to check for last bit only for even or odd
    # rounding up
    print(-(int(n / 2)+1))
else:
    print(int(n / 2))
