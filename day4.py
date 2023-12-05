## Parse file
my_file = open("inputs/day4.txt", "r")
content = my_file.read()
input_array = content.split("\n")

class Ticket:
  def __init__(self, card_number, winning_numbers, drawn_numbers):
    self.card_number = card_number
    self.winning_numbers = winning_numbers
    self.drawn_numbers = drawn_numbers

  def value(self):
    winners = 0
    for number in self.drawn_numbers:
      if number in self.winning_numbers:
        # print("Number: " + number + " is a winner!")
        winners += 1
    if winners == 0:
      return 0
    return pow(2,winners-1)
    



def generate_tickets(lines):
  tickets = []
  for line in lines:
    line_array = line.split(":")
    print(line_array[0])
    card_number = line_array[0].split(" ")[1]

    number_split = line_array[1].split("|")

    winning_numbers = []
    for number in number_split[0].strip().split(" "):
      if number == "":
        continue
      winning_numbers.append(int(number))

    drawn_numbers = []

    for number in number_split[1].strip().split(" "):
      if number == "":
        continue
      drawn_numbers.append(int(number))
    tickets.append(Ticket(card_number, winning_numbers, drawn_numbers))
  return tickets

all_tickets = generate_tickets(input_array)

total_value = 0
for ticket in all_tickets:
  total_value += ticket.value()

print("Total value: " + str(total_value))