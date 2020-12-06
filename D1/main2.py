"""
D1: Find sum of two entries equal to 2020 and get their mult
"""
import sys


class Solution:
    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__file_handler = open(file_name, "r")
        self.__nums = []

    def read_from_file(self):
        self.__nums = [int(x.strip()) for x in self.__file_handler.readlines()]

    def find_values(self):
        self.read_from_file()
        for i in range(len(self.__nums) - 2):
            for j in range(i + 1, len(self.__nums) - 1):
                for k in range(j + 2, len(self.__nums)):
                    if (self.__nums[i] + self.__nums[j] +
                            self.__nums[k] == 2020):
                        return {
                            "first": self.__nums[i],
                            "second": self.__nums[j],
                            "third": self.__nums[k],
                            "mult": self.__nums[i] * self.__nums[j] * self.__nums[k],
                        }


def main():
    sol = Solution(sys.argv[1])
    print(sol.find_values())


if __name__ == "__main__":
    main()
