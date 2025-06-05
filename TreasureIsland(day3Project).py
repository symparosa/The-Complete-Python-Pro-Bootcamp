print(r'''
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
              |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
''') 
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
want_to_go = input("\t Type 'left' or 'right' \n").lower()

if want_to_go == 'left':
    print("You've come to a lake. There is an island in the middle of the lake.")
    want_to_do = input("\t Type 'wait' to wait for a boat. Type 'swim' to swim across. \n").lower()
    
    if want_to_do =='wait':
        print("You arrive at the island unharmed. There is a house with 3 doors.\n One red, one yellow and one blue.")
        colour = input("\t Which colour do you choose? \n").lower()
        
        if colour=='Blue':
            print("Eaten by beasts.Game Over.")
        elif colour=='Yellow':
            print("You Win!")
        elif colour=='Red':
            print("Burned by fire.Game Over.")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout.Game Over.")
else:
    print("You fell into a hole. Game Over.")