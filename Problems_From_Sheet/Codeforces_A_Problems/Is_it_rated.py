n = int(input())
state = ""
check_state = []


while(n):
    a, b = map(int, input().split(" "))
    if b - a > 0 or b - a < 0:
        state = "rated"
        break
    else:
        check_state.append(a)
    n = n-1

if state == "rated":
    print(state)
else:
    for i in range(len(check_state)):
        if i+1 <= len(check_state)-1:  # garding against => index out of range
            if check_state[i+1] > check_state[i]:
                state = "unrated"
                break
            else:
                state = "maybe"
        else:
            break
    print(state)
