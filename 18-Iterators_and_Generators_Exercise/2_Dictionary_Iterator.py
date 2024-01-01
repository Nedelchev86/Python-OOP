class dictionary_iter:
    def __init__(self, dict_obj):
        self.dict_obj = dict_obj
        self.list_from_dict = list(self.dict_obj.items())

    def __iter__(self):
        return self

    def __next__(self):
        if self.list_from_dict:
            return self.list_from_dict.pop(0)
        raise StopIteration




result = dictionary_iter({1: "1", 2: "2"})
for x in result:
 print(x)