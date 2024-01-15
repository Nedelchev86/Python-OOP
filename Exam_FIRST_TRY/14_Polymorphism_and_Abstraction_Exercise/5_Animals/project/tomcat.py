# from project.cat import Cat
#
#
# class Tomcat(Cat):
#     gender = "Male"
#
#     def __init__(self, name, age):
#         super().__init__(name, age, self.gender)
#         self.gender = "Male"
#
#     def make_sound(self):
#         return "Hiss"

from project.cat import Cat


class Tomcat(Cat):

    def __init__(self, name, age):
        super().__init__(name, age, "Male")

    def make_sound(self):
        return "Hiss"

