number = int(input())

for i in range(number +1):
    print(" " *(number - i) + "* " * i)

for i in range(number-1, -1, -1):
    print((" " * (number -i)) + ("* " * i))

