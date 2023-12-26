class ExercisePlan:
    exercise_plan = 1

    def __init__(self,trainer_id: int, equipment_id: int, duration: int):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = ExercisePlan.get_next_id()
        ExercisePlan.exercise_plan += 1

    @staticmethod
    def get_next_id():
        return ExercisePlan.exercise_plan

    @classmethod
    def from_hours(cls, trainer_id:int, equipment_id:int, hours:int):
        return cls(trainer_id, equipment_id, hours * 60)


    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"