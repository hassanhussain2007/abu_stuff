import random

teams = []
sold = []
soldTo = []
soldPrice = []
soldNumber = []
saleList = []
salePriceList = []
saleAverage = 0
balances = ["Balance"]
ledger = []
ledgerEntry = ["Teams"]
ledgerSpaces = []
propertyCount = ["Owned"]
propertyEntry = []
spentAmount = ["Spent"]
spentEntry = []
averageCost = ["Average Spend"]
averageEntry= []
predictedPL = ["Predicted P/L"]
predictedPLEntry= []
averageBid = ["Average Bid"]
averageBidEntry= []
averageBidFixed = ["Average Bid (S)"]
averageBidFixedEntry= []
numTeams = 0
startBalance = 0

br_record = ["Browns"]
lb_record = ["Light Blues"]
pi_record = ["Pinks"]
or_record = ["Oranges"]
re_record = ["Reds "]
ye_record = ["Yellows"]
gr_record = ["Greens"]
bl_record = ["Blues"]
tr_record = ["Trains"]
ut_record = ["Utilities"]

br_entry = []
lb_entry = []
pi_entry = []
or_entry = []
re_entry = []
ye_entry = []
gr_entry = []
bl_entry = []
tr_entry = []
ut_entry = []

br_flag = 0
lb_flag = 0
pi_flag = 0
or_flag = 0
re_flag = 0
ye_flag = 0
gr_flag = 0
bl_flag = 0
tr_flag = 0
ut_flag = 0

print("\nTeams")
print("======\n")

while True :
  try :
    numTeams = int(input("How many teams are playing: "))
    startBalance = int(input("\nHow much money is each team starting with: "))
    break
  except :
    print("\n\nTry again\n")


n = 0

while n < numTeams :
  team = input("\nEnter team name: ")
  teams.append(team)
  ledgerEntry.append(team)
  ledgerSpaces.append(" ")
  spentAmount.append(0)
  propertyCount.append(0)
  averageCost.append(0)
  predictedPL.append(0)
  averageBid.append(int(startBalance/28))
  averageBidFixed.append(int(float(startBalance/28) * numTeams))
  balances.append(startBalance)
  br_record.append(0)
  lb_record.append(0)
  pi_record.append(0)
  or_record.append(0)
  re_record.append(0)
  ye_record.append(0)
  gr_record.append(0)
  bl_record.append(0)
  tr_record.append(0)
  ut_record.append(0)
  n += 1

ledger.append(tuple(ledgerEntry))
ledger.append(tuple(ledgerSpaces))
ledger.append(tuple(ledgerEntry))
ledger.append(tuple(br_record))
ledger.append(tuple(lb_record))
ledger.append(tuple(pi_record))
ledger.append(tuple(or_record))
ledger.append(tuple(re_record))
ledger.append(tuple(ye_record))
ledger.append(tuple(gr_record))
ledger.append(tuple(bl_record))
ledger.append(tuple(tr_record))
ledger.append(tuple(ut_record))
ledger.append(tuple(ledgerSpaces))
ledger.append(tuple(ledgerEntry))
ledger.append(tuple(spentAmount))
ledger.append(tuple(propertyCount))
ledger.append(tuple(averageCost))
ledger.append(tuple(predictedPL))
ledger.append(tuple(averageBid))
ledger.append(tuple(averageBidFixed))
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

prices = [
60,
60,
200,
100,
100,
120,
140,
150,
140,
160,
200,
180,
180,
200,
220,
220,
240,
200,
260,
260,
150,
280,
300,
300,
320,
200,
350,
400
]

propertyFlags = [
  "br_flag",
  "br_flag",
  "tr_flag",
  "lb_flag",
  "lb_flag",
  "lb_flag", 
  "pi_flag", 
  "ut_flag", 
  "pi_flag", 
  "pi_flag", 
  "tr_flag", 
  "or_flag", 
  "or_flag", 
  "or_flag", 
  "re_flag",
  "re_flag",
  "re_flag",
  "tr_flag",
  "ye_flag",
  "ye_flag",
  "ut_flag",
  "ye_flag",
  "gr_flag",
  "gr_flag",
  "gr_flag",
  "tr_flag",
  "bl_flag",
  "bl_flag"
]


i = 1
print("\n\n\n\n\n")

