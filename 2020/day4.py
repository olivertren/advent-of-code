from utils import get_input, print_answers

VALID = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def solution(passports, correct):
    count = 0
    current = set()
    for line in passports:
        if line:
            for stat in line.split():
                s, value = stat.split(":")
                if correct(s, value):
                    current.add(s)
        else:
            if VALID.issubset(current):
                count += 1
            current = set()
    return count


def correct(stat, value):
    if stat == "cid":
        return True
    elif stat == "byr":
        return 1920 <= int(value) <= 2002
    elif stat == "iyr":
        return 2010 <= int(value) <= 2020
    elif stat == "eyr":
        return 2020 <= int(value) <= 2030
    elif stat == "hgt":
        measure = value[-2:]
        value = value[:-2]
        if measure == "cm":
            return 150 <= int(value) <= 193
        elif measure == "in":
            return 59 <= int(value) <= 76
        else:
            return False
    elif stat == "hcl":
        pound = value[0]
        value = value[1:]
        if pound != "#":
            return False
        else:
            valid = {
                "0",
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "a",
                "b",
                "c",
                "d",
                "e",
                "f",
            }
            return set(value).issubset(valid)
    elif stat == "ecl":
        return value in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    elif stat == "pid":
        return len(value) == 9 and int(value) >= 0
    else:
        return False


passports = get_input(__file__)
passports.append("")
print_answers(solution(passports, lambda _, __: True), solution(passports, correct))
