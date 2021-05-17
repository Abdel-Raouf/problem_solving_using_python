n = int(input())
first_line = str(input())
sum_letters_diff_from_diag_calculation = int(((n - 2) * n) + 1)
sum_for_each_line = int(n - 2)
state = ''

for i in range(n-1):
    from_secLine_and_above = str(input())
    if first_line[0] != from_secLine_and_above[i+1]:
        state = "NO"
        break

    if first_line[-1] != from_secLine_and_above[(-i-1)-1]:
        state = "NO"
        break

    if n > 3:
        if first_line[1] == first_line[2] and first_line[2] == first_line[3]:
            sum_for_each_line += from_secLine_and_above.count(
                first_line[1])
        else:
            state = "NO"
            break
    elif n == 3:
        if first_line[1] != first_line[0]:
            sum_for_each_line += from_secLine_and_above.count(first_line[1])
        else:
            state = "NO"
            break
    else:
        state = "NO"
        break

if len(state) == 0:
    if sum_for_each_line == sum_letters_diff_from_diag_calculation:
        print("YES")
    else:
        print("NO")
else:
    print(state)
