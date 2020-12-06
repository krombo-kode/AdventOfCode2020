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


def yes_counter(group):
    result = len(set("".join(group)))
    return result


def yes_sum_finder(groups):
    total = 0
    for group in groups:
        total += yes_counter(group)
    return total


print(yes_sum_finder(answer_list_maker("input.txt")))
