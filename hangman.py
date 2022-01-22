pics = ["  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========", 

        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========", 

        "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="] 



HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']



from calendar import c
import random
# from hangman_art import logo

logo = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/  
'''

print(logo)
print("Welcome to hangman.\n\nYou have 6 lifes\n")

lives = 7
pic = 0
# words = ["visibility"]#,"gravity","jiberish"]
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

chosen_word = list(random.choice(words))

print("solution: "," ".join(chosen_word))

already_guessed = []
chosen_word_ = []

for _ in range(len(chosen_word)):
    chosen_word_.append("_")
    
# print(chosen_word_)
print(" ".join(chosen_word_))

end_game = False

while not end_game:
    
    choice = input("\n\nGuess letter: ").lower()
    
    if choice.isalpha() and len(choice) == 1:

        if choice in already_guessed:
            print("already guessed")
            # if you want not to count same letters
            # continue
        else:
            already_guessed.append(choice)



        for (index, letter) in enumerate(chosen_word):
            if letter == choice:
                chosen_word_[index] = choice
                

        if choice not in chosen_word:
            print(pics[pic])
            pic += 1
            lives -= 1
            print(choice + " not in word\n")
            if lives == 0:
                end_game = True
                print("Game Over")
        
        if "_" not in chosen_word_:
            end_game = True
            print("You win")
            
        print("\n\n"," ".join(chosen_word_))
    else:
        print("try_gain_giving a letter!!!")

    

# print(" ".join(chosen_word_))
print("word is "," ".join(chosen_word))
    # [index for (index, letter) in enumerate(chosen_word) if letter == 'i']a