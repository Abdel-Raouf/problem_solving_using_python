s = reversed([letter for letter in str(input())])
t = str(input())
# s.reverse()
s_str = ''.join(s)

if len(s_str) == len(t):
    if s_str == t:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
