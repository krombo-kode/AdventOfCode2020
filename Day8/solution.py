def instruction_set_writer(input_file):
    instruction_set = []
    with open(input_file, "r") as instruction_file:
        for line in instruction_file:
            line_split = (line.rstrip("\n").split(" "))
            line_split[1] = int(line_split[1])
            instruction_set.append(line_split)
    return instruction_set


def instruction_executor(instruction_set):
    past_indexes = []
    index = 0
    acc = 0
    
    while index not in past_indexes:
        past_indexes.append(index)
        if instruction_set[index][0] == "nop":
            if index + 1 > len(instruction_set):
                index = 0
            else:
                index += 1
        elif instruction_set[index][0] == "acc":
            acc += instruction_set[index][1]
            if index + 1 > len(instruction_set):
                index = 0
            else:
                index += 1
        elif instruction_set[index][0] =="jmp":
            if index + instruction_set[index][1] > len(instruction_set):
                index = (index + instruction_set[index][1]) - (len(instruction_set) + 1)
            index += instruction_set[index][1]
    return acc


def main_function(input_file):
    instruction_set = instruction_set_writer(input_file)
    accumulator = instruction_executor(instruction_set)
    return accumulator

print(main_function("input.txt"))