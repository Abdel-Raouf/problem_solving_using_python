stat_no = int(input())
lines = ""
counter = 0

# TODO : we need to loop through inputs based on stat_no
for i in range(stat_no):
    line = str(input())+"\n"
    if line.find("+") != -1:
        counter += 1
    else:
        counter -= 1

print(counter)
