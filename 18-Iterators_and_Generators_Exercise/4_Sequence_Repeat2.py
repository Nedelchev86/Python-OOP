class sequence_repeat:
    def __init__(self, text, length):
        self.text = text
        self.length = length
        self.count = 0
        self.idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == self.length:
            raise StopIteration
        self.count += 1
        self.idx += 1
        if self.idx == len(self.text):
            self.idx = 0
        return self.text[self.idx]


result = sequence_repeat('I Love Python', 3)
for item in result:
 print(item, end ='')