levels_no = int(input())
little_x = list(map(int, input().split(" ")))
little_y = list(map(int, input().split(" ")))
result_set = set()

for i in range(1, little_x[0]+1):
    result_set.add(little_x[i])

for j in range(1, little_y[0]+1):
    result_set.add(little_y[j])

if len(result_set) == levels_no:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
