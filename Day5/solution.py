def ticket_list_maker(input_file):
    ticket_list = []
    with open(input_file, "r") as tickets:
        for line in tickets:
            ticket_list.append(line.rstrip("\n"))
    return ticket_list


def ticket_splitter(ticket):
    temp = {}
    temp["row"] = ticket[:7]
    temp["column"] = ticket[-3:]
    return temp

def row_translator(row):
    lower = 0
    upper = 127
    for direction in row:
        mid = (upper - lower) // 2 + lower
        if direction == "F":
            upper = mid
        else:
            lower = mid + 1
    return int(lower)

def column_translator(column):
    lower = 0
    upper = 7
    for direction in column:
        mid = (upper - lower) // 2 + lower
        if direction == "L":
            upper = mid
        else:
            lower = mid + 1
    return int(lower)

def seat_id_generator(ticket):
    return ticket["row"] * 8 + ticket["column"]


def main_function(input_file):
    boarding_passes = []
    ticket_list = ticket_list_maker(input_file)
    for ticket in ticket_list:
        ticket = ticket_splitter(ticket)
        ticket["row"] = row_translator(ticket["row"])
        ticket["column"] = column_translator(ticket["column"])
        ticket["seat_id"] = seat_id_generator(ticket)
        boarding_passes.append(ticket)
    return boarding_passes

def highest_seat_id(boarding_passes):
    highest_id = 0
    for boarding_pass in boarding_passes:
        if boarding_pass["seat_id"] > highest_id:
            highest_id = boarding_pass["seat_id"]
    return highest_id

print(highest_seat_id(main_function("input.txt")))