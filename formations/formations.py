#!/usr/bin/python3

import itertools
import random

dictionary = {"gk_dict" : {"file" : "goalkeepers.txt", "set" : set()}, "def_dict" : {"file" : "defenders.txt", "set" : set()}, "mid_dict" : {"file" : "midfielders.txt", "set" : set()}, "fwd_dict" : {"file" : "forwards.txt", "set" : set()}}

formations = ["334","343","352","424","433","442","451","523","532","541"]

def colourRed(text) :
  return ("\033[91m{}\033[00m" .format(text))

def colourGreen(text) :
  return ("\033[92m{}\033[00m" .format(text))

def colourCyan(text) :
  return ("\033[96m{}\033[00m" .format(text))

def colourYellow(text) :
  return ("\033[93m{}\033[00m" .format(text))

def makeBold(text) :
  return ("\033[1m{}\033[00m" .format(text))

def readFiles() :
  for sub in dictionary :
    try :
      file = open(dictionary[sub]["file"], "r")
      for line in file :
        if line.rstrip() != "" :
          dictionary[sub]["set"].add(line.rstrip())
    except FileNotFoundError :
      file = open(dictionary[sub]["file"], "w")
    finally :
      file.close()

def saveFiles() :
  for sub in dictionary :
    file = open(dictionary[sub]["file"], "w")
    for name in dictionary[sub]["set"] :
      file.write(name + "\n")
    file.close()

def displayMenu() :
  while True :
    print("\n\n")
    print(colourCyan("Welcome to Formations"))
    print(colourCyan("====================="))
    print("\n")
    print("1) Player Management")
    print("2) Team Selection")
    print("3) Save Changes")
    print("0) Exit")
    print("\n")
    try :
      selection = int(input(colourYellow("Select an option to continue [1-3] :  ")))
    except :
      print(chr(27) + "[2J")
      print(colourRed("Invalid selection - try again"))
      continue
    else :
      if 1 <= selection <= 3 :
        if selection == 1 :
          playerMgmtMenu()
        elif selection == 2 :
          teamSelection()
        elif selection == 3 :
          saveFiles()
      elif selection == 0 :
        break
      else :
        print(chr(27) + "[2J")
        print("Invalid selection - try again")

def playerMgmtMenu() :
  while True :
    print("\n\n")
    print(colourCyan("Player Management"))
    print(colourCyan("================="))
    print("\n")
    print("1) List Players")
    print("2) Add a Player")
    print("3) Remove a Player")
    print("0) Previous Menu")
    print("\n")
    try :
      selection = int(input(colourYellow("Select an option to continue [1-3] :  ")))
    except :
      print(chr(27) + "[2J")
      print(colourRed("Invalid selection - try again"))
      continue
    else :
      if 1 <= selection <= 3 :
        if selection == 1 :
          listPlayerMenu()
        elif selection == 2 :
          addPlayerMenu()
        elif selection == 3 :
          removePlayerMenu()
      elif selection == 0 :
        break
      else :
        print(chr(27) + "[2J")
        print(colourRed("Invalid selection - try again"))

def listPlayerMenu() :
  while True :
    print("\n\n")
    print(colourCyan("List Players"))
    print(colourCyan("============"))
    print("\n")
    print("1) Goalkeepers")
    print("2) Defenders")
    print("3) Midfielders")
    print("4) Forwards")
    print("0) Previous Menu")
    print("\n")
    try :
      selection = int(input(colourYellow("Select an option to continue [1-4] :  ")))
    except :
      print(chr(27) + "[2J")
      print(colourRed("Invalid selection - try again"))
      continue
    else :
      if 1 <= selection <= 4 :
        listPlayers(selection)
      elif selection == 0 :
        break
      else :
        print(chr(27) + "[2J")
        print(colourRed("Invalid selection - try again"))


def addPlayerMenu() :
  while True :
    print("\n\n")
    print(colourCyan("Add a Player"))
    print(colourCyan("============"))
    print("\n")
    print("1) Goalkeeper")
    print("2) Defender")
    print("3) Midfielder")
    print("4) Forward")
    print("0) Previous Menu")
    print("\n")
    try :
      selection = int(input(colourYellow("Select an option to continue [1-4] :  ")))
    except :
      print(chr(27) + "[2J")
      print(colourRed("Invalid selection - try again"))
      continue
    else :
      if 1 <= selection <= 4 :
        addPlayer(selection)
      elif selection == 0 :
        break
      else :
        print(chr(27) + "[2J")
        print(colourRed("Invalid selection - try again"))

