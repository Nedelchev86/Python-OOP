class dictionary_iter:
    def __init__(self, some_dict: dict):
        self.some_dict = some_dict
        self.items = list(self.some_dict.items())
        self.idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx == len(self.items) - 1:
            raise StopIteration
        self.idx += 1
        return self.items[self.idx]



