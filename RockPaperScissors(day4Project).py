import random

Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper = ''' 
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

Scissors = '''   
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [Rock, Paper, Scissors]

choose_op = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n "))

if 0 <= choose_op <= 2:
    print(f"You chose: \n {options[choose_op]}")
    
    random_choose = random.randint(0,2)
    print(f"Computer chose: \n {options[random_choose]}")
    
    if choose_op == random_choose:
        print("It's a draw!")
    elif choose_op == 0:
        if random_choose == 1:
            print("You lose!")
        elif random_choose == 2:
            print("You win!")
    elif choose_op == 1:
        if random_choose == 0:
            print("You win!")
        elif random_choose == 2:
            print("You lose!")
    elif choose_op == 2:
        if random_choose == 0:
            print("You lose!")
        elif random_choose == 1:
            print("You win!")
else:
    print("Invalid option")