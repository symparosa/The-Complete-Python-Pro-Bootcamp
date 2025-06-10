from art import the_higher_lower, the_vs_logo
from gameData import famous_people
from os import system, name
from random import choices

print(the_higher_lower)

SCORE = 0
GAME_OVER = False

def clear():
  system('cls' if name == 'nt' else 'clear')

def random_selection():
    """A function to return a random selection of famous people"""
    
    list_a = choices(famous_people)
    list_b = choices(famous_people)

    diferent = False

    while diferent is False:
        if list_a == list_b:
            list_b = choices(famous_people)
        else:
            diferent = True
            
    return {"op_a":list_a[0], "op_b":list_b[0]}


def compare_options(op1,op2):
    """A function to compare the number of followers between two random famous people"""
    
    if op1["follower"] > op2["follower"]:
        return True
    elif op1["follower"] == op2["follower"]:
        return True
    else:
        return False

def higher_lower_game():
    """A function to play the higher lower game"""
    
    global SCORE, GAME_OVER, op_a, op_b

    print(f"Compare A: {op_a["name"]}, a {op_a["description"]}, from {op_a["country"]}.")
    print(the_vs_logo)
    print(f"Against B: {op_b["name"]}, a {op_b["description"]}, from {op_b["country"]}.")

    type = input("Who has more followers? Type 'A' or 'B': ").lower()

    if type in ('a','b'):
        
        if type == 'a':
            win = compare_options(op_a,op_b)
        else:
            win = compare_options(op_b,op_a)
        
        if win:
            SCORE +=1
            clear()
            print(the_higher_lower)
            print(f"You're right! Current score: {SCORE}.")
            op_a = op_b
            op_b = random_selection()["op_b"]
        else:
            GAME_OVER = True
            clear()
            print(the_higher_lower)
            print(f"Sorry, that's wrong. Final score: {SCORE}.")
        
    else:
        GAME_OVER = True
        clear()
        print(the_higher_lower)
        print(f"There no option {type}, just 'A' or 'B'.")

def play():
    while GAME_OVER is False:
        higher_lower_game()

op_a = random_selection()["op_a"]
op_b = random_selection()["op_b"]   
play()
    
