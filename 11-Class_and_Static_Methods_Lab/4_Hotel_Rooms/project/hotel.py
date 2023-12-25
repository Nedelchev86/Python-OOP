from project.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                result = room.take_room(people)
                if result:
                    return result

                self.guests += people

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                guests = room.guests
                result = room.free_room()

                if result:
                    return result

                self.guests -= guests

    def status(self):
        result = [f"Hotel {self.name} has {self.guests} total guests"]
        free_rooms = [str(room.number) for room in self.rooms if not room.is_taken]
        taken_rooms = [str(room.number) for room in self.rooms if room.is_taken]
        result.append(F"Free rooms: {', '.join(free_rooms)}")
        result.append(f"Taken rooms: {', '.join(taken_rooms)}")
        return "\n".join(result)
