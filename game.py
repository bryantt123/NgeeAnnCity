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
            start_turn(coins, turn)

        elif option == 2:
            a = 1
        
        elif option == 3:
            b = 1

        elif option == 4:
            print("Thanks for playing!")
            break

def start_turn(coins, turn):
    buildings = ['R', 'I', 'C', 'O', '*']
    while True:
        turn += 1
        randNo1 = random.randint(0,4)
        randNo2 = random.randint(0,4)
        if coins == 0:
            print("You have ran out of coins! Game over...")
            return
        while True:
            show_map()
            print("Turn: {:<5} Coins: {:<5}".format(str(turn), str(coins)))
            print_menu()
            try:
                option = int(input("Please enter a choice: "))
            except:
                print("Error.. invalid input!! Try again!")
                continue

            if option not in range(2):
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
                    buildChoice = input("Choose a building to build! Your choices: {} or {} ".format(buildings[randNo1], buildings[randNo2])).upper()
                except:
                    print("Error.. invalid input!! Try again!")
                    continue

                if buildChoice not in buildings:
                    print("Error.. invalid input!! Try again!")
                    continue
                else:
                    coins -= 1
                    build(turn, buildChoice)
                    break
        
        elif option == 2:
            print("to be continued")
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
            column = int(position[1:])
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
                    column = int(position[1:])
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




game_start()