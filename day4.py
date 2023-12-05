## Parse file
import time
my_file = open("inputs/day4.txt", "r")
content = my_file.read()
input_array = content.split("\n")

count = 0

class Ticket:
  value = 0
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
    
  def get_number_of_winners(self):
    winners = 0
    for number in self.drawn_numbers:
      if number in self.winning_numbers:
        winners += 1
    return winners
  
  def set_value(self, value):
    self.value = value



def generate_tickets(lines):
  tickets = []
  for line in lines:
    line_array = line.split(":")
    card_number_array = line_array[0].split(" ")
    card_number = int(card_number_array[len(card_number_array)-1])

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

## Part 2

cards_map = {}


for ticket in all_tickets:
  cards_map.update({ticket.card_number: ticket})

ticket_list = []
for ticket in all_tickets:
  ticket_list.append(ticket)

for ticket in ticket_list:
  print("Ticket: " + str(ticket.card_number) + " has " + str(ticket.get_number_of_winners()) + " winners")

# Find all tickets with no winners, set value = 1
# Find all tickets with 1 winner, set value = 1 + value of one below
# etc.
count = 0
total_overall_count = 0
def get_total_winners(ticket, total_winners):
  # print("Ticket number: " + str(ticket.card_number))
  global count
  count+=1

  winners = ticket.get_number_of_winners()
  # print("Winners: " + str(winners))
  if winners == 0:
    return 0
  
  for i in range(ticket.card_number + 1, ticket.card_number + winners + 1):
    # print("Getting ticket number: " + str(i))
    get_total_winners(cards_map.get(i), total_winners)

  return total_winners
total_winners = 0
for ticket in ticket_list:
  total_winners += get_total_winners(ticket, 0)
  # time.sleep(1000)
  print("Ticket number: " + str(ticket.card_number))
  print("Total Count: " + str(count))
# print("Total Winning Tickets: " + str(total_winners))
print("Count: " + str(count))