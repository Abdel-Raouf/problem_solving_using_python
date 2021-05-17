n = int(input())
vis = set()
a = list(map(int, input().split(" ")))
for i in range(n):
    vis.add(a[i])
    while n in vis:
        print(n, end=" ")
        n -= 1
    print()
