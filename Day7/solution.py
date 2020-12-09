def rule_writer(input_file):
    rules = {}
    bag_words = [" bag.", " bag" " bags.", " bags", " bag"]
    with open(input_file, "r") as source:
        for line in source:
            for bag_word in bag_words:
                line = line.replace(bag_word, "")
            line = line.split(" contain ")
            line[0]= line[0].strip()
            rules[line[0]] = {}
            line[1] = line[1].rstrip(" .\n").split(", ")
            for definition in line[1]:
                if definition == "no other":
                    rules[line[0]] = {}
                else:
                    key = definition[2:]
                    value = int(definition[0])
                    rules[line[0]][key] = value
    return rules


def contains_bag(color, bags):
    return [c for c in bags if color in bags[c]]


def outer_bags(color, bags):
    valid_bags = {color}
    new_bag = True 
    while new_bag:
        new_bag = False
        for bag in list(valid_bags):
            for container_color in contains_bag(bag, bags):
                if container_color not in valid_bags:
                    valid_bags.add(container_color)
                    new_bag = True
    return valid_bags - {color}


def main_function(input_file):
    rules = rule_writer(input_file)
    count = outer_bags("shiny gold", rules)
    return count

def bag_contents(color, bags):
    contained_bags = 0
    for bag, n in bags[color].items():
        contained_bags += n + n * bag_contents(bag, bags)
    return contained_bags

print(len(main_function("input.txt")))
print(bag_contents("shiny gold", rule_writer("input.txt")))