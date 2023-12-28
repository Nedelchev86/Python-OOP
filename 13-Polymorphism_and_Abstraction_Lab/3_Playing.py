class Guitar:
    def play(self):
        return "Playing the guitar"


def start_playing(obj):
    return obj.play()


class Children:
    def play(self):
        return "Children are playing"

children = Children()
print(start_playing(children))


guitar = Guitar()
print(start_playing(guitar))
