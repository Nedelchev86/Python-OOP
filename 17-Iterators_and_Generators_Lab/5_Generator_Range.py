def genrange(start, end):
    while start <= end:
        yield start
        start += 1


# def genrange(start, end):
#     count = start
#     while count  <= end:
#         yield count
#         count += 1







print(list(genrange(1, 10)))