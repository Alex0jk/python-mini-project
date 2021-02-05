# Credentials will be expanded with the usage for tokens, passphrases with no user,
# security questions, keys (private/public) and no credentials
class Credential:
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def check_correct_credentials(self, user, password):
        return self.user == user and self.password == password
