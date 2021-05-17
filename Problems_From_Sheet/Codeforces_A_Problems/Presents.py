n = int(input())
friends = list(map(int, input().split(" ")))

solution = [0] * n  # make a list of specfic size

for i in range(n):
    solution[friends[i] - 1] = i + 1

print(" ".join(map(str, solution)))

# for each_steward in range(no_of_stewards):
# steward_support_set.add(stewards_strength[each_steward])
# no_of_steward_jon_will_help = len(steward_support_set) - 2
