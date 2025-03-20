import random
from day_7_hangman_words import word_list
from day_7_hangman_art import logo, stages

# Select a random word from the word list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Game state variables
end_of_game = False
lives = 6

# Display the game logo
print(logo) 

# Initialize the display with underscores
display = []
for _ in range(word_length):
    display.append("_")

# The above is basics where a random word is picked from a list and its length is calculated and a empty list is created and filled with "_" for the length of chosen word 
# Apart from the above there are 2 game variables initilized for better contoll of the game.
# end_of_game is a variable that controls if the game ends or not so we usually use this to start our loop so we can decide end or no 
# lives is the max health of the man

while not end_of_game: # the whole control loop of the game the condition is the key for ending the game
    guess = input("Guess a letter: ").lower()
    
    # Check if the letter has already been guessed
    if guess in display:
        print(f"You've already guessed {guess}")
    
    # Reveal the guessed letter in the word
    for position in range(word_length):
        letter = chosen_word[position] # This line choose each letter from the picked word 
        if letter == guess:               # This line checks if letter picked from picked word is equal to gussed letter
            display[position] = letter   # if there the "_" in the display list is replaced by the letter from the picked word
    
    # Reduce life if the guess is incorrect
    if guess not in chosen_word:
        print(f"{guess} is not in the word. You lose a life.")
        lives -= 1
        if lives == 0: 
            end_of_game = True
            print("You lose.")
    
    # Display the current progress
    print(f"{' '.join(display)}")
    
    # Check if the player has won
    if "_" not in display:
        end_of_game = True
        print("You win.")
    
    # Display the hangman stages
    print(stages[lives])