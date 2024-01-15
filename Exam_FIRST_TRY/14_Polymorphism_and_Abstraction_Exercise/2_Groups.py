class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        return f"{self.name} {other.surname}"


class Group:
    def __init__(self, name, people):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        return Group(f"{self.name} {other.name}", self.people + other.people)

    def __str__(self):
        return f"Group {self.name} with members {', '.join(str(x) for x in self.people)}"

    def __getitem__(self, item):
        return f"Person {item}: {str(self.people[item])}"

