# number theory: watch out for patterns in numbers.
num = int(input())
if num == 0:
    print("1")
elif num % 4 == 0:
    print("6")
elif num % 4 == 1:
    print("8")
elif num % 4 == 2:
    print("4")
else:
    print("2")