while len(properties) > 0 :
##  print(chr(27) + "[2J")
  input("\n\nPress enter to auction the next property ...")
  saleList.clear()
  card = random.choice(properties)
  saleList.append(card)
  f = 0
  while f < 2 :
    fraud = random.choice(propertiesCopy)
    if fraud not in saleList:
      saleList.append(fraud)
      f += 1
  for x in range(200):
    random.shuffle(saleList)
  for item in saleList :
    salePriceList.append(prices[propertiesCopy.index(item)])
    locals()[propertyFlags[propertiesCopy.index(item)]] += 1
  print("\n\n\n\n\n")

  for row in ledger :
    for column in row :
      print(str(column).rjust(5).ljust(20), end="")
    print("\r")
  print("\n\n\n")
  print("AUCTION NUMBER " + str(i))
  print("=================\n")
  print("This auction is for one of the following properties:")
  for item in saleList :
    print(str(saleList.index(item)+1) + ") " + item)
  i += 1
  saleAverage = int(sum(salePriceList) / len(saleList))
  print("\nThe average price of the properties listed above is:  " + str(saleAverage))
  print("\n")
  for team in teams :
    print(str(teams.index(team)+1) + ") " + team)
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
  ledger.insert(len(ledger)-21, tuple(ledgerEntry))
  ledger[len(ledger)-1] = tuple(balances)
  propertyEntry = list(ledger[len(ledger)-6])
  propertyEntry[winner] += 1
  ledger[len(ledger)-6] = tuple(propertyEntry)
  spentEntry = list(ledger[len(ledger)-7])
  spentEntry[winner] += price
  ledger[len(ledger)-7] = tuple(spentEntry)
  averageEntry = list(ledger[len(ledger)-5])
  averageEntry[winner] = int(spentEntry[winner] / propertyEntry[winner])
  ledger[len(ledger)-5] = tuple(averageEntry)
  predictedPLEntry = list(ledger[len(ledger)-4])
  predictedPLEntry[winner] += (saleAverage - price)
  ledger[len(ledger)-4] = tuple(predictedPLEntry)
  averageBidEntry = list(ledger[len(ledger)-3])
  for entry in averageBidEntry :
    if averageBidEntry.index(entry) == 0 :
      pass
    else :
      if len(properties) > 1 :
        averageBidEntry[averageBidEntry.index(entry)] = int(balances[averageBidEntry.index(entry)] / (len(properties) - 1))
      else :
        averageBidEntry[averageBidEntry.index(entry)] = int(balances[averageBidEntry.index(entry)])
  ledger[len(ledger)-3] = tuple(averageBidEntry)
  averageBidFixedEntry = list(ledger[len(ledger)-2])
  for entry in averageBidFixedEntry :
    if averageBidFixedEntry.index(entry) == 0 :
      pass
    else :
      if len(properties) > 1 :
        averageBidFixedEntry[averageBidFixedEntry.index(entry)] = int(float(balances[averageBidFixedEntry.index(entry)] / (len(properties) - 1)) * len(teams))
      else :
        averageBidFixedEntry[averageBidFixedEntry.index(entry)] = int(float(balances[averageBidFixedEntry.index(entry)]))
  ledger[len(ledger)-2] = tuple(averageBidFixedEntry)
  br_entry = list(ledger[len(ledger)-19])
  lb_entry = list(ledger[len(ledger)-18])
  pi_entry = list(ledger[len(ledger)-17])
  or_entry = list(ledger[len(ledger)-16])
  re_entry = list(ledger[len(ledger)-15])
  ye_entry = list(ledger[len(ledger)-14])
  gr_entry = list(ledger[len(ledger)-13])
  bl_entry = list(ledger[len(ledger)-12])
  tr_entry = list(ledger[len(ledger)-11])
  ut_entry = list(ledger[len(ledger)-10])
  if br_flag > 0 :
    br_entry[winner] += br_flag
  if lb_flag > 0 :
    lb_entry[winner] += lb_flag
  if pi_flag > 0 :
    pi_entry[winner] += pi_flag
  if or_flag > 0 :
    or_entry[winner] += or_flag
  if re_flag > 0 :
    re_entry[winner] += re_flag
  if ye_flag > 0 :
    ye_entry[winner] += ye_flag
  if gr_flag > 0 :
    gr_entry[winner] += gr_flag
  if bl_flag > 0 :
    bl_entry[winner] += bl_flag
  if tr_flag > 0 :
    tr_entry[winner] += tr_flag
  if ut_flag > 0 :
    ut_entry[winner] += ut_flag
  ledger[len(ledger)-19] = tuple(br_entry)
  ledger[len(ledger)-18] = tuple(lb_entry)
  ledger[len(ledger)-17] = tuple(pi_entry)
  ledger[len(ledger)-16] = tuple(or_entry)
  ledger[len(ledger)-15] = tuple(re_entry)
  ledger[len(ledger)-14] = tuple(ye_entry)
  ledger[len(ledger)-13] = tuple(gr_entry)
  ledger[len(ledger)-12] = tuple(bl_entry)
  ledger[len(ledger)-11] = tuple(tr_entry)
  ledger[len(ledger)-10] = tuple(ut_entry)
  br_entry.clear()
  lb_entry.clear()
  pi_entry.clear()
  or_entry.clear()
  re_entry.clear()
  ye_entry.clear()
  gr_entry.clear()
  bl_entry.clear()
  tr_entry.clear()
  ut_entry.clear()
  ledgerEntry.clear()
  spentEntry.clear()
  propertyEntry.clear()
  averageEntry.clear()
  averageBidEntry.clear()
  averageBidFixedEntry.clear()
  salePriceList.clear()
  br_flag = 0
  lb_flag = 0
  pi_flag = 0
  or_flag = 0
  re_flag = 0
  ye_flag = 0
  gr_flag = 0
  bl_flag = 0
  tr_flag = 0
  ut_flag = 0
  properties.remove(card)


for row in ledger :
  for column in row :
    print(str(column).rjust(5).ljust(20), end="")
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
