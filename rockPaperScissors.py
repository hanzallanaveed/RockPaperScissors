import random

rock = '''
rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
choose_RPS = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))
if choose_RPS == 0:
    print(rock)
if choose_RPS == 1:
    print(paper)
if choose_RPS == 2:
    print(scissors)

print("The computer chose:")
computer_chooses = random.randint(0, 2)
if computer_chooses == 0:
    print(rock)
if computer_chooses == 1:
    print(paper)
if computer_chooses == 2:
    print(scissors)

if choose_RPS == 0 and computer_chooses == 0:
    print("Draw")
if choose_RPS == 1 and computer_chooses == 1:
    print("Draw")
if choose_RPS == 2 and computer_chooses == 2:
    print("Draw")

if choose_RPS == 0 and computer_chooses == 1:
    print("You Lost")
if choose_RPS == 1 and computer_chooses == 2:
    print("You Lost")
if choose_RPS == 2 and computer_chooses == 0:
    print("You Lost")

if choose_RPS == 0 and computer_chooses == 2:
    print("You Win")
if choose_RPS == 1 and computer_chooses == 0:
    print("You Win")
if choose_RPS == 2 and computer_chooses == 1:
    print("You Win")