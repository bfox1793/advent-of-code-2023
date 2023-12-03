import re

## Parse file
my_file = open("inputs/day1.txt", "r")
content = my_file.read()
input_array = content.split("\n")


number_map = {
        "one" : "1",
        "two" : "2",
        "three" : "3",
        "four" : "4",
        "five" : "5",
        "six" : "6",
        "seven" : "7",
        "eight" : "8",
        "nine" : "9"
    }

curr_sum = 0

def is_number_present(string):
    for char in string:
        if char.isdigit():
            return True
    return False

def get_first_digit_from_string(string, is_reversed):
    total_string = ""
    for current_char in string:
        if is_reversed:
            total_string = current_char + total_string
        else:
            total_string += current_char
        keys = number_map.keys()
        for key in keys:
            total_string = total_string.replace(key, number_map[key])
        for char in total_string:
            if char.isdigit():
                return char

    print("A NUMBER WAS NOT FOUND! SOMETHING WENT WRONG")

    print("A NUMBER WAS NOT FOUND! SOMETHING WENT WRONG")


for line in input_array:
    first_int = get_first_digit_from_string(line, False)
    last_int = get_first_digit_from_string(line[::-1], True)

    combined_number = first_int + last_int
    curr_sum += int(combined_number)

print(curr_sum)
