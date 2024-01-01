class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.start = 0 - step
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == self.count:
            raise StopIteration
        self.counter += 1
        self.start += self.step
        return self.start



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