## Parse file
my_file = open("inputs/day3.txt", "r")
content = my_file.read()
input_array = content.split("\n")

def get_number_from_position(y,x):
  total_number = ""
  current_number = input_array[y][x]

  # find leftmost digit
  # need to normalize x so this works no matter where we start
  while(current_number.isnumeric()):
    if x == 0:
      break
    if not(input_array[y][x-1].isnumeric()):
      break
    x -= 1
    current_number = input_array[y][x]
    print("Current check: " + input_array[y][x] )
  
  while(current_number.isnumeric()):
    # print("Current Number: " + current_number)
    total_number += current_number
    # print("Total Number: " + total_number)
    x += 1
    # safety
    if x >= len(input_array[y]):
      break
    current_number = input_array[y][x]
  print("Final Number: " + total_number)
  return total_number

def is_object(y,x):
  print(input_array[y][x])
  if input_array[y][x] == ".":
    return False
  elif input_array[y][x].isnumeric():
    return False
  return True

def is_number_valid(number, y, x):
  print("Checking number validity: " + number)
  # check left
  if x-1 >= 0:
    if is_object(y,x-1):
      return True
  # check right
  if x + len(number) + 1 <= len(input_array[y])-1:
    if is_object(y,x + len(number)):
      return True
  # check above & below
  for curr_x in range(x, x + len(number)):
    print("Current number position: " + str(curr_x))
    # check above
    if y != 0:
      if is_object(y-1, curr_x):
        return True
    # check below
    if y != len(input_array) - 1:
      if is_object(y+1, curr_x):
        return True
  # check left diagonals
  if x != 0 and y != 0:
    if is_object(y-1, x-1):
      return True
  if x != 0 and y != len(input_array) - 1:
    if is_object(y+1, x-1):
      return True
  # check right diagonals
  right_x = x + len(number) - 1
  # right up
  if right_x != len(input_array[y]) - 1 and y != 0:
    if is_object(y-1, right_x + 1):
      return True
  # right down
  if right_x != len(input_array[y]) - 1 and y != len(input_array) - 1:
    if is_object(y+1, right_x + 1):
      return True
  return False
y=0
x=0

valid_numbers = []
while y < len(input_array):
  while x < len(input_array[y]):
    current_char = input_array[y][x]
    if current_char.isnumeric():
      # figure out total number
      total_number = get_number_from_position(y,x)
      # check left, right, above, below, diag to number
      if is_number_valid(total_number, y, x):
        print("Number: " + total_number + " is valid!")
        valid_numbers.append(total_number)
      # if special char exists, count
      # else, continue
      x += len(total_number) - 1
    x += 1
  y += 1
  x = 0

total_sum = 0
for num in valid_numbers:
  print("valid number: " + str(num))
  total_sum += int(num)

print("Total Sum: " + str(total_sum))

## part 2

print("STARTING PART 2")
def get_gear_ratio(y,x):
  adjacent_numbers = []
  # find all adjacent numbers
  # check left
  if x-1 >= 0:
    if input_array[y][x-1].isnumeric():
      adjacent_numbers.append(get_number_from_position(y,x-1))
  # check right
  if x + 1 <= len(input_array[y])-1:
    if input_array[y][x+1].isnumeric():
      adjacent_numbers.append(get_number_from_position(y,x+1))
  # check above
  if y != 0:
    if input_array[y-1][x].isnumeric():
      adjacent_numbers.append(get_number_from_position(y-1,x))
  # check below
  if y != len(input_array) - 1:
    if input_array[y+1][x].isnumeric():
      adjacent_numbers.append(get_number_from_position(y+1,x))
  # # check left diagonals
  if x != 0 and y != 0:
    if input_array[y-1][x-1].isnumeric():
      adjacent_numbers.append(get_number_from_position(y-1,x-1))
  if x != 0 and y != len(input_array) - 1:
    if input_array[y+1][x-1].isnumeric():
      adjacent_numbers.append(get_number_from_position(y+1,x-1))
  # # check right diagonals
  # # right up
  if x != len(input_array[y]) - 1 and y != 0:
    if input_array[y-1][x+1].isnumeric():
      adjacent_numbers.append(get_number_from_position(y-1,x+1))
  # # right down
  if x != len(input_array[y]) - 1 and y != len(input_array) - 1:
    if input_array[y+1][x+1].isnumeric():
      adjacent_numbers.append(get_number_from_position(y+1,x+1))
  # if adjacent numbers == 2, return product
  
  if len(set(adjacent_numbers)) == 2:
    curr_product = 1
    for num in set(adjacent_numbers):
      curr_product *= int(num)
    return curr_product
  return 0
x=0
y=0
gear_ratios = []
while y < len(input_array):
  while x < len(input_array[y]):
    current_char = input_array[y][x]
    if current_char == "*":
      print("This is a potential gear!")
      gear_ratios.append(get_gear_ratio(y,x))

      
      
    x += 1
  y += 1
  x = 0

total_ratio = 0
for ratio in gear_ratios:
  total_ratio += ratio
  print("Gear ratio: " + str(ratio))

print("Total gear ratio: " + str(total_ratio))