n = int(input())
x = []
y = []
z = []

while(n):
    a, b, c = map(int, input().split(" "))
    x.append(a)
    y.append(b)
    z.append(c)
    n = n-1


if (sum(x) == 0 and sum(y) == 0 and sum(z) == 0):
    print("YES")
else:
    print("NO")


# for further use when have a huge number of input lines separated by spaces

# we assign list here to be able to push every list map() makes in the loop
# vector_points = list()
# reading line by line by applying map() function to everyline and neglect spaces
# for i in range(n):
#   vector_points += list(map(int, input().split(" ")))