def removePlayerMenu() :
  while True :
    print("\n\n")
    print(colourCyan("Remove a Player"))
    print(colourCyan("==============="))
    print("\n")
    print("1) Goalkeeper")
    print("2) Defender")
    print("3) Midfielder")
    print("4) Forward")
    print("0) Previous Menu")
    print("\n")
    try :
      selection = int(input(colourYellow("Select an option to continue [1-4] :  ")))
    except :
      print(chr(27) + "[2J")
      print(colourRed("Invalid selection - try again"))
      continue
    else :
      if 1 <= selection <= 4 :
        removePlayer(selection)
      elif selection == 0 :
        break
      else :
        print(chr(27) + "[2J")
        print(colourRed("Invalid selection - try again"))

def listPlayers(selected) :
  if selected == 1 :
    dict = "gk_dict"
  elif selected == 2 :
    dict = "def_dict"
  elif selected == 3 :
    dict = "mid_dict"
  elif selected == 4 :
    dict = "fwd_dict"
  players = []
  column1 = []
  column2 = []
  column3 = []
  column4 = []
  index = 1
  for name in dictionary[dict]["set"] :
    players.append(name)
  players = sorted(players)
  for name in players[0::4] :
    column1.append(str(index) + ". " + name)
    index += 1
  for name in players[1::4] :
    column2.append(str(index) + ". " + name)
    index += 1
  for name in players[2::4] :
    column3.append(str(index) + ". " + name)
    index += 1
  for name in players[3::4] :
    column4.append(str(index) + ". " + name)
    index += 1
  print("\n")
  for (a, b, c, d) in itertools.zip_longest(column1, column2, column3, column4) :
    if type(b) is not str and type(c) is not str and type(d) is not str :
      print(a.ljust(len(max(column1, key = len))))
    elif type(c) is not str and type(d) is not str :
      print(a.ljust(len(max(column1, key = len))) + "   " + b.ljust(len(max(column2, key = len))))
    elif type(d) is not str :
      print(a.ljust(len(max(column1, key = len))) + "   " + b.ljust(len(max(column2, key = len))) + "   " + c.ljust(len(max(column3, key = len))))
    else :
      print(a.ljust(len(max(column1, key = len))) + "   " + b.ljust(len(max(column2, key = len))) + "   " + c.ljust(len(max(column3, key = len))) + "   " + d.ljust(len(max(column4, key = len))))
  input(colourYellow("\nPress Enter to continue..."))

def addPlayer(selected) :
  if selected == 1 :
    dict = "gk_dict"
  elif selected == 2 :
    dict = "def_dict"
  elif selected == 3 :
    dict = "mid_dict"
  elif selected == 4 :
    dict = "fwd_dict"
  while True :
    try :
      player = str(input(colourYellow("\nUse CTRL+C to cancel\nEnter player's name:  ")))
    except KeyboardInterrupt :
      break
    if player.replace(" ","").isalpha() is True :
      if player in dictionary[dict]["set"] :
        print(colourRed("\nPlayer is already in the set - not added again"))
        input(colourYellow("\nPress Enter to continue..."))
      else :
        dictionary[dict]["set"].add(player)
        print(colourGreen("\nPlayer Added"))
        input(colourYellow("\nPress Enter to continue..."))
      break
    else :
      print(colourRed("\n\nInvalid characters used - only letters A-Z are accepted - Try again"))

def removePlayer(selected) :
  if selected == 1 :
    dict = "gk_dict"
  elif selected == 2 :
    dict = "def_dict"
  elif selected == 3 :
    dict = "mid_dict"
  elif selected == 4 :
    dict = "fwd_dict"
  while True :
    try :
      player = str(input(colourYellow("\nUse CTRL+C to cancel\nEnter player's name:  ")))
    except KeyboardInterrupt :
      break
    if player.replace(" ","").isalpha() is True :
      if player in dictionary[dict]["set"] :
        dictionary[dict]["set"].remove(player)
        print(colourGreen("\nPlayer Removed"))
        input(colourYellow("\nPress Enter to continue..."))
      else:
        print(colourRed("\nPlayer is not in the set therefore cannot be removed"))
        input(colourYellow("\nPress Enter to continue..."))
      break
    else :
      print(colourRed("\n\nInvalid characters used - only letters A-Z are accepted - Try again"))

def teamSelection() :
  formation = random.choice(formations)
  print("\nYou must select the following number of players ...")
  print("   " + colourGreen("1") + " first team goalkeepers")
  print("   " + colourGreen(formation[0]) + " first team defenders")
  print("   " + colourGreen(formation[1]) + " first team midfielders")
  print("   " + colourGreen(formation[2]) + " first team forwards")
  print("   " + colourRed("7") + " substitutes")
  num_gks = 4
  num_defs = 8
  num_mids = 8
  num_fwds = 8
  goalkeepers = randomSelect("gk_dict", num_gks)
  defenders = randomSelect("def_dict", num_defs)
  midfielders = randomSelect("mid_dict", num_mids)
  forwards = randomSelect("fwd_dict", num_fwds)
  goalkeepers.insert(0, "Goalkeepers")
  defenders.insert(0, "Defenders")
  midfielders.insert(0, "Midfielders")
  forwards.insert(0, "Forwards")
  global selectedCount
  selectedCount = 18
  selectedGks = prepSelection("(G) ", 1)
  selectedDefs = prepSelection("(D) ", int(formation[0]))
  selectedMids = prepSelection("(M) ", int(formation[1]))
  selectedFwds = prepSelection("(F) ", int(formation[2]))
  selectedSubs = prepSelection("(S) ", 7)
  while True :
    team = ["Selected"]
    team = team + selectedGks + selectedDefs + selectedMids + selectedFwds + selectedSubs
    print("\nYour formation is " + formation[0] + "-" + formation[1] + "-" + formation[2] + "\n")
    listSelection(goalkeepers, defenders, midfielders, forwards, team)
    input(colourYellow("\nPress Enter to continue..."))
    print("\n")
    print("1) Add First Team Goalkeeper     \t  9) Remove First Team Goalkeeper")
    print("2) Add First Team Defender       \t 10) Remove First Team Defender")
    print("3) Add First Team Midfielder     \t 11) Remove First Team Midfielder")
    print("4) Add First Team Forward        \t 12) Remove First Team Forward")
    print("5) Add Substitute Goalkeeper     \t 13) Remove Substitute Goalkeeper")
    print("6) Add Substitute Defender       \t 14) Remove Substitute Defender")
    print("7) Add Substitute Midfielder     \t 15) Remove Substitute Midfielder")
    print("8) Add Substitute Forward        \t 16) Remove Substitute Forward")
    print("0) Exit")
    print("\n")
    try :
      selection = int(input(colourYellow("Select an option to continue [1-16] :  ")))
    except :
      print(chr(27) + "[2J")
      print(colourRed("Invalid selection - try again"))
      continue
    else :
      if 1 <= selection <= 16 :
        if selection == 1 :
          print(makeBold("\nAvailable Players"))
          listPosition(goalkeepers)
          try :
            choice = int(input(colourYellow("Select a player to add :  ")))
          except :
            print(colourRed("\nInvalid selection"))
          else :
            if 1 <= choice <= num_gks :
              selectedGks = addSelection(True, goalkeepers, choice, selectedGks, selectedSubs)
            else :
              print(colourRed("\nInvalid selection"))
        elif selection == 2 :
          print(makeBold("\nAvailable Players"))
          listPosition(defenders)
          try :
            choice = int(input(colourYellow("Select a player to add :  ")))
          except :
            print(colourRed("\nInvalid selection"))
          else :
            if 1 <= choice <= num_defs :
              selectedDefs = addSelection(True, defenders, choice, selectedDefs, selectedSubs)
            else :
              print(colourRed("\nInvalid selection"))
        elif selection == 3 :
          print(makeBold("\nAvailable Players"))
          listPosition(midfielders)
          try :
            choice = int(input(colourYellow("Select a player to add :  ")))
          except :
            print(colourRed("\nInvalid selection"))
          else :
            if 1 <= choice <= num_mids :
              selectedMids = addSelection(True, midfielders, choice, selectedMids, selectedSubs)
            else :
              print(colourRed("\nInvalid selection"))
        elif selection == 4 :
          print(makeBold("\nAvailable Players"))
          listPosition(forwards)
          try :
            choice = int(input(colourYellow("Select a player to add :  ")))
          except :
            print(colourRed("\nInvalid selection"))
          else :
            if 1 <= choice <= num_fwds :
              selectedFwds = addSelection(True, forwards, choice, selectedFwds, selectedSubs)
            else :
              print(colourRed("\nInvalid selection"))
        elif selection == 5 :
          print(makeBold("\nAvailable Players"))
          listPosition(goalkeepers)
          try :
            choice = int(input(colourYellow("Select a player to add :  ")))
          except :
            print(colourRed("\nInvalid selection"))
          else :
            if 1 <= choice <= num_gks :
              selectedSubs = addSelection(False, goalkeepers, choice, selectedGks, selectedSubs)
            else :
              print(colourRed("\nInvalid selection"))
        elif selection == 6 :
          print(makeBold("\nAvailable Players"))
          listPosition(defenders)
          try :
            choice = int(input(colourYellow("Select a player to add :  ")))
          except :
            print(colourRed("\nInvalid selection"))
          else :
            if 1 <= choice <= num_defs :
              selectedSubs = addSelection(False, defenders, choice, selectedDefs, selectedSubs)
            else :
              print(colourRed("\nInvalid selection"))
        elif selection == 7 :
          print(makeBold("\nAvailable Players"))
          listPosition(midfielders)
          try :
            choice = int(input(colourYellow("Select a player to add :  ")))
          except :
            print(colourRed("\nInvalid selection"))
          else :
            if 1 <= choice <= num_mids :
              selectedSubs = addSelection(False, midfielders, choice, selectedMids, selectedSubs)
            else :
              print(colourRed("\nInvalid selection"))
        elif selection == 8 :
          print(makeBold("\nAvailable Players"))
          listPosition(forwards)
          try :
            choice = int(input(colourYellow("Select a player to add :  ")))
          except :
            print(colourRed("\nInvalid selection"))
          else :
            if 1 <= choice <= num_fwds :
              selectedSubs = addSelection(False, forwards, choice, selectedFwds, selectedSubs)
            else :
              print(colourRed("\nInvalid selection"))
        elif selection == 9 :
          print(makeBold("\nAvailable Players"))
          listPosition(goalkeepers)
          try :
            choice = int(input(colourYellow("Select a player to remove :  ")))
          except :
            print(colourRed("\nInvalid selection"))
          else :
            if 1 <= choice <= num_gks :
              selectedGks = removeSelection(goalkeepers, choice, selectedGks)
            else :
              print(colourRed("\nInvalid selection"))
        elif selection == 10 :
          print(makeBold("\nAvailable Players"))
          listPosition(defenders)
          try :
            choice = int(input(colourYellow("Select a player to remove :  ")))
          except :
            print(colourRed("\nInvalid selection"))
          else :
            if 1 <= choice <= num_defs :
              selectedDefs = removeSelection(defenders, choice, selectedDefs)
            else :
              print(colourRed("\nInvalid selection"))
        elif selection == 11 :
          print(makeBold("\nAvailable Players"))
          listPosition(midfielders)
          try :
            choice = int(input(colourYellow("Select a player to remove :  ")))
          except :
            print(colourRed("\nInvalid selection"))
          else :
            if 1 <= choice <= num_mids :
              selectedMids = removeSelection(midfielders, choice, selectedMids)
            else :
              print(colourRed("\nInvalid selection"))
        elif selection == 12 :
          print(makeBold("\nAvailable Players"))
          listPosition(forwards)
          try :
            choice = int(input(colourYellow("Select a player to remove :  ")))
          except :
            print(colourRed("\nInvalid selection"))
          else :
            if 1 <= choice <= num_fwds :
              selectedFwds = removeSelection(forwards, choice, selectedFwds)
            else :
              print(colourRed("\nInvalid selection"))
        elif selection == 13 :
          print(makeBold("\nAvailable Players"))
          listPosition(goalkeepers)
          try :
            choice = int(input(colourYellow("Select a player to add :  ")))
          except :
            print(colourRed("\nInvalid selection"))
          else :
            if 1 <= choice <= num_gks :
              selectedSubs = removeSelection(goalkeepers, choice, selectedSubs)
            else :
              print(colourRed("\nInvalid selection"))
        elif selection == 14 :
          print(makeBold("\nAvailable Players"))
          listPosition(defenders)
          try :
            choice = int(input(colourYellow("Select a player to add :  ")))
          except :
            print(colourRed("\nInvalid selection"))
          else :
            if 1 <= choice <= num_defs :
              selectedSubs = removeSelection(defenders, choice, selectedSubs)
            else :
              print(colourRed("\nInvalid selection"))
        elif selection == 15 :
          print(makeBold("\nAvailable Players"))
          listPosition(midfielders)
          try :
            choice = int(input(colourYellow("Select a player to add :  ")))
          except :
            print(colourRed("\nInvalid selection"))
          else :
            if 1 <= choice <= num_mids :
              selectedSubs = removeSelection(midfielders, choice, selectedSubs)
            else :
              print(colourRed("\nInvalid selection"))
        elif selection == 16 :
          print(makeBold("\nAvailable Players"))
          listPosition(forwards)
          try :
            choice = int(input(colourYellow("Select a player to add :  ")))
          except :
            print(colourRed("\nInvalid selection"))
          else :
            if 1 <= choice <= num_fwds :
              selectedSubs = removeSelection(forwards, choice, selectedSubs)
            else :
              print(colourRed("\nInvalid selection"))
      elif selection == 0 :
        break
      else :
        print("\nInvalid selection - try again")

def listPosition(position) :
  positionList = position.copy()
  positionList.pop(0)
  for name in positionList :
    print(name)

def prepSelection(prefix, quantity) :
  list = []
  i = 0
  while i < quantity :
    list.append(prefix)
    i += 1
  return list

def addSelection(firstTeam, position, selection, main, subs) :
  i = 0
  j = 0
  k = 0
  mainSlots = main.copy()
  subSlots = subs.copy()
  player = position[selection].split(") ")[1]
  for slot in mainSlots :
    if slot.split(") ")[1] == player :
      k += 1
  for slot in subSlots :
    if slot.split(") ")[1] == player :
      k += 1
  if firstTeam is True :
    slots = mainSlots
  else :
    slots = subSlots
  if k == 0 :
    for slot in slots :
      if slot.split(") ")[1].replace(" ","").isalpha() is not True :
        if firstTeam is True :
          main[j] = slot + player
        else :
          subs[j] = slot + player
        print(colourGreen("\nPlayer added successfully"))
        global selectedCount
        selectedCount -= 1
        i += 1
        break
      j += 1
    if i == 0 :
      print(colourRed("\nNo available spaces - remove a player from this position before trying to add more"))
  else :
    print(colourRed("\nPlayer is already selected"))
  if firstTeam is True :
    return main
  else :
   return subs

