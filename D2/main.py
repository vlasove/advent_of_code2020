"""
D2 password validation
"""
import sys


class PasswordValidation:
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__file_handler = open(file_name, "r")
        self.__valid_counter = 0

    def __calculate_validations(self):
        lines = [x.strip() for x in self.__file_handler.readlines()]
        for line in lines:
            blocks = line.split()
            minimum, maximum = [int(x) for x in blocks[0].split("-")]
            letter = blocks[1][:-1]
            password = blocks[2]
            if password.count(letter) >= minimum and password.count(
                    letter) <= maximum:
                self.__valid_counter += 1

    def get_valid_counter(self):
        self.__calculate_validations()
        return self.__valid_counter


def main():
    pv = PasswordValidation(sys.argv[1])
    print(pv.get_valid_counter())


if __name__ == "__main__":
    main()
