

n = int(input())

for i in range(n+1):
    print((" " * (n -i))  + ("* " * i))

for i in range(n-1, -1, -1):
    print((" " * (n -i))  + ("* " * i))