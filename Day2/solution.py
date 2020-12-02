def list_generator(text):
    lines = []
    file = open(f"{text}", "r")
    for line in file:
        lines.append(line.split(" "))
    return lines


def list_cleaner(password_list):
    for entry in password_list:
        entry[0] = entry[0].split("-")
        entry[1] = entry[1][:1]
        entry[2] = entry[2].rstrip("\n")
    return password_list


def rule_check_1(entry):
    min_count, max_count = int(entry[0][0]), int(entry[0][1])+1
    check_char = entry[1]
    password = entry[2]
    if password.count(check_char) in range(min_count, max_count):
        return True
    return False


def rule_check_2(entry):
    pos_1, pos_2 = int(entry[0][0])-1, int(entry[0][1])-1
    check_char = entry[1]
    password = entry[2]
    return (password[pos_1] == check_char) != (password[pos_2] == check_char)


def valid_counter(password_list, rule):
    count = 0
    for entry in password_list:
        if rule(entry):
            count += 1
    return count


def main_function(input, rule):
    pass_list = list_generator(input)
    list_cleaner(pass_list)
    valid_count = valid_counter(pass_list, rule)
    return valid_count


print(main_function("input.txt", rule_check_1))
print(main_function("input.txt", rule_check_2))
