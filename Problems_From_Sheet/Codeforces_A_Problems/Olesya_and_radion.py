n, t = map(int, input().split(" "))
satisfy_no_list = []
satisfy_no_int = 0
final_no = 0
max_range = n * t
if n == 1:
    if t < 10:
        satisfy_no_list.append(t)
        final_no = satisfy_no_list
    else:
        final_no = -1
else:
    if t < 10:
        for i in range(max_range+1):
            satisfy_no_list.append(t)
            if(len(satisfy_no_list) == n):
                final_no = satisfy_no_list
                break
            else:
                final_no = -1
    else:
        satisfy_no_int = 1
        for i in range(max_range+1):
            satisfy_no_int *= t
            if(len(str(satisfy_no_int)) == n):
                final_no = satisfy_no_int
                break
            else:
                final_no = -1
if t < 10:
    if final_no != -1:
        # concat numbers from a list into a string then convert string to an integer
        print(int(''.join([str(x) for x in final_no])))
    else:
        print(final_no)
else:
    print(final_no)
