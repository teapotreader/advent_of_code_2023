# issue: we need the first and last digit of a string which can contain more than 2 digits. If there is only 1 digit, then the digit will need to be multiple (i.e. 7 turns to 77).


#import data
data = open("input_day_1_1.txt", "r")

# loop totdat er geen regels meer zijn
# loop totdat er geen characters meer zijn
# check of een character een getal is

def parse_line(string):
  first_digit = 0
  last_digit = 0
  for char in string:
    if char.isdigit():
      if first_digit == 0:
        first_digit = char
      last_digit = char

  digits = int(first_digit + last_digit)
  return digits

list = []
for line in data:
  list.append(parse_line(line))

print(sum(list))
