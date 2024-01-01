class vowels:
    def __init__(self, text):
        self.text = list(text)
        self.all_vowels = "aeiouAEIOU"
        self.vowels = [el for el in self.text if el in self.all_vowels]

    def __iter__(self):
        return self

    def __next__(self):
        if not self.vowels:
            raise StopIteration
        return self.vowels.pop(0)




my_string = vowels('Abcedifuty0o')
for char in my_string:
 print(char)