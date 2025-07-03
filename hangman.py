import random

import hangman_art

word_list= ["aadvark","baboon","camel"]

random_chose=random.choice(word_list)

print(hangman_art.logo)


placeholder= ""

for item in range(len(random_chose)):
    placeholder += "_"

print(f"Word to guess: {placeholder}")

lives = 6
game_over = False

correct_letters= []
guessed_letter = []

while not game_over :

    print(hangman_art.stages[lives])


    guess= input("Enter a letter:").lower()



    if guess in guessed_letter:
        print("you guess this letter before")

    guessed_letter.append(guess)


    display = ""

    for letter in random_chose:
        if letter == guess:
            display += letter
            correct_letters.append(guess)

        elif letter in correct_letters:
            display += letter

        else:
            display += "_"


    if guess not in random_chose:
        lives -= 1
        print("letter does not exist in the word")


    print(display ,"\n")
    print(f"remaining lives:{lives}")


    if "_" not in display:
        game_over = True

        print("YOU WİN \n CONGRATS! ")
    elif lives == 0:
        game_over= True
        print(f"YOU LOSE \n The word is: {random_chose}  \n GAME OVER     ")






