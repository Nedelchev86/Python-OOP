# def reverse_text(text):
#     idx = len(text) - 1
#     while idx >= 0:
#         yield text[idx]
#         idx -= 1
#
# for char in reverse_text("step"):
#     print(char, end='')


def reverse_text(text):
    text = list(text)
    while text:
        yield text.pop()

for char in reverse_text("step"):
    print(char, end='')
