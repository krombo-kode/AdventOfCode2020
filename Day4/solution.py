import copy
import string

def line_maker(file):
    with open(file, "r") as file:
        lines = []
        for line in file:
            lines.append(line.rstrip("\n"))
        return lines


def entry_assembler(lines):
    entries = {}
    id_num = 0
    temp = []
    for item in lines:
        if item == "":
            id_num += 1
            entries[id_num] = copy.copy(temp)
            temp.clear()
        elif item != "":
            temp.append(item)
    id_num += 1
    entries[id_num] = copy.copy(temp)
    temp.clear()
    return entries


def entry_cleaner(entries):
    for id_num in entries:
        entries[id_num] = " ".join(entries[id_num])
        entries[id_num] = entries[id_num].split(" ")
    return entries


def sub_dict_creator(entry):
    sub_dict = {}
    for item in entry:
        items = item.split(":")
        sub_dict[items[0]] = items[1]
    return sub_dict


def field_checker(item, checks):
    for field in checks:
        if field not in item:
            return False
    return True


def year_checker(item, checks):
    if len(item[checks[0]]) != checks[1]:
        return False
    elif int(item[checks[0]]) >= checks[2] and int(item[checks[0]]) <= checks[3]:
        return True


def height_checker(item, checks):
    if item[checks[0]].endswith(checks[1]):
        if int(item[checks[0]][:-2]) >= checks[2] and int(item[checks[0]][:-2]) <= checks[3]:
            return True
        return False
    elif item[checks[0]].endswith(checks[4]):
        if int(item[checks[0]][:-2]) >= checks[5] and int(item[checks[0]][:-2]) <= checks[6]:
            return True
        return False


def hair_checker(item, checks):
    if item[checks[0]].startswith("#"):
        if len(item[checks[0]]) == 7:
            return all(c in string.hexdigits for c in item[checks[0]][1:])
    return False


def eye_checker(item, checks):
    if item[checks[0]] in checks[1:]:
        return True
    return False


def passport_id_checker(item, checks):
    if len(str(item[checks[0]])) == checks[1]:
        return True
    return False


def invalid_entry_remover(entries, function, checks):
    valid = {}
    for item in entries:
        if function(entries[item], checks):
            valid[item] = entries[item]
    return valid


def main_function(file):
    lines = line_maker(file)
    entries = entry_assembler(lines)
    entries = entry_cleaner(entries)
    for entry in entries:
        entries[entry] = sub_dict_creator(entries[entry])
    for function in FUNCTION_LIST:
        entries = invalid_entry_remover(entries, function[0], function[1])
    for year_check in YEAR_CHECKS:
        entries = invalid_entry_remover(entries, year_checker, year_check)
    return len(entries)





FIELD_CHECKS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
YEAR_CHECKS = [
    ["byr", 4, 1920, 2002],
    ["iyr", 4, 2010, 2020],
    ["eyr", 4, 2020, 2030]
]
HEIGHT = ["hgt", "cm", 150, 193, "in", 59, 76]
HAIR_COLOR = ["hcl", 7, "hex"]
EYE_COLOR = ["ecl", "amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
PASSPORT_ID = ["pid", 9]

FUNCTION_LIST = [[field_checker, FIELD_CHECKS],  [height_checker, HEIGHT],
    [hair_checker, HAIR_COLOR], [eye_checker, EYE_COLOR],
    [passport_id_checker, PASSPORT_ID]]



print(main_function("input.txt"))
