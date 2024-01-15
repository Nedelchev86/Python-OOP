from project.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(F"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number and not room.is_taken and room.capacity >= people:
                room.is_taken = True
                room.guests += people

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                if room.is_taken:
                    room.is_taken = False
                    room.guests = 0

    def status(self):
        free_room = [str(x.number) for x in self.rooms if not x.is_taken]
        taken_room = [str(x.number) for x in self.rooms if x.is_taken]

        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join(free_room)}\nTaken rooms: {', '.join(taken_room)}"


