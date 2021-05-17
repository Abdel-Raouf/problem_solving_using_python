
n = list(map(int, input().split(" ")))
seq = n[0]
position = n[1]
result = 0

if seq % 2 == 0:
    if position <= int((seq/2)):
        result = (position*2) - 1
    else:
        position_after_odd = position - int((seq/2))
        result = position_after_odd * 2
else:
    if position <= int((seq/2)+1):
        result = (position * 2) - 1
    else:
        position_after_odd = position - int((seq/2)+1)
        result = position_after_odd * 2

print(result)

#  Time limit exceeded solution

# n = list(map(int, input().split(" ")))
# seq = n[0]
# position = n[1]
# remain = seq - position
# odd_list = list()
# even_list = list()
# result = 0

# for num in range(1, seq+1):
#     if num % 2 != 0:
#         odd_list.append(num)
#     else:
#         even_list.append(num)

# if seq % 2 == 0:
#     if seq / 2 <= remain:
#         result = odd_list[position - 1]
#     else:
#         result = even_list[(position - len(odd_list)) - 1]
# else:
#     if int(seq / 2) <= remain:
#         result = odd_list[position - 1]
#     else:
#         result = even_list[(position - len(odd_list)) - 1]

# # print(odd_list, even_list)
# # print(odd_list + even_list)
# print(result)
