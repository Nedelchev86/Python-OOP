class reverse_iter:
    def __init__(self, value: list):
        self.value = value
        self.idx = len(self.value)

    def __iter__(self):
        return self

    def __next__(self):
        while self.idx > 0:
            self.idx -= 1
            return self.value[self.idx]
        else:
            raise StopIteration


reversed_list = reverse_iter("ivan")
for item in reversed_list:
    print(item)
