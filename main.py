import random

'''
Rules:
4 pegs color code
blue, green, yellow, orange, silver, white, pink, red.
white: corrent colour, wrong position
red: correct colour and correct position
2 players: code master chooses code and gives red/white feedback, guesser gueses the code within 12 tries.
'''

CHANCES = 1
CODE_LEN = 4

def get_code():
    # Generate random code
    opts = ['R', 'G', 'B', 'W', 'Y', 'O', 'P', 'S']
    code = random.choices(opts, k=CODE_LEN)
    return code

def show_board(board):
    if len(board):
        # show the player's current board
        for row in board:
            print(row)
    else:
        print('[]')

def calc_hint(code, guess):
    correct_colour = 0
    correct_position = 0
    for peg in guess:
        if peg in code:
            correct_colour += 1
    for index, peg in enumerate(code):
        if peg == guess[index]:
            correct_position += 1
            correct_colour -= 1
            print(correct_colour)
            print(correct_position)
    return correct_colour, correct_position

def update_stats(game_stats):
    game_stats.update({"guesses": (game_stats['guesses'] + count)})
    game_stats.update({
        "avg_white":(
            game_stats['avg_white'] + sum([guess[4] for guess in board])
            )
        })
    game_stats.update({
        "avg_red":(
            game_stats['avg_red'] + sum([guess[-1] for guess in board])
            )
        })
    return game_stats

# Remember previous tries on game board
board = []
code = get_code()
game_over = False
count = 0
wins = 0
game_stats = {
    "wins": 0,
    "losses": 0,
    "guesses": 0,
    "avg_white": 0,
    "avg_red": 0
}

while True:
    show_board(board)
    # Check how many tries the player has left
    if count == CHANCES:
        print('You are out of guesses!')
        game_stats.update({"losses": (game_stats['losses'] + 1)})
        game_stats = update_stats(game_stats)
        game_over = True
    else:
        print(f"You have {CHANCES - count} guesses left!")

        # Ask player for their guess
        guess = [item.upper() for item in input("Enter your guess: ").split()]
        print(guess)

        # Proceed game if guess is valid
        if len(guess) == CODE_LEN:
            # Check if the guess is correct
            result = [a == b for a, b in zip(code, guess)]
            if all(result):
                print(f"You win with {count+1} tries!")
                game_stats.update({"wins": (game_stats['wins'] + 1)})
                game_stats = update_stats(game_stats)
                game_over = True
            else:
                # Give player a hint
                white, red = calc_hint(code, guess)

                # Show player hints
                print(f"# of correct colours: {white}")
                print(f"# of correct positions: {red}")

                # Save player guess to board
                guess.append(white)
                guess.append(red)
                board.append(guess)
            count += 1  # next turn
            print()
    # Ask to play again
    if game_over:
        print(f"\nThe code was {code}")
        print("== YOUR BOARD ==")
        show_board(board)
        play_again = input('Play Again? [y/n]: ')
        if play_again.lower() != 'y':
            break
        # Reset game
        game_over = False
        count = 0
        board.clear()

print("\n=== Game Stats ===")
total_games = game_stats['wins'] + game_stats['losses']
print('Winning % {}'. format(game_stats['wins']/total_games))
print(f"Avg. tries per game: {game_stats['guesses']/total_games}")
print("Avg. correct colours per game: {}".format(game_stats['avg_white']/total_games))
print(f"Avg. correct position per game: {game_stats['avg_red']/total_games}")
# Save game stats and high score