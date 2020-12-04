import copy

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
    return entries


def valid_checker(item, checks):
    for field in checks:
        if field not in item:
            return 0
    return 1


def valid_counter(entries, checks):
    count = 0
    for item in entries:
        count += valid_checker(entries[item], checks)
    return count


def main_function(file, checks):
    lines = line_maker(file)
    entries = entry_assembler(lines)
    entries = entry_cleaner(entries)
    return valid_counter(entries, checks)


CHECKS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
print(main_function("input.txt", CHECKS))
