n = int(input())
string_chars = str(input())

if n >= 26:
    char_set = set(char.lower() for char in string_chars)
    if len(char_set) == 26:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
