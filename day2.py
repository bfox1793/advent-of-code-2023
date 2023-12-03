## Parse file
my_file = open("inputs/day2.txt", "r")
content = my_file.read()
input_array = content.split("\n")

all_games = []

class Draw:
  def __init__(self, blue, green, red):
    self.blue = blue
    self.green = green
    self.red = red

class Game:
  def __init__(self, number, draws):
    self.number = number
    self.draws = draws
  
  def is_valid(self, max_blue, max_green, max_red):
    for draw in self.draws:
      if draw.blue > max_blue or draw.green > max_green or draw.red > max_red:
        print("Game number " + str(self.number) + " is invalid!")
        return False
    print("Game number " + str(self.number) + " is valid!")
    return True
  
  def get_power(self):
    min_blue = 0
    min_green = 0
    min_red = 0

    for draw in self.draws:
      if draw.blue > 0 and draw.blue > min_blue:
        min_blue = draw.blue
      if draw.green > 0 and draw.green > min_green:
        min_green = draw.green
      if draw.red > 0 and draw.red > min_red:
        min_red = draw.red
      print("blue: " + str(min_blue))
      print("green: " + str(min_green))
      print("red: " + str(min_red))
      print("")
    
    return min_blue * min_green * min_red

def parse_games(lines):
  for line in lines:
    input_array = line.split(":")
    game_number = input_array[0].split(" ")[1]
    draws = []
    for draw in input_array[1].split(";"):
      blue=0
      red=0
      green=0
      for dice in draw.split(','):
        dice = dice.strip()
        number = int(dice.split(" ")[0])
        color = dice.split(" ")[1]

        if color == "blue":
          blue = number
        elif color == "green":
          green = number
        elif color == "red":
          red = number
      current_draw = Draw(blue, green, red)
      draws.append(current_draw)
    all_games.append(Game(int(game_number), draws))

def solve_part1(total_blue, total_green, total_red):
  valid_games = []
  for game in all_games:
    if game.is_valid(total_blue, total_green, total_red):
      valid_games.append(game)
  total_number = 0
  for game in valid_games:
    total_number += game.number
  
  print("Total Number: " + str(total_number))

def solve_part2():
  total_sum = 0
  for game in all_games:
    total_sum += game.get_power()
    print("Game " + str(game.number) + " Power: " + str(game.get_power()))

  print("Total Sum: " + str(total_sum))

parse_games(input_array)
#solve_part1(14,13,12)
solve_part2()