#SDD Assignment 1

import random

map = [[[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]],
         [[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]],
         [[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]],
         [[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]],
         [[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]],
         [[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]],
         [[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]],
         [[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]],
         [[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]],
         [[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]],
         [[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]],
         [[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]],
         [[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]],
         [[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]],
         [[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]],
         [[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]],
         [[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]],
         [[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]],
         [[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]],
         [[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]]
    ]

rowLetters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T']

def show_map():
    borders = "+-----"
    end = "+"
    rows = len(map)
    columns = len(map[0])
    for i in range(0, 19):
        print("{:>6}".format(i+1), end="")
    print("{:>6}".format("20"))
    print()
    
    print("  ",end="")
    for i in range(columns):
        print(borders,end="")
    print(end)
    
    for i in range(rows):
        print(rowLetters[i],end="")
        print(" ",end="")

        for j in map[i]:
            print("|",end="")
            if j[0] == None:
                print("{:^5}".format(""),end="")
            else:
                print("{:^5}".format(str(j[0])),end="")
        print("|")
        print("  ",end="")

        for j in map[i]:
            print("|",end="")
            if j[1] == None:
                print("{:^5}".format(""),end="")
            else:
                print("{:2}/{:2}".format(j[1],j[2]),end="")
        print("|")

        print("  ",end="")  #To leave a space in the column that has a letter
        
        for i in range(columns):
            print(borders,end="")
        print(end)

def print_menu():
    print("1. Build a building")
    print("2. Save game")
    print("0. Exit to main menu")

def game_start():
    coins = 16
    turn = 0
    score = 0
    while True:
        print("Welcome to Ngee Ann City!")
        print("{:-^28}".format(""))
        print("1. Start new game\n2. Load previous save\n3. Show high scores\n4. Exit game")
        
        try:
            option = int(input("Please enter your choice: "))
        except:
            print()
            print("Error.. invalid input!! Try again!")
            continue
        print()
        if option not in range(5):
            print("Error.. invalid input!! Try again!")
            continue

        if option == 1:
            start_turn(coins, turn, score)

        elif option == 2:
            turn, score, coins = loadGame()
            turn -= 1
            start_turn(coins, turn, score)
            print("Previous save has been loaded succesfully!")
        
        elif option == 3:
            displayLeaderboard()
            continue

        elif option == 4:
            print("Thanks for playing!")
            break

def start_turn(coins, turn, score):
    buildings = ['R', 'I', 'C', 'O', '*']
    while True:
        turn += 1
        randNo1 = random.randint(0,4)
        randNo2 = random.randint(0,4)
        if coins == 0:
            print("You have ran out of coins! Game over...")
            if checkLeaderboard(score) == True:
                print("Impressive! Your score has reached the leaderboard!")
                name = input("Enter your username in the leaderboard: ")
                updateLeaderboard(name, score)
            return
        elif buildingCount(map) == 400:
            print("You have successfully populated Ngee Ann City! The game has ended :)")
            if checkLeaderboard(score) == True:
                print("Impressive! Your score has reached the leaderboard!")
                name = input("Enter your username in the leaderboard: ")
                updateLeaderboard(name, score)
            return
        while True:
            show_map()
            print("Turn: {:<5} Coins: {:<5} Score: {:<5}".format(str(turn), str(coins), str(score)))
            print_menu()
            try:
                option = int(input("Please enter a choice: "))
            except:
                print("Error.. invalid input!! Try again!")
                continue

            if option not in range(3):
                print("Error.. invalid input!! Try again!")
                continue
            else:
                break

        if option == 0:
            print("Exiting to main menu..")
            return
        
        elif option == 1:
            while True:
                try:
                    buildChoice = input("Choose a building to build! Your choices: {} or {}. \nYour Choice: ".format(buildings[randNo1], buildings[randNo2])).upper()
                except:
                    print("Error.. invalid input!! Try again!")
                    continue

                if buildChoice not in buildings:
                    print("Error.. invalid input!! Try again!")
                    continue
                else:
                    coins -= 1
                    building, row, column = build(turn, buildChoice)
                    scoreAddition, coinsAddition = calcScore(building, row, column)
                    score += scoreAddition
                    coins += coinsAddition
                    break
        
        elif option == 2:
            saveGame(turn, score, coins)
            print("Game progress has been saved succesfully!")
            continue


def build(turn, building):
    buildings = ['R', 'I', 'C', 'O', '*']
    while True: # validation step
        try:
            position = input("Enter a position to place your building: ")
        except:
            print("Error.. invalid input!! Try again!")
            continue

        if not len(position) in [2,3] or not position[0].isalpha() or not position[1:].isdigit(): # check if position input is valid
            print("Error.. invalid position!! Enter another position!")
            continue

        else:
            column = int(position[1:]) - 1
            row = ord(position[0].upper()) - ord('A')
            if map[row][column][0] in buildings:
                print("Error.. position already taken!! Enter another position!")
                continue
            else:
                break

    if turn == 1:
        map[row][column][0] = building
        return building, row, column
    
    else:
        if checkPosition(row, column) == True:
            map[row][column][0] = building
            return building, row, column
        
        else:
            while True:
                print("Error.. invalid position!! Enter another position!")
                try:
                    position = input("Enter a position to place your building: ")
                except:
                    print("Error.. invalid input!! Try again!")
                    continue

                if not len(position) in [2,3] or not position[0].isalpha() or not position[1:].isdigit(): # check if position input is valid
                    print("Error.. invalid position!! Enter another position!")
                    continue
                else:
                    column = int(position[1:]) - 1
                    row = ord(position[0].upper()) - ord('A')
                    if checkPosition(row, column) == False:
                        print("Error.. invalid position!! Enter another position!")
                        continue
                    else:
                        break

            map[row][column][0] = building
            return building, row, column

def checkPosition(row, column):
    # for corners, check if there is a building adjacent to specified position
    if row == 0 and column == 0:
        if map[row+1][column][0] != None or map[row][column+1][0] != None:
            return True
        return False
    
    if row == 0 and column == 19:
        if map[row][column-1][0] != None or map[row+1][column][0] != None:
            return True
        return False
    
    if row == 19 and column == 0:
        if map[row][column+1][0] != None or map[row-1][column][0] != None:
            return True
        return False

    if row == 19 and column == 19:
        if map[row][column-1][0] != None or map[row-1][column][0] != None:
            return True
        return False
    
    # for first and last rows, check if there is a building on either side or below specified position
    if row == 0:
        if map[row][column+1][0] != None or map[row][column-1][0] != None or map[row+1][column][0] != None:
            return True
        return False
    
    if row == 19:
        if map[row][column+1][0] != None or map[row][column-1][0] != None or map[row-1][column][0] != None:
            return True
        return False
    
    # for first and last columns, check if there is a building on either side or above/below the specified position
    if column == 0:
        if map[row+1][column][0] != None or map[row-1][column][0] != None or map[row][column+1][0] != None:
            return True
        return False

    if column == 0:
        if map[row+1][column][0] != None or map[row-1][column][0] != None or map[row][column-1][0]:
            return True
        return False
    # for other position, checks if there is a building on any side of the specified position
    if map[row][column-1][0] != None or map[row][column+1][0] != None or map[row-1][column][0] != None or map[row+1][column][0] != None:
        return True
    return False

def calcScore(building, row, col):
    scoreAddition = 0
    coinsAddition = 0
    indices_to_check = [
            (row, col-1), (row, col+1),
            (row-1, col), (row+1, col),
            (row-1, col-1), (row-1, col+1),
            (row+1, col-1), (row+1, col+1)
        ]
    if building == "R":
        temp = ["R","C"]
        
        # Residential next to industry(I)
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for dr, dc in directions:
            try:
                if map[row + dr][col + dc][0] == "I":
                    scoreAddition += 1
            except:
                pass
        # Residential adjacent to Residential(R) or Commercial(C)
        for i, j in indices_to_check:
            try:
                if map[i][j][0] in temp:
                    scoreAddition += 1
                if map[i][j][0] == "C":
                    coinsAddition += 1
            except:
                pass
        # Residential(R) adjacent to Park(O)
        for i, j in indices_to_check:
            try:
                if map[i][j][0] == "O":
                    scoreAddition += 2
            except:
                pass
    
    if building == "I":
        scoreAddition += 1
        # Industry(I) adjacent to Residential(R)
        for i, j in indices_to_check:
            try:
                if map[i][j][0] == "R":
                    coinsAddition += 1
                    scoreAddition += 1
            except:
                pass
            
    if building == "C":
        # Commercial(C) adjacent to Commercial(C)
        for i, j in indices_to_check:
            try:
                if map[i][j][0] == "C":
                    scoreAddition += 1
            except:
                pass
        # Commercial (C) adjacent to Residential(R)
        for i, j in indices_to_check:
            try:
                if map[i][j][0] == "R":
                    coinsAddition += 1
                    scoreAddition += 1
            except:
                pass

    if building == "O":
        # Park(O) adjacent to Park(O)
        for i, j in indices_to_check:
            try:
                if map[i][j][0] == "O":
                    scoreAddition += 1
            except:
                pass
        # Park(O) adjacent to Residential(R)
        for i, j in indices_to_check:
            try:
                if map[i][j][0] == "R":
                    scoreAddition += 2
            except:
                pass
    
    if building == "*":
        if map[row][col-1][0] == "*":
            scoreAddition += 1
        if map[row][col+1][0] == "*":
            scoreAddition += 1
            
    return scoreAddition, coinsAddition

