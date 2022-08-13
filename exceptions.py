class IncorrectKey(Exception):
    def __init__(self, message="Key is invalid. Try selecting another key"):
        self.message = message
        super().__init__(self.message)