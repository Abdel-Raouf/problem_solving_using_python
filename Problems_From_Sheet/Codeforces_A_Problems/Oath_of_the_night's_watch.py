no_of_stewards = int(input())
stewards_strength = list(map(int, input().split(" ")))
john_wonot_help = 0


if no_of_stewards <= 2:
    print(0)
else:
    sorted_steward_strength = sorted(stewards_strength)
    if sorted_steward_strength[0] == sorted_steward_strength[-1]:
        print(0)
    else:
        for i in range(no_of_stewards):
            if sorted_steward_strength[0] == sorted_steward_strength[i]:
                john_wonot_help += 1

            if sorted_steward_strength[-1] == sorted_steward_strength[i]:
                john_wonot_help += 1

        print(no_of_stewards - john_wonot_help)


# Another Good Solution (using min() and max())

# x = int(input())
# d = [int(d) for d in input().split()]
# count = 0
# d1 = min(d)
# d2 = max(d)
# for i in d:
#     if i > d1 and i < d2:
#         count += 1
# print(count)
