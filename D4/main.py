import sys 


class PassportBook:
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__fhand = open(file_name, "r")
        self.__all = []
        self.__ruler = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        self.__valid = 0

    def get_passports(self):
        current_passport = ""
        for line in self.__fhand.readlines():
            current_passport += line.strip() + " "
            if line == "\n":
                # Паспорт прочитан, переходим к следующему
                self.__all.append(current_passport.strip())
                current_passport = ""
        self.__all.append(current_passport)
        return self.__all

    def check_valid(self):
        for passport in self.get_passports():
            checker = []
            for pair in passport.split(" "):
                checker.append(pair.split(":")[0])
            checker.sort()
            if ("cid" in checker):
                checker.remove("cid")
            
            
            if checker == sorted(self.__ruler):
                self.__valid += 1
                

    def get_valid(self):
        self.check_valid()
        return self.__valid

def main():
    pb = PassportBook(sys.argv[1])
    print(pb.get_valid())

if __name__ == "__main__":
    main()
    