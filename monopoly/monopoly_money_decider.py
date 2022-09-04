import random
import time

games = {"200" : 0, "250" : 0, "1100" : 0, "1500" : 0, "2500" : 0, "5000" : 0}

flag1 = True
nap = 0.05
pop_this = ""

while flag1 :
  flag2 = True
  gamesList = []
  weightsList = []
  for game in games :
    games[game] = 0
    gamesList.append(game)
    weightsList.append(0)
  while flag2 :
    tempList = []
    selection = random.choices(gamesList, weights = weightsList, k = 1)[0]
    weightsList.clear()
    games[selection] += 1
    print(chr(27) + "[2J")
    sortedGames = sorted(games.items(), key=lambda x: x[1], reverse=False)
    for game in sortedGames :
      print(game[0].ljust(len(max(gamesList, key=len))) + "\t(" + str(games[game[0]]) + ") \t" + "#" * games[game[0]])
      tempList.append(game[0])
    print("\n")
    sortedGames = sorted(games.items(), key=lambda x: x[1], reverse=True)
    for game in sortedGames :
      weightsList.append(games[game[0]])
    gamesList = tempList.copy()
    time.sleep(nap)
    for game in games :
      if games[game] >= 100 :
        pop_this = min(games, key=games.get)
        flag2 = False
        nap += 0.005
    if flag2 == False :
      games.pop(pop_this)
  if len(games) < 2 :
    flag1 = False
    print("\n\nThe winning game is ... " + next(iter(games.items()))[0])

