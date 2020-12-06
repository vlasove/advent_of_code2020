"""
D2 : password validations
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
            first, second = [int(x) for x in blocks[0].split("-")]
            letter = blocks[1][:-1]
            password = blocks[2]
            if (password[first - 1] == letter and password[second - 1] != letter) or (
                    password[first - 1] != letter and password[second - 1] == letter):
                self.__valid_counter += 1

    def get_valid_counter(self):
        self.__calculate_validations()
        return self.__valid_counter


def main():
    pv = PasswordValidation(sys.argv[1])
    print(pv.get_valid_counter())


if __name__ == "__main__":
    main()
