class dictionary_iter:
    def __init__(self, some_dict: dict):
        self.some_dict = some_dict
        self.items = list(self.some_dict.items())
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx >= len(self.items):
            raise StopIteration
        result = self.items[self.idx]
        self.idx += 1
        return result



result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
