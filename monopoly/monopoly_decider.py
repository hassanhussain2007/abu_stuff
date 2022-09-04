import random
import time

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

players = [
  "A",
  "N",
  "H",
  "Z",
  "U"
]

selections = {}

flag = True

copyProperties = properties.copy()

while flag :
  card = random.choice(properties)
  owner = random.choice(players)
  selections[card] = owner
  properties.remove(card)
  print(chr(27) + "[2J")
  sortedSelections = sorted(selections.items(), key=lambda x: x[1], reverse=False)
  for deed in sortedSelections :
    print(deed[0].ljust(len(max(copyProperties, key=len))) + "\t(" + str(selections[deed[0]]) + ")")
  print("\n")
  time.sleep(1)
  if len(properties) < 1 :
    flag = False
