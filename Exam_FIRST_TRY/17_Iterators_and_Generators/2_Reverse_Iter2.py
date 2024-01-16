class reverse_iter:
    def __init__(self, value: list):
        self.value = list(value)

    def __iter__(self):
        return self

    def __next__(self):
        while self.value:
            return self.value.pop()

        else:
            raise StopIteration


reversed_list = reverse_iter([1, 2, 3, 4, 5, 6])
for item in reversed_list:
    print(item)
