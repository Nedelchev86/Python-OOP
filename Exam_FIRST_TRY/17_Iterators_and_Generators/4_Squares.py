# def squares(nums):
#     for i in range(1, nums + 1):
#         yield i ** 2
#
# print(list(squares(5)))


# def squares(nums):
#     i = 1
#     while i <= nums:
#         yield i ** 2
#         i += 1

def squares(nums):
    i = 1
    while i <= nums:
        yield i * i
        i += 1


print(list(squares(5)))