def buildingCount(map):
    flat_list = [item for sublist1 in map for sublist2 in sublist1 for item in sublist2]

    # Count the number of non-types (in this case, None elements)
    count_non_types = sum(1 for element in flat_list if element is not None)
    return count_non_types

def loadGame():
    datafile = open("GameSave.txt", "r")
    lines = datafile.readlines()
    playerSettings = lines[0].split(",")
    savedMap = lines[1:]
    
    turn = int(playerSettings[0])
    score = int(playerSettings[1])
    coins = int(playerSettings[2])

    for i in range (len(savedMap)):
        temp = savedMap[i].split("-")
        for j in range(len(temp)):
            if temp[j].strip("\n") == "[None, None]" or temp[j].strip("\n") == "[None, None, None]":
                map[i][j] = [None, None]
            else:
                unit = temp[j].strip("\n").strip("[").strip("]").split(",")
                map[i][j] = [unit[0].strip("'"), None, None]

    return turn, score, coins

def saveGame(turn, score, coins):
    saved_list = []
    saved_list.append(turn)
    saved_list.append(score)
    saved_list.append(coins)
    
    datafile = open("GameSave.txt", "w")
    for h in saved_list:
        datafile.write("{},".format(h))
    datafile.write("\n")
    
    for i in map:
        row = []
        for j in i:
            row.append(str(j))
        datafile.writelines("-".join(row))
        datafile.write("\n")
        
    datafile.close()

def displayLeaderboard():
    datafile = open("Leaderboard.txt", "r")
    lines = datafile.readlines()
    newList = []
    for line in lines:
        newList.append(line.strip())
    print("\n")
    y = 1
    print("LEADERBOARD\n")
    for x in range (0, len(newList), 2):
        print(str(y) + ". " + newList[x] + ": " + newList[x + 1])
        y += 1
    datafile.close()

def checkLeaderboard(score):
    name = ""

    file = open("Leaderboard.txt", "r")
    f = file.readlines()
    file.close()
    emptyFile = False

    if len(f) == 0:
        emptyFile = True

    newList = []
    for line in f:
        newList.append(line.strip())

    scoreList = []
    for x in range(1, len(newList), 2):
            scoreList.append(int(newList[x]))
        
    if len(newList) == 20:
        if scoreList[9] > score:
            return False
        for index in range(0, len(scoreList), 1):
            if scoreList[index] < score:
                newList.pop(19)
                newList.pop(18)
                newList.insert(index * 2, name)
                newList.insert(index * 2 + 1, score)
                break
            elif scoreList[index] == score:
                if scoreList[9] == score:
                    return False
                else:
                    newList.pop(19)
                    newList.pop(18)
                    newList.insert(index * 2, name)
                    newList.insert(index *2 + 1, score)
                    break
            
    else:
        for index in range(0, len(scoreList), 1):
            if scoreList[index] <= score:
                newList.insert(index * 2, name)
                newList.insert(index * 2 + 1, score)
                break
            if index == len(scoreList):
                return False

    return True

def updateLeaderboard(name, score):
    file = open("Leaderboard.txt", "r")
    f = file.readlines()
    file.close()
    emptyFile = False

    if len(f) == 0:
        emptyFile = True

    newList = []
    for line in f:
        newList.append(line.strip())

    scoreList = []
    for x in range(1, len(newList), 2):
            scoreList.append(int(newList[x]))
        
    if len(newList) == 20:
        if scoreList[9] > score:
            return False
        for index in range(0, len(scoreList), 1):
            if scoreList[index] < score:
                newList.pop(19)
                newList.pop(18)
                newList.insert(index * 2, name)
                newList.insert(index * 2 + 1, score)
                break
            elif scoreList[index] == score:
                if scoreList[9] == score:
                    return False
                else:
                    newList.pop(19)
                    newList.pop(18)
                    newList.insert(index * 2, name)
                    newList.insert(index *2 + 1, score)
                    break
            
    else:
        for index in range(0, len(scoreList), 1):
            if scoreList[index] <= score:
                newList.insert(index * 2, name)
                newList.insert(index * 2 + 1, score)
                break
            if index == len(scoreList):
                return False
            
    with open("Leaderboard.txt", "w") as file:
        if emptyFile == True:
            file.write(name + "\n" + str(score) + "\n")
        else:
            for value in newList:
                file.write(str(value) + "\n")
    file.close()
    return True


game_start()