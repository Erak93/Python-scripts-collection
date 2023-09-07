import random
from logo import logo

print(logo)

difficulty_level=""
random_number=random.randint(1,101)

# test random number
# print(random_number)



def pick_difficulty():
    difficulty_level_choice=input("Choose a difficulty level.Type easy or hard. ")
    if difficulty_level_choice=="easy":
        return 10
    elif difficulty_level_choice=="hard":
        return 5
    else:
        print("Invalid command")


difficulty_level=pick_difficulty()
#test setting the difficulty level
#print (difficulty_level)

game_is_over=False

while game_is_over==False:
    guess=int(input("Guess a number between 1 and 100:\n"))
    
    if guess<random_number:
        print(f"Your guess is too low.")
    elif guess>random_number:
        print("Your guess is too high")
    elif guess==random_number:
        print(f'You won. The number was {random_number}')
        game_is_over=True
    
    difficulty_level-=1


    if difficulty_level==0:
        print(f"You run out of attempts. You lost. The number was {random_number}")
        game_is_over=True
    elif difficulty_level!=0 and game_is_over==False and guess!=random_number:
        print(f'You have {difficulty_level} attempts remaining')