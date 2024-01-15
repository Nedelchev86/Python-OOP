from calendar import month_name


class DVD:
    def __init__(self, name, some_id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = some_id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, some_id: int, name: str, date: str, age_restriction: int):
        day, month, year = [int(x) for x in date.split(".")]
        month = month_name[month]
        return cls(name, some_id, year, month, age_restriction)

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) " \
               f"has age restriction {self.age_restriction}. Status: {'rented' if self.is_rented else 'not rented'}"

