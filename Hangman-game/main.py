from hangman_art import stages
from hangman_art import logo
from hangman_words import word_list


print (logo)


import random
end_of_game = False

chosen_word = random.choice(word_list)
word_length = len(chosen_word)


lives = 6

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')


display = []

for _ in range(word_length):
    display += "_"

print (display)

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    

    if guess in display:
        print("You have already guessed that letter")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
       # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter==guess:
            display[position]=letter
        

    
    if guess not in chosen_word:
        print(f'You guessed {guess}, that is not correct. You lose a life')
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])

    if end_of_game==True:
        print("The word was",chosen_word)