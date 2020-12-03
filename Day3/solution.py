def row_generator(text):
    rows = []
    file = open(f"{text}", "r")
    for row in file:
        rows.append(row.rstrip("\n"))
    return rows


def tree_or_not(position_contents):
    if position_contents == "#":
        return "X"
    return "O"


def traverse_slope(position_x, x_trav, row):
    position_x += x_trav
    if position_x > len(row)-1:
        position_x -= len(row)
    return position_x


def tree_counter(tree_map, x_trav, y_trav):
    x, y = 0, 0
    tree_count = 0
    slope = row_generator(tree_map)
    for y in range(0, len(slope), y_trav):
        if tree_or_not(slope[y][x]) == "X":
            tree_count += 1
        x = traverse_slope(x, x_trav, slope[y])
    return tree_count


def main_function(tree_map, traversal_patterns):
    product = 1
    for pattern in traversal_patterns:
        tree_count = 0
        tree_count = tree_counter(tree_map, pattern[0], pattern[1])
        product *= tree_count
    return product


travel_patterns = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

print(main_function("input.txt", travel_patterns))
