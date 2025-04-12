class UserAuth:
    # users = [("username1", "password1"), ("admin", "1234"), ("user", "wrongpass"), ("Unknown", "pass")]

    def __init__(self, users):
        for un, pw in users:


    def login(self, username, password):
        for un, pw in self.users:
            if un == self.username and pw == self.password:
                print("Login successful")
                return


class UserNotFoundError(Exception):
    pass


class WrongPasswordError(Exception):
    pass


auth = UserAuth("username1", "password2")
auth.login()
