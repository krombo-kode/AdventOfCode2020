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


def ticket_translator(segment, segment_type):
    lower = 0
    if segment_type == "R":
        upper = 127
    elif segment_type == "C":
        upper = 7
    for direction in segment:
        mid = (upper - lower) // 2 + lower
        if direction == "L" or direction == "F":
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
        ticket["row"] = ticket_translator(ticket["row"], "R")
        ticket["column"] = ticket_translator(ticket["column"], "C")
        ticket["seat_id"] = seat_id_generator(ticket)
        boarding_passes.append(ticket)
    return boarding_passes


def highest_seat_id(boarding_passes):
    highest_id = 0
    for boarding_pass in boarding_passes:
        if boarding_pass["seat_id"] > highest_id:
            highest_id = boarding_pass["seat_id"]
    return highest_id


def seat_locator(boarding_passes):
    seat_map = []
    for i in range(0, 127):
        seat_map.append([])
    for boarding_pass in boarding_passes:
        seat_map[boarding_pass["row"]].append(boarding_pass["seat_id"])
    for row in seat_map:
        if len(row) == 7:
            seat_row = sorted(row)
    for i in range(0, 6):
        if seat_row[i+1] - seat_row[i] != 1:
            return seat_row[i]+1


print(highest_seat_id(main_function("input.txt")))
print(seat_locator(main_function("input.txt")))
