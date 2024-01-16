class vowels:
    def __init__(self, text: str):
        self.text = text
        self.vowels = "AEIOUYaeiouy"
        self.idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        while self.idx < len(self.text) -1:
            self.idx += 1
            if self.text[self.idx] in self.vowels:
                return self.text[self.idx]
        else:
            raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
