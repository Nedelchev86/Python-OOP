class take_skip:
    def __init__(self, step, end):
        self.step = step
        self.end = end
        self.iterator = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterator == self.end - 1:
            raise StopIteration
        self.iterator += 1
        return self.iterator * self.step



numbers = take_skip(2, 6)
for number in numbers:
    print(number)
