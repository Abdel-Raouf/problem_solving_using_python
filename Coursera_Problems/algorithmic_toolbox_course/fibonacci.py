# Uses python3
def calc_fib(n):
    fibonacci_list = []

    fibonacci_list.insert(0, 0)
    fibonacci_list.insert(1, 1)

    if (n <= 1):
        return n
    else:
        for nth_number in range(2, n+1):
            fibonacci_list.insert(nth_number, fibonacci_list[nth_number-1]
                                  + fibonacci_list[nth_number-2])

    return fibonacci_list[-1]


n = int(input())
print(calc_fib(n))
