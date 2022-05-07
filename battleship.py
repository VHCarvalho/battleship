#Game rules: https://www.cs.nmsu.edu/~bdu/TA/487/brules.htm

import random

print("Welcome to Battleship!")
print("This game was made with love by @VHCarvalho, send him some love via Instagram or Github")
bl = "-" * 20
print(bl)

#List of ships and the number of spaces each occupies
ships  = {"carrier": 5,
    "battleship": 4,
    "rcruiser": 3,
    "submarine": 3,
    "destroyer": 2 }

#The map to place our ships
map = [['0' for x in range(10)] for x in range(10)]

#Function to sort the ships on the map
def sort_ships(map):
    for ship in ships:
        while True:
            tested = 0
            first_spot = [random.randint(0,9), random.randint(0,9)]
            
            #randomizing the orientation of the ship: 
            # if 1 it will be vertical, else, horizontal
            orientation = random.randint(1,2)
            
            #check if the ship fits on the map
            if orientation == 1:
                if ships[ship] + first_spot[0] - 1 > 9:
                    continue

                #checking if there is already any ship on the way
                #if positive, sorting a first_spot again
                else:    
                    test_spot = []
                    for spot in range(len(first_spot)):
                        test_spot.append(first_spot[spot])
                    for y in range(ships[ship]):
                        if map[test_spot[0]][test_spot[1]] == '0':
                            test_spot[0] += 1
                            continue
                        else: 
                            tested = 1
                            break
                    if tested:
                        continue

                    #placing the ship
                    for x in range(ships[ship]):
                        map[first_spot[0]][first_spot[1]] = ship[0]
                        first_spot[0] += 1
            
            #check if the ship fits on the map
            else:
                if ships[ship] + first_spot[1] - 1 > 9:
                    continue

                #checking if there is already any ship on the way
                else:
                    test_spot = []
                    for spot in range(len(first_spot)):
                        test_spot.append(first_spot[spot])
                    for y in range(ships[ship]):
                        if map[test_spot[0]][test_spot[1]] == '0':
                            test_spot[1] += 1
                            continue
                        else: 
                            tested = 1
                            break
                    if tested:
                        continue
                    
                    #placing the ship
                    for x in range(ships[ship]):
                        map[first_spot[0]][first_spot[1]] = ship[0]
                        first_spot[1] += 1

            break       

#Function to set up the game, sorting the map and confirming if the player wants to play
def start_game():
    print("Let's start the game, shall we? [Y/N]")
    start = input(">>>")

    confirmation = ["y", "Y"]

    if not start in confirmation:
        print("Whenever you want! Bye!")
        quit()
    

    print("The ships will be sorted now, wait a sec...")
    
    sort_ships(map)

    print("Done!")

#Function to get the torpedo from the user
def get_torpedo():

    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    
    print("Where your torpedo will hit?")
    
    

    while True:
        
        user_coordinations = input(">>>")

        #Checking if the user is inputing on the right format
        if user_coordinations == 'map':
            for m in range(10):
                
                print(map[m])
        if len(user_coordinations) != 2:
        
            print("Usage: >>>A7")
        
        elif user_coordinations[0].upper() not in letters or user_coordinations[1].isdigit() == False:

            print("Usage: >>>A7")
        
        else:
            #All tested, send coordinations to check hit
            torpedo_coordinations = [letters.index(user_coordinations[0].upper()), int(user_coordinations[1])]
            
            return torpedo_coordinations

def check_hit(coordinations):

    row = coordinations[0]
    col = coordinations[1]

    if map[row][col] == '0':
    
        print("Water!")
    
        return False
    
    elif map[row][col] == 'x':
        print('Coordinates already shot, try another')
    
    else:
        print("Hit!")

        check_ship = map[row][col]

        map[row][col] = 'x'
        for a in range(10):
            
            found = 0
            
            for b in range(10):
                
                if check_ship in map[a][b]:
                    found = 1
                    break
            
            if found:
                break
        
        if not found:
            print("Ship down!")
        
        return True

def check_end(map):
    
    end = False

    initials = ['c', 'b', 'r', 's', 'd']
    found = 0
    for a in range(10):
        
        for b in range(10):

        
            if map[a][b] in initials:
                found = 1
                break
    
    if found:
        return end
    
    end = True
    return end

def main():
    
    start_game()

    print("Now I'll ask where you will want to send a torpedo.")
    print("To send a torpedo, when asked to, just use a letter (A-J) and a number (0-9) together")
    print("Example: B2")
    print(bl)

    end_game = False

    while end_game == False:
        torpedo = get_torpedo()

        hit = check_hit(torpedo)
        
        if hit:
            end_game = check_end(map)
    
    print("End of the game!")
    print('Thank you so much for playing this game!')
    print("Don't be shy and reach out for me at Instagram (@vhcarvalho) or Github (VHCarvalho)!")
    print("I'll love to hear your thoughts!")

if __name__ == '__main__':
    main()

