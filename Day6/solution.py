import copy


def answer_list_maker(input_file):
    groups_answers = []
    with open(input_file, "r") as file:
        temp_lines = []
        for line in file:
            if line != "\n":
                temp_lines.append(line.rstrip("\n"))
            else:
                groups_answers.append(copy.copy(temp_lines))
                temp_lines.clear()
        groups_answers.append(copy.copy(temp_lines))
    return groups_answers


def any_yes_counter(group):
    result = len(set("".join(group)))
    return result


def all_yes_counter(group):
    count = 0
    answers = "".join(group)
    checks = set(answers)
    for check in checks:
        if answers.count(check) == len(group):
            count +=1
    return count



def yes_sum_finder(groups,func):
    total = 0
    for group in groups:
        total += func(group)
    return total


print(yes_sum_finder(answer_list_maker("input.txt"),any_yes_counter))
print(yes_sum_finder(answer_list_maker("input.txt"),all_yes_counter))
