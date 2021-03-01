class Error(Exception):
    pass


class WrongTypeError(Error):
    def __init__(self, datatype, message="No Info", outtype="object"):
        if outtype != "object":
            self.type = datatype
        self.type = type(datatype)
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"The Object has the wrong type: {self.type}; Additional Info: {self.message}"


class WrongSaltTypeError(WrongTypeError):
    def __init__(self, datatype, message="No Info"):
        self.type = type(datatype)
        self.message = message

    def __str__(self):
        return f"The Salt has the wrong type: {self.type}; Additional Info: {self.message}"

class InvalidLetterError(Error):
    def __init__(self, letter, message="No Info"):
        self.letter = letter
        self.message = message

    def __str__(self):
        return f"The letter {self.letter} is invalid for the operation; Additional Info: {self.message}"

class MissingPackageError(Error):
    def __init__(self, message="No Info"):
        self.message = message
        super().__init__(self.message)

