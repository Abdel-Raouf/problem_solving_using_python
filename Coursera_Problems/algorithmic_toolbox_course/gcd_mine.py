def GCD(a, b):
    if b != 0:
        GCD(b, a % b)
    else:
        print(a)


GCD(6, 8)


# naiave algorithm for GCD

# def gcd_naive(a, b):
#     current_gcd = 1
#     for d in range(2, min(a, b) + 1):
#         if a % d == 0 and b % d == 0:
#             if d > current_gcd:
#                 current_gcd = d

#     return current_gcd
