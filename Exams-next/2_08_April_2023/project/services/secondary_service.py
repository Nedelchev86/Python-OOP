from project.services.base_service import BaseService


class SecondaryService(BaseService):
    capacity = 15

    def __init__(self, name):
        super().__init__(name, SecondaryService.capacity)

    def details(self):
        # if not self.robots:
        #     return f"{self.name} Secondary Service:\nRobots: none"
        # return f"{self.name} Secondary Service:\nRobots: {' '.join(r.name for r in self.robots)}"
        return f"{self.name} Secondary Service:\nRobots: {self._get_names()}"
