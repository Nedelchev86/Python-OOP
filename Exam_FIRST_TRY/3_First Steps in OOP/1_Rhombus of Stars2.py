def rhombus_stars(num):
    return F'{(" " * (n -i))  + ("* " * i)}'


n = int(input())

for i in range(n+1):
    print(rhombus_stars(i))

for i in range(n-1, -1, -1):
    print(rhombus_stars(i))