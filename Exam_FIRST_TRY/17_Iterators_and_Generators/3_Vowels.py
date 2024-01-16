class vowels:
    def __init__(self, text: str):
        self.text = list(text)
        self.vowels =  "AEIOUYaeiouy"

    def __iter__(self):
        return self

    def __next__(self):
        while self.text:
            current = self.text.pop(0)
            if current in self.vowels:
                return current
        else:
            raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
