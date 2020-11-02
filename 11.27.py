#Martinez_Omat_psid#1484888
def getJerseyNumber():
    jerseyNumber = int(input("Enter new player's jersey number:"))
    while (jerseyNumber < 0 or jerseyNumber > 99):
        jerseyNumber = int(input("Error! Enter new player's jersey number:"))
    return jerseyNumber

def getRating():
    rating = int(input("Enter player's rating:"))
    while (rating < 1 or rating > 9):
        rating = int(input("Error! Enter player's rating:"))
    return rating

def menu():
    print("MENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")
    choice = input("Choose an option: ")
    return choice[0]

def printRoster(player):
    print("ROSTER")
    for jersey in sorted(player):
        print("Jersey number: ", jersey,", Rating:", player[jersey])

def addPlayer(player):
    jerseyNumber = getJerseyNumber()
    rating = getRating()
    player[jerseyNumber] = rating

def deletePlayer(player):
    jerseyNumber = getJerseyNumber()
    if jerseyNumber in player:
        player.pop(jerseyNumber)
    else:
        print("Jersey number not found.")

def updatePlayer(player):
    jerseyNumber = getJerseyNumber()  # get jersey number
    if jerseyNumber in player:  # if jersey number exits in dictionary
        rating = getRating()  # get rating
        player[jerseyNumber] = rating
    else:
        print("Jersey number not found.")


def outputRatingPlayer(player):
    rating = getRating()  # get rating
    print("ABOVE", rating)
    for jersey in sorted(player):  # dictionary in sorted order
        if (player[jersey] > rating):
            print("Jersey number: ", jersey, ", Rating:", player[jersey])


def getPlayerInput(player):
    i = 0
    while i < 5:
        print("Enter player",(i+1),"'s jersey number:", end='\n')
        jerseyNumber = int(input())
        while (jerseyNumber < 0 or jerseyNumber > 99):
            print('\n')
            print("Error! Enter player",(i+1),"'s jersey number:", end='\n')
            jerseyNumber = int(input())
            print('\n')
        print("Enter player",(i+1),"'s rating:", end='\n')
        rating = int(input())
        while (rating < 1 or rating > 9):
            print()
            print("Error! Enter player",(i+1),"'s rating:", end='\n')
            rating = int(input())
        player[jerseyNumber] = rating
        i += 1

if __name__ == "__main__":
    player = {}
    getPlayerInput(player)
    printRoster(player)
    while True:
        choice = menu()
        if choice == 'a':
            addPlayer(player)
        elif choice == 'd':
            deletePlayer(player)
        elif choice == 'u':
            updatePlayer(player)
        elif choice == 'r':
            outputRatingPlayer(player)
        elif choice == 'o':
            printRoster(player)
        elif choice == 'q':
            break
            print("")
            break
        else:
            print("Invalid choice.")
