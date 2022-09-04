import random


properties = [
  "Old Kent Road",
  "Whitechapel Road",
  "The Angel, Islington",
  "Euston Road",
  "Pentonville Road",
  "Pall Mall",
  "Whitehall",
  "Northumberland Avenue",
  "Bow Street",
  "Malborough Street",
  "Vine Street",
  "Strand",
  "Fleet Street",
  "Trafalgar Square",
  "Leicester Square",
  "Coventry Street",
  "Picadilly",
  "Regent Street",
  "Oxford Street",
  "Bond Street",
  "Park Lane",
  "Mayfair",
  "Kings Cross Station",
  "Marylebone Station",
  "Fenchurch Street Station",
  "Liverpool Street Station",
  "Electric Company",
  "Waterworks"
]

flag = True

while flag :
  print(chr(27) + "[2J")
  input("Press enter to reveal property ...")
  card = random.choice(properties)
  print("\n\n\n\n\n")
  print(card)
  print("\n\n\n\n\n")
  input("Press enter to continue ...")
  properties.remove(card)
  if len(properties) < 1 :
    flag = False