def removeSelection(position, selection, selected) :
  i = 0
  slots = selected.copy()
  player = position[selection].split(") ")[1]
  for slot in slots :
    if slot.split(") ")[1] == player :
      selected[i] = selected[i].replace(player,"")
      print(colourGreen("\nPlayer removed successfully"))
      global selectedCount
      selectedCount += 1
      break
    i += 1
  else :
    print(colourRed("\nPlayer is not part of selection - cannot be removed"))
  return selected

def listSelection(goalkeepers, defenders, midfielders, forwards, team) :
  i = 0
  for (a, b, c, d, e) in itertools.zip_longest(goalkeepers, defenders, midfielders, forwards, team) :
    if i == 0 :
      print(makeBold(a.ljust(len(max(goalkeepers, key = len))) + "   " + b.ljust(len(max(defenders, key = len))) + "   " + c.ljust(len(max(midfielders, key = len))) + "   " + d.ljust(len(max(forwards, key = len))) + "\t\t\t" + e.ljust(len(max(team, key = len)))))
    else :
      if type(a) is not str :
        a = ""
      if type(b) is not str :
        b = ""
      if type(c) is not str :
        c = ""
      if type(d) is not str :
        d = ""
      if type(e) is not str :
        e = ""
      a = a.ljust(len(max(goalkeepers, key = len)))
      b = b.ljust(len(max(defenders, key = len)))
      c = c.ljust(len(max(midfielders, key = len)))
      d = d.ljust(len(max(forwards, key = len)))
      print(colourSelection(a, team) + "   " + colourSelection(b, team) + "   " + colourSelection(c, team) + "   " + colourSelection(d, team) + "\t\t\t" + e)
    i += 1
  print("\nNumber of remaining positions: " + colourYellow(str(selectedCount)))

def colourSelection(player, selected) :
  team = selected.copy()
  first = []
  subs = []
  team.pop(0)
  for name in team :
    if name[1] == "S" :
      subs.append(name.split(") ")[1])
    else :
      first.append(name.split(") ")[1])
  if ")" in player :
   if player.split(") ")[1].rstrip() in first :
     return colourGreen(player)
   elif player.split(") ")[1].rstrip() in subs :
     return colourRed(player)
   else :
     return player
  else :
    return player

def randomSelect(dict, quantity) :
  allPlayers = []
  tempPlayers = []
  randomPlayers = []
  for name in dictionary[dict]["set"] :
    allPlayers.append(name)
  i = 0
  while i < quantity :
    player = random.choice(allPlayers)
    if player not in tempPlayers :
      tempPlayers.append(player)
      i += 1
  tempPlayers = sorted(tempPlayers)
  n = 1
  for player in tempPlayers :
    randomPlayers.append(str(n) + ") " + player)
    n += 1
  return randomPlayers

readFiles()
displayMenu()
