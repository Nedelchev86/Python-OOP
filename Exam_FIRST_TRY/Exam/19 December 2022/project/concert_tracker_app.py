from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in ["Guitarist", "Drummer", "Singer"]:
            raise ValueError("Invalid musician type!")
        for musican in self.musicians:
            if musican.name == name:
                raise Exception(f"{name} is already a musician!")
        if musician_type == "Guitarist":
            musician = Guitarist(name, age)
        elif musician_type == "Drummer":
            musician = Drummer(name, age)
        else:
            musician = Singer(name, age)
        self.musicians.append(musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name):
        for band in self.bands:
            if band.name == name:
                raise Exception(f"{name} band is already created!")
        self.bands.append(Band(name))
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        for concert in self.concerts:
            if concert.place == place:
                raise Exception(f"{place} is already registered for {concert.genre} concert!")
        self.concerts.append(Concert(genre, audience, ticket_price, expenses, place))
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        for musican in self.musicians:
            if musican.name == musician_name:
                for band in self.bands:
                    if band.name == band_name:
                        band.members.append(musican)
                        return f"{musician_name} was added to {band_name}."
                raise Exception(f"{band_name} isn't a band!")
        raise Exception(f"{musician_name} isn't a musician!")

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        for band in self.bands:
            if band.name == band_name:
                for names in band.members:
                    if names.name == musician_name:
                        band.members.remove(names)
                        return f"{musician_name} was removed from {band_name}."
                raise Exception(f"{musician_name} isn't a member of {band_name}!")
        raise Exception(f"{band_name} isn't a band!")


    def __find_concert_by_place(self, place: str):
        for concert in self.concerts:
            if concert.place == place:
                return concert

    def __find_band_by_name(self, name: str):
        for band in self.bands:
            if band.name == name:
                return band
        else:
            raise Exception(f"{name} isn't a band!")

    def start_concert(self, concert_place: str, band_name: str):
        for b in self.bands:
            if b.name == band_name:
                band = b
        for c in self.concerts:
            if c.place == concert_place:
                concert = c
        drummer, singer, guitarist = False, False, False
        for member in band.members:
            if member.__class__.__name__ == "Drummer":
                drummer = True
            elif member.__class__.__name__ == "Singer":
                singer = True
            elif member.__class__.__name__ == "Guitarist":
                guitarist = True

        if not drummer or not singer or not guitarist:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        if concert.genre == 'Rock':
            for band_member in band.members:
                if band_member.__class__.__name__ == 'Drummer' and \
                         "play the drums with drumsticks" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Singer' and "sing high pitch notes" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Guitarist' and "play rock" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == 'Metal':
            for band_member in band.members:
                if band_member.__class__.__name__ == 'Drummer' and "play the drums with drumsticks" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Singer' and "sing low pitch notes" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Guitarist' and "play metal" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == 'Jazz':
            for band_member in band.members:
                if band_member.__class__.__name__ == 'Drummer' \
                        and "play the drums with drum brushes" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Singer' \
                        and ("sing low pitch notes" not in band_member.skills
                             or "sing high pitch notes" not in band_member.skills):
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Guitarist' and "play jazz" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = concert.audience * concert.ticket_price - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."








