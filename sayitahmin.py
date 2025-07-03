import random

random_number = random.randint(1,100)
remaining_attempts = 5
score = 100
attempt_count=0
print("guess a number between 1 and 100")
print(f"Your starting score:{score} ")

while remaining_attempts>0 :
    guess= int(input("enter your guess:"))
    attempt_count +=1

    if guess<1 or guess>100:
        print("please enter a number between 1 and 100 !")
        continue

    if guess== random_number:
        print("Congrats, correct!!")
        print(f"your total score is {score}")
        break

    elif guess < random_number:
        print("try larger number.")

    else:
        print("try smaller number.")

    remaining_attempts -= 1
    score -= 10


    if remaining_attempts >0 :
        print(f"remaining attempts:{remaining_attempts}")
        print(f"current score:{score}\n")

    else:
        print("you failed")
        print(f"the number is:{random_number}")

