import random

teams = []
sold = []
soldTo = []
soldPrice = []
soldNumber = []
balances = ["Balance"]
ledger = []
ledgerEntry = ["Teams"]
ledgerSpaces = []
propertyCount = ["Owned"]
propertyEntry = []
spentAmount = ["Spent"]
spentEntry = []
averageCost = ["Average"]
averageEntry= []
numTeams = 0
startBalance = 0

print("\nTeams")
print("======\n")

while True :
  try :
    numTeams = int(input("How many teams are playing: "))
    startBalance = int(input("\nHow much money is each team starting with: "))
    break
  except :
    print("\n\nTry again\n")

while numTeams > 0 :
  team = input("\nEnter team name: ")
  teams.append(team)
  ledgerEntry.append(team)
  ledgerSpaces.append(" ")
  spentAmount.append(0)
  propertyCount.append(0)
  averageCost.append(0)
  balances.append(startBalance)
  numTeams -= 1

ledger.append(tuple(ledgerEntry))
ledger.append(tuple(ledgerSpaces))
ledger.append(tuple(ledgerEntry))
ledger.append(tuple(spentAmount))
ledger.append(tuple(propertyCount))
ledger.append(tuple(averageCost))
ledger.append(tuple(balances))

ledgerEntry.clear()

input("\n\nGET READY FOR THE AUCTION ... PRESS ENTER TO START!")

properties = [
  "Old Kent Road",
  "Whitechapel Road",
  "Kings Cross Station",
  "The Angel, Islington",
  "Euston Road",
  "Pentonville Road", 
  "Pall Mall", 
  "Electric Company", 
  "Whitehall", 
  "Northumberland Avenue", 
  "Marylebone Station", 
  "Bow Street", 
  "Malborough Street", 
  "Vine Street", 
  "Strand",
  "Fleet Street",
  "Trafalgar Square",
  "Fenchurch Street Station",
  "Leicester Square",
  "Coventry Street",
  "Waterworks",
  "Picadilly",
  "Regent Street",
  "Oxford Street",
  "Bond Street",
  "Liverpool Street Station",
  "Park Lane",
  "Mayfair"
]


propertiesCopy = properties.copy()

i = 1
print("\n\n\n\n\n")

while len(properties) > 0 :
##  print(chr(27) + "[2J")
  input("\n\nPress enter to auction the next property ...")
  card = random.choice(properties)
  print("\n\n\n\n\n")

  for row in ledger :
    for column in row :
      print(str(column).rjust(5).ljust(10), end="")
    print("\n")
  print("\n\n\n")
  print("AUCTION NUMBER " + str(i))
  print("===+=============\n")
  i += 1
  for team in teams :
    print(str(teams.index(team)+1) + ") " + team)
  print("\n\n")
  while True :
    while True :
      try :
        winner = int(input("\nWhich team won the auction ?  "))
        if 1 <= winner <= len(teams) :
         break
      except :
        continue
    while True :
      try :
        price = int(input("\nHow much did they pay ? "))
        if 1 <= winner <= len(teams) :
          break
      except :
        continue
    check = input("\nYou entered (" + teams[winner-1] + ") and (" + str(price) + ")  - is this correct? Y/N :  ").capitalize()
    if check == "Y" :
      break
  sold.append(card)
  soldTo.append(teams[winner-1])
  soldPrice.append(price)
  soldNumber.append(propertiesCopy.index(card))
  balances[winner] -= price
  ledgerEntry = [0] * len(teams)
  ledgerEntry[winner-1] = price
  ledgerEntry.insert(0, "#" + str(29 - len(properties)))
  ledger.insert(len(ledger)-6, tuple(ledgerEntry))
  ledger[len(ledger)-1] = tuple(balances)
  propertyEntry = list(ledger[len(ledger)-3])
  propertyEntry[winner] += 1
  ledger[len(ledger)-3] = tuple(propertyEntry)
  spentEntry = list(ledger[len(ledger)-4])
  spentEntry[winner] += price
  ledger[len(ledger)-4] = tuple(spentEntry)
  averageEntry = list(ledger[len(ledger)-2])
  averageEntry[winner] = int(spentEntry[winner] / propertyEntry[winner])
  ledger[len(ledger)-2] = tuple(averageEntry)
  ledgerEntry.clear()
  spentEntry.clear()
  propertyEntry.clear()
  averageEntry.clear()
  properties.remove(card)


for row in ledger :
  for column in row :
    print(str(column).rjust(5).ljust(10), end="")
  print("\n")

input()

print(chr(27) + "[2J")
i = 200
while i > 0 :
  print("#### AUCTION COMPLETE - GET READY TO REVEAL RESULTS  ####")
  i -= 1
input("\n Press enter to reveal results ...")
print(chr(27) + "[2J")

for (index, card, team, price) in sorted(zip(soldNumber, sold, soldTo, soldPrice), key = lambda x: x[0]) :
  card = card.ljust(len(max(sold, key = len)))
  team = team.ljust(len(max(soldTo, key = len)))
  print(card + "   ====================>     " + team + "   ( " + str(price) +  " )")
  input()
