import math

no_of_coins = int(input())
coins_values = list(map(int, input().split(" ")))

whole_sum = sum(coins_values)
sorted_coin_values = sorted(coins_values)
values_counter = 0
remaining_value = 0

if no_of_coins == 1:
    print(1)
else:
    for i in range(1, int(math.ceil(no_of_coins/2))+1):  # o(n)
        values_counter += sorted_coin_values[-i]
        remaining_value = whole_sum - values_counter

        if values_counter > remaining_value:
            print(i)
            break
        elif remaining_value == values_counter:
            print(i+1)
            break
