import random

'''
Rules:
4 pegs color code
blue, green, yellow, orange, silver, white, pink, red.
white: corrent colour, wrong position
red: correct colour and correct position
2 players: code master chooses code and gives red/white feedback, guesser gueses the code within 12 tries.
'''

CHANCES = 3

def get_code():
    # Generate random code
    opts = ['R', 'G', 'B', 'W', 'Y', 'O', 'P', 'S']
    num_to_select = 4  # set the number to select here.
    code = random.choices(opts, k=num_to_select)
    return code

# Remember previous tries on game board
board = []
code = get_code()
guess = []
playing_game = True
count = 0
correct_colour = 0
correct_position = 0

while playing_game:
    print(f"The board:")  # show the player's current board
    for row in board:
        print(row)

    # Check how many tries the player has left
    if count == CHANCES:
        print('You are out of guesses!')
        break
    print(f"You have {CHANCES - count} guesses left!")

    # Ask player for their guess
    guess = [item.upper() for item in input("Enter your guess: ").split()]
    print(guess)

    # Proceed game if guess is valid
    if len(guess) == 4:
        # Check if the guess is correct
        result = [a == b for a, b in zip(code, guess)]
        if all(result):
            print(f"You win with {count+1} tries!")
            playing_game = False
        else:  # Compare guess and code
            # Correct colour in the incorrect position
            for peg in guess:
                if peg in code:
                    correct_colour += 1

            # Correct colour in correct position
            for index, (a, b) in enumerate(zip(code, guess)):
                if a == b:
                    correct_position += 1
                    correct_colour -= 1

            # Show player hints
            print(f"# of correct colours: {correct_colour}")
            print(f"# of correct positions: {correct_position}")

            # Save player guess to board
            guess_copy = guess
            guess_copy.append(correct_colour)
            guess_copy.append(correct_position)
            print(guess_copy)
            board.append(guess_copy)
            # Reset lists
            correct_colour = 0
            correct_position = 0 
        count += 1  # next turn
        print()
# Game over
print(f"The code was {code}")
for row in board:
    print(row)
