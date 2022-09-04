# import libraries
from prettytable import PrettyTable
import random
import copy

# define team class
class Team:
  def __init__(self, teamName, balance):
    self.name = teamName
    self.remainingBalance = balance
    self.totalSpend = 0
    self.propertiesOwned = 0
    self.averageSpend = 0
    self.predictedProfitLoss = 0
    self.averageBidForAll = int(balance/auctionCounter)
    self.averageBidForShare = int(float(balance/auctionCounter) * numberOfTeams)
    self.auctionHistory = [[]]
    self.hits_set_0 = 0
    self.hits_set_1 = 0
    self.hits_set_2 = 0
    self.hits_set_3 = 0
    self.hits_set_4 = 0
    self.hits_set_5 = 0
    self.hits_set_6 = 0
    self.hits_set_7 = 0
    self.hits_set_8 = 0
    self.hits_set_9 = 0
    self.hits_set_99 = 0
    self.prob_set_0 = "0%"
    self.prob_set_1 = "0%"
    self.prob_set_2 = "0%"
    self.prob_set_3 = "0%"
    self.prob_set_4 = "0%"
    self.prob_set_5 = "0%"
    self.prob_set_6 = "0%"
    self.prob_set_7 = "0%"
    self.prob_set_8 = "0%"
    self.prob_set_9 = "0%"
    self.prob_set_99 = "0%"
    self.prob_set_any = "0%"

# define property class
class Property:
  def __init__(self, propertyName, propertyGroup, propertyTag, propertyPrice):
    self.name = propertyName
    self.group = propertyGroup
    self.tag = propertyTag
    self.listPrice = propertyPrice
    self.owner = ""
    self.state = "Not Auctioned"
    self.soldPrice = 0
    self.profitLoss = 0

# define main variables
teamCounter = 0
numberOfTeams = 0
startBalance = 0
wildcardMode = False
wildcardCount = 0
teamsList = []
propertiesList = []
auctionList = []
auctionCounter = 28
auctionLimit = 28
fraudList = []
fraudCounter = 0
fraudNotOwnedList = []
fraudNotOwnedFlag = False
thisAuctionList = []
auctionNumber = 1
averageAuctionPrice = 0
cumulativeAuctionPrice = 0
tableHeadings = []
currentOptions = []
combinationResults = []
wildcardAllocPref1 = [7,6,5,4,3,2,1,0,8,9]
wildcardAllocPref2 = [9,8,0,1,2,3,4,5,6,7]

# define properties master list
propertiesMaster = [
  ["Old Kent Road", 0, "B1", 60],
  ["Whitechapel Road", 0, "B2", 60],
  ["Kings Cross Station", 8, "T1", 200],
  ["The Angel, Islington", 1, "LB1", 100],
  ["Euston Road", 1, "LB2", 100],
  ["Pentonville Road", 1, "LB3", 120],
  ["Pall Mall", 2, "P1", 140],
  ["Electric Company", 9, "U1", 150],
  ["Whitehall", 2, "P2", 140],
  ["Northumberland Avenue", 2, "P3", 160],
  ["Marylebone Station", 8, "T2", 200],
  ["Bow Street", 3, "O1", 180],
  ["Malborough Street", 3, "O2", 180],
  ["Vine Street", 3, "O3", 200],
  ["Strand", 4, "R1", 220],
  ["Fleet Street", 4, "R2", 220],
  ["Trafalgar Square", 4, "R3", 240],
  ["Fenchurch Street Station", 8, "T3", 200],
  ["Leicester Square", 5, "Y1", 260],
  ["Coventry Street", 5, "Y2", 260],
  ["Waterworks", 9, "U2", 150],
  ["Picadilly", 5, "Y3", 280],
  ["Regent Street", 6, "G1", 300],
  ["Oxford Street", 6, "G2", 300],
  ["Bond Street", 6, "G3", 320],
  ["Liverpool Street Station", 8, "T4", 200],
  ["Park Lane", 7, "DB1", 350],
  ["Mayfair", 7, "DB2", 400]
]

# define set list for probability calculations
setlist = [
  ["B1", "B2"],
  ["LB1","LB2","LB3"],
  ["P1","P2","P3"],
  ["O1","O2","O3"],
  ["R1","R2","R3"],
  ["Y1","Y2","Y3"],
  ["G1","G2","G3"],
  ["DB1","DB2"],
  ["T1","T2","T3", "T4"],
  ["U1","U2"]
]

# define probability calculation function
def calculateProbabilities(prev, currauc):
  prev1 = copy.deepcopy(prev)
  prev2 = copy.deepcopy(prev)
  prev3 = copy.deepcopy(prev)
  for i in range(int(len(prev))):
    prev1[i] += [currauc[0]]
  for i in range(int(len(prev))):
    prev2[i] += [currauc[1]]
  for i in range(int(len(prev))):
    prev3[i] += [currauc[2]]
  prev = prev1 + prev2 + prev3
  nrcombs = 0
  setchances = 0
  newcomblist = []
  for comblist in prev:
    if len(comblist) == len(set(comblist)):
      newcomblist.append(comblist)
      nrcombs +=1
  for newcombs in newcomblist:
    for sets in setlist:
      if set(sets).issubset(set(newcombs)):
        setchances +=1
        break
  totprob = "{:.0%}".format(setchances/nrcombs)
  probs = []
  for sets in setlist:
    setchances = 0
    for newcombs in newcomblist:
      if set(sets).issubset(set(newcombs)):
        setchances +=1
    probs.append("{:.0%}".format(setchances/nrcombs))
  return newcomblist, probs, totprob

# prep finance row function
def prepareFinanceRow(rowNumber, list) :
  row = []
  if rowNumber == 0 :
    row.append("Properties Owned")
    for team in list :
      row.append(team.propertiesOwned)
    return row
  if rowNumber == 1 :
    row.append("Total Spend")
    for team in list :
      row.append(team.totalSpend)
    return row
  if rowNumber == 2 :
    row.append("Average Spend")
    for team in list :
      row.append(team.averageSpend)
    return row
  if rowNumber == 3 :
    row.append("Predicted Profit/Loss")
    for team in list :
      row.append(team.predictedProfitLoss)
    return row
  if rowNumber == 4 :
    row.append("Average Bid (For All)")
    for team in list :
      row.append(team.averageBidForAll)
    return row
  if rowNumber == 5 :
    row.append("Average Bid (For Share)")
    for team in list :
      row.append(team.averageBidForShare)
    return row
  if rowNumber == 6 :
    row.append("Remaining Balance")
    for team in list :
      row.append(team.remainingBalance)
    return row

# prep sets row function
def prepareSetsRow(rowNumber, list) :
  row = []
  if rowNumber == 0 :
    row.append("Browns")
    for team in list :
      row.append(str(team.hits_set_0) + " / " + str(team.prob_set_0))
    return row
  if rowNumber == 1 :
    row.append("Light Blues")
    for team in list :
      row.append(str(team.hits_set_1) + " / " + str(team.prob_set_1))
    return row
  if rowNumber == 2 :
    row.append("Pinks")
    for team in list :
      row.append(str(team.hits_set_2) + " / " + str(team.prob_set_2))
    return row
  if rowNumber == 3 :
    row.append("Oranges")
    for team in list :
      row.append(str(team.hits_set_3) + " / " + str(team.prob_set_3))
    return row
  if rowNumber == 4 :
    row.append("Reds")
    for team in list :
      row.append(str(team.hits_set_4) + " / " + str(team.prob_set_4))
    return row
  if rowNumber == 5 :
    row.append("Yellows")
    for team in list :
      row.append(str(team.hits_set_5) + " / " + str(team.prob_set_5))
    return row
  if rowNumber == 6 :
    row.append("Greens")
    for team in list :
      row.append(str(team.hits_set_6) + " / " + str(team.prob_set_6))
    return row
  if rowNumber == 7 :
    row.append("Dark Blues")
    for team in list :
      row.append(str(team.hits_set_7) + " / " + str(team.prob_set_7))
    return row
  if rowNumber == 8 :
    row.append("Train Stations")
    for team in list :
      row.append(str(team.hits_set_8) + " / " + str(team.prob_set_8))
    return row
  if rowNumber == 9 :
    row.append("Utilities")
    for team in list :
      row.append(str(team.hits_set_9) + " / " + str(team.prob_set_9))
    return row
  if rowNumber == 10 :
    row.append("Any Set")
    for team in list :
      row.append(str(team.prob_set_any))
    return row

# prep ledger row function
def prepareLedgerRow(round, winner, teams, amount) :
  row = []
  row.append("Auction Number " + str(round))
  for team in teams :
    if teams.index(team) == winner :
      row.append(amount)
    else :
      row.append(0)
  return row

# input game parameters
while True :
  try :
    numberOfTeams = int(input("How many teams are playing: "))
    startBalance = int(input("\nHow much money is each team starting with: "))
    wildcardModeInput = input("\nTurn on Wildcard Mode? (Y/N)  ").capitalize()
    while True :
      if wildcardModeInput == "Y" :
        wildcardMode = True
        break
      elif check == "N" :
        break
    break
  except :
    print("\n\nTry again\n")

# create teams
while teamCounter < numberOfTeams :
  teamName = input("\nEnter name of team " + str(teamCounter + 1) + ": ")
  teamsList.append(Team(teamName, startBalance))
  teamCounter += 1

# create properties
for property in propertiesMaster :
  propertiesList.append(Property(property[0],property[1],property[2],property[3]))

# create tables
ledgerTable = PrettyTable()
setsTable = PrettyTable()
financesTable = PrettyTable()
resultsTable = PrettyTable()

for team in teamsList :
  tableHeadings.append(team.name)
tableHeadings.insert(0, " ".ljust(24))

ledgerTable.field_names = tableHeadings.copy()
setsTable.field_names = tableHeadings.copy()
financesTable.field_names = tableHeadings.copy()
resultsTable.field_names = ["          Property        ", "State", "List Price", "Sold Price", "Profit/Loss", "Owner"]

ledgerTable.align = "r"
setsTable.align = "r"
financesTable.align = "r"
resultsTable.align["Property"] = "r"

# prepare auction
input("\n\nGET READY FOR THE AUCTION ... PRESS ENTER TO START!")
auctionList = propertiesMaster.copy()
fraudList = propertiesMaster.copy()
print("\n" * 3)

wildcardDebug = "NO WILDCARD"

# prepare wildcard mode
if wildcardMode :
  wildcardCount = random.randint(4,6)
  fraudList.append(["Wildcard", 99, "WC", 0])
  fraudList.append(["Wildcard", 99, "WC", 0])
  fraudList.append(["Wildcard", 99, "WC", 0])
  fraudList.append(["Wildcard", 99, "WC", 0])
  fraudList.append(["Wildcard", 99, "WC", 0])
  while wildcardCount > 0 :
    wildcardTag = "WC" + str(wildcardCount)
    fraudList.append(["Wildcard", 99, "WC", 0])
    fraudList.append(["Wildcard", 99, "WC", 0])
    auctionList.append(["Wildcard", 99, wildcardTag, 0])
    propertiesList.insert(0, Property("Wildcard", 99, wildcardTag, 0))
    wildcardCount -= 1

# start auction
while auctionLimit > 0 :
  thisAuctionList.clear()
  currentOptions.clear()
  combinationResults.clear()
  setsTable.clear_rows()
  financesTable.clear_rows()
  averageAuctionPrice = 0
  cumulativeAuctionPrice = 0
  fraudCounter = 0
  fraudNotOwnedList.clear()
  fraudNotOwnedFlag = False
  for i in range(11) :
    setsTable.add_row(prepareSetsRow(i, teamsList))
  for i in range(7) :
    financesTable.add_row(prepareFinanceRow(i, teamsList))
  print(ledgerTable)
  input("\n\nPress enter to auction the next property ...")
  print(setsTable)
  print("\n")
  print(financesTable)
