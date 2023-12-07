def empty_map():
    map = []
    for r in range(20):
        temp = []
        for c in range(20):
            temp.append("")
        map.append(temp)
    return map

def show_map():
    map_str = ""

    for i in range(20):
        # Draw the top border of the box
        map_str += "+----" * 20 + "+\n"

        # Draw the vertical borders of the box
        map_str += "|    " * 20 + "|\n"

    # Draw the bottom border of the last row
    map_str += "+----" * 20 + "+"
    print(map_str)

def print_menu():
    print("1. Build a building")
    print("2. See current score")
    print()
    print("3. Save game")
    print("4. Exit to main menu")

def turn_counter(map):
    temp2=0
    for r in map:
        temp = r.count("")
        temp2+=temp
    return(20*20-temp2)

while True:
    print("Welcome to Ngee Ann City!")
    print("{:-^28}".format(""))
    print("1. Start new game\n2.Load previous save\n3. Show high scores\n4. Exit game")
    
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
        map = empty_map()

    elif option == 2:
        a = 1
    
    elif option == 3:
        b = 1

    elif option == 4:
        print("Thanks for playing!")
        break

    turn = turn_counter(map)

    while turn<400:
        turn+=1

        while True:
            print("Turn {}".format(turn))
            show_map()
            print_menu()
            try:
                option = int(input("Please enter a choice: "))
            except:
                print("Error.. invalid input!! Try again!")
                continue

            if option not in range(5):
                print("Error.. invalid input!! Try again!")
                continue
            else:
                break

        if option == 4:
            break