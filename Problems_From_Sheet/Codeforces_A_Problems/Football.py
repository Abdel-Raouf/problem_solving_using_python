no_of_lines = int(input())
first_team = str(input())
sec_team = ''
counter_fir_team = 1

if no_of_lines == 2:
    print(first_team)
else:
    for i in range(no_of_lines-1):
        input_placeholder = str(input())
        if first_team == input_placeholder:
            counter_fir_team += 1
        else:
            sec_team = input_placeholder

if (no_of_lines - counter_fir_team) == 0:
    print(first_team)
else:
    if (no_of_lines - counter_fir_team) < counter_fir_team:
        print(first_team)
    else:
        print(sec_team)
