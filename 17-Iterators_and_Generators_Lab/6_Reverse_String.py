# def reverse_text(some_string):
#     string = list(some_string)
#     while string:
#         yield string.pop()


def reverse_text(some_string):
    count = len(some_string) - 1
    while count >= 0:
        yield some_string[count]
        count -= 1



for char in reverse_text("step"):
 print(char, end='')
