class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if len(value) >= 5 and len(value) <= 15:
            self.__username = value
        else:
            raise ValueError("The username must be between 5 and 15 characters.")

    @property
    def password(self):
        return self.__password

    # @password.setter
    # def password(self, value):
    #     if len(value) >= 8 and any(x.isdigit() for x in value) and any(x.isalpha() and x == x.upper() for x in value):
    #         self.__password = value
    #     else:
    #         raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    @password.setter
    def password(self, value):
        if len(value) < 8 or not any(s.isdigit() for s in value) or not any(
                s.isalpha() and s == s.upper() for s in value):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = value


    def __str__(self):
        return f'You have a profile with username: "{self.__username}" and password: {"*" * len(self.__password)}'


correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)