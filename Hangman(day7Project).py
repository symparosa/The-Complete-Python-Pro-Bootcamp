import random

hangman_stages = [
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ======
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    ======
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    ======
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    ======
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    ======
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    ======
    """,
    """
     +---+
     |   |
         |
         |
         |
         |
    ======
    """
]

live = 6

print(live)

list = ["praia", "fogo", "sofia", "casa", "ovos"]

random_word = random.choice(list)

print(random_word)

space = ""

for position in range(len(random_word)):
    space += "-"

print(space)

complete = False
correct_letter = []

while complete == 0:
    
    display = ""
    
    guess = input("Guess a letter: ").lower()

    for letter in random_word:
        if letter == guess:
            display += letter
            correct_letter.append(letter)
        elif letter in correct_letter:
            display += letter
        else:
            display += '_'
            
    print(display)
    
    if guess not in random_word:
        live -= 1
        if(live == 0):
            complete = True
            print("You lose!")
        
    if "_" not in display:
        print("You win!")
        complete = True
        
    
    print(hangman_stages[live])


