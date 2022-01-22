import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]


while True:

    user_choice = int(input("Τί διαλέγεις? Πάτα \n 0: πέτρα\n 1: χαρτί\n 2: ψαλίδι.\n==> "))
    if user_choice >= 3 or user_choice < 0: 
        print("Έδωσες λάθος νούμερο, έχασες!") 
    else:
        print(game_images[user_choice])

        computer_choice = random.randint(0, 2)
        print("ο Υπολογιστής διάλεξε:")
        print(game_images[computer_choice])

        if user_choice == 0 and computer_choice == 2:
            print("ΚΕΡΔΙΣΕΣ!\n")
        elif computer_choice == 0 and user_choice == 2:
            print("ΕΧΑΣΕΣ\n")
        elif computer_choice > user_choice:
            print("ΕΧΑΣΕΣ\n")
        elif user_choice > computer_choice:
            print("ΚΕΡΔΙΣΕΣ!\n")
        elif computer_choice == user_choice:
            print("ΙΣΟΠΑΛΛΙΑ\n")
