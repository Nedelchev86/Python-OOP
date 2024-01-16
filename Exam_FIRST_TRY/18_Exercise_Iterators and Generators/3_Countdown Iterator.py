class countdown_iterator:
    def __init__(self, start):
        self.start = start + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start == 0:
            raise StopIteration
        self.start -= 1
        return self.start

iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")