#  print(wildcardDebug)
  card = random.choice(auctionList)
  thisAuctionList.append(card)
  while fraudCounter < 2 :
    fraud = random.choice(fraudList)
#    if fraud not in thisAuctionList :
    if fraud[0] not in list(map(lambda x: x[0], thisAuctionList)) :
      thisAuctionList.append(fraud)
      for property in propertiesList :
        if (property.name == fraud[0]) and (property.owner == "") :
          fraudNotOwnedList.append(fraud)
          fraudNotOwnedFlag = True
          break
      fraudCounter += 1
  for x in range(321) :
    random.shuffle(thisAuctionList)
  print("\n" * 3)
  print("AUCTION NUMBER " + str(auctionNumber))
  print("=================\n")
  print("This auction is for one of the following properties:")
  for item in thisAuctionList :
    print(str(thisAuctionList.index(item)+1) + ") " + item[0])
    cumulativeAuctionPrice += item[3]
    currentOptions.append(item[2])
  averageAuctionPrice = int(cumulativeAuctionPrice / len(thisAuctionList))
  print("\nThe average price of the properties listed above is:  " + str(averageAuctionPrice))
  print("\n")
  for team in teamsList :
    print(str(teamsList.index(team)+1) + ") " + team.name)
  flag = True
  while flag :
    while True :
      try :
        winner = int(input("\nWhich team won the auction ?  "))
        if 1 <= winner <= len(teamsList) :
         break
      except :
        continue
    while True :
      try :
        price = int(input("\nHow much did they pay ? "))
        break
      except :
        continue
    while True :
      try :
        check = input("\nYou entered (" + teamsList[winner-1].name + ") and (" + str(price) + ")  - is this correct? Y/N :  ").capitalize()
        if check == "Y" :
          flag = False
          break
        elif check == "N" :
          break
      except :
        continue
  print("\n")
  for property in propertiesList :
    if property.tag == card[2] :
      property.owner = teamsList[winner-1].name
      property.state = "Auctioned"
      property.soldPrice = price
      property.profitLoss = property.listPrice - price
      if property.group != 99 :
        auctionLimit -= 1
  for team in teamsList :
    if team.name == teamsList[winner-1].name :
      team.propertiesOwned += 1
      team.remainingBalance -= price
      team.totalSpend += price
      team.averageSpend = int(team.totalSpend / team.propertiesOwned)
      team.predictedProfitLoss += (averageAuctionPrice - price)
      combinationResults = list(calculateProbabilities(team.auctionHistory, currentOptions))
      team.auctionHistory = combinationResults[0]
      for item in thisAuctionList :
        code = "team.hits_set_" + str(item[1]) + " += 1"
        exec(code)
      for entry in combinationResults[1] :
        code = "team.prob_set_" + str(combinationResults[1].index(entry)) + " = entry"
        exec(code)
      team.prob_set_any = combinationResults[2]
    if auctionCounter > 1 :
      team.averageBidForAll = int(team.remainingBalance / (auctionCounter - 1))
      team.averageBidForShare = int(team.remainingBalance / (auctionCounter - 1) * len(teamsList))
  wildcardDebug = "NO WILDCARD"
  if (wildcardMode) and (card[1] == 99):
    ownedGroups = []
    shortList = []
    dilutedGroups = []
    dilutedList = []
    priorityList = []
    for property in propertiesList :
      if (property.owner == teamsList[winner-1].name) and (property.group != 99) :
        ownedGroups.append(property.group)
    ownedGroups = sorted(ownedGroups, reverse=True)
    ownedGroups = list(dict.fromkeys(ownedGroups))
    for group in ownedGroups :
      for property in propertiesList :
        if (property.group == group) and (property.owner != teamsList[winner-1].name) :
          shortList.append(property)
    for property in shortList :
      if property.owner != "" :
        dilutedGroups.append(property.group)
    dilutedGroups = sorted(dilutedGroups, reverse=True)
    dilutedGroups = list(dict.fromkeys(dilutedGroups))
    for property in shortList :
      if property.group not in dilutedGroups :
        priorityList.append(property)
      elif (property.group in dilutedGroups) and (property.owner == "") :
        dilutedList.append(property)
    if len(priorityList) > 0 :
      wildcardDebug = "WILDCARD OPTION 1"
      flag = False
      for group in wildcardAllocPref1 :
        for bonusCard in priorityList :
          if bonusCard.group == group :
            for property in propertiesList :
              if property.name == bonusCard.name :
                property.owner = teamsList[winner-1].name
                property.state = "WC Option 1"
                property.soldPrice = 0
                property.profitLoss = property.listPrice - property.soldPrice
                auctionLimit -= 1
                for item in auctionList :
                  if item[0] == bonusCard.name :
                    auctionList.remove(item)
                    break
                flag = True
                break
          if flag :
            break
        if flag :
          break
    elif len(dilutedList) > 0 :
      wildcardDebug = "WILDCARD OPTION 2"
      flag = False
      for group in wildcardAllocPref1 :
        for bonusCard in dilutedList :
          if bonusCard.group == group :
            for property in propertiesList :
              if property.name == bonusCard.name :
                property.owner = teamsList[winner-1].name
                property.state = "WC Option 2"
                property.soldPrice = 0
                property.profitLoss = property.listPrice - property.soldPrice
                auctionLimit -= 1
                for item in auctionList :
                  if item[0] == bonusCard.name :
                    auctionList.remove(item)
                    break
                flag = True
                break
          if flag :
            break
        if flag :
          break
    elif fraudNotOwnedFlag :
      wildcardDebug = "WILDCARD OPTION 3"
      for bonusCard in fraudNotOwnedList :
        for property in propertiesList :
          if property.name == bonusCard[0] :
            property.owner = teamsList[winner-1].name
            property.state = "WC Option 3"
            property.soldPrice = (int(price/len(fraudNotOwnedList)) * -1)
            property.profitLoss = 0
            auctionLimit -= 1
            for item in auctionList :
              if item[0] == bonusCard[0] :
                auctionList.remove(item)
                break
    else :
      wildcardDebug = "WILDCARD OPTION 4"
      flag = False
      if not flag :
        for group in wildcardAllocPref2 :
          for bonusCard in auctionList :
            if (bonusCard[1] == group) :
              for property in propertiesList :
                if property.name == bonusCard[0] :
                  property.owner = teamsList[winner-1].name
                  property.state = "WC Option 4"
                  property.soldPrice = 0
                  property.profitLoss = property.listPrice - property.soldPrice
                  auctionLimit -= 1
                  for item in auctionList :
                    if item[0] == bonusCard[0] :
                      auctionList.remove(item)
                      break
                  flag = True
                  break
            if flag :
              break
          if flag :
            break
  ledgerTable.add_row(prepareLedgerRow(auctionNumber, winner-1, teamsList, price))
  auctionList.remove(card)
  auctionCounter -= 1
  auctionNumber += 1

print(setsTable)
print("\n")
print(financesTable)
input("\n")
print(chr(27) + "[2J")
for x in range(200) :
  print("#### AUCTION COMPLETE - GET READY TO REVEAL RESULTS  ####")
input("\n Press enter to reveal results ...")
print(chr(27) + "[2J")

for property in propertiesList :
  print(resultsTable)
  resultsTable.add_row([property.name, property.state, property.listPrice, property.soldPrice, property.profitLoss, " ? "])
  input()
  print(chr(27) + "[2J")
  print(resultsTable)
  resultsTable.del_row(propertiesList.index(property))
  resultsTable.add_row([property.name, property.state, property.listPrice, property.soldPrice, property.profitLoss, property.owner])
  input()
  print(chr(27) + "[2J")

print(resultsTable)
