import sys


def print_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print()


def check_win(board, player):
    wins = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    return any(board[a]==board[b]==board[c]==player for a,b,c in wins)


def check_draw(board):
    return all(cell != " " for cell in board)


def get_move(board, player):
    while True:
        try:
            choice = input(f"Player {player}, enter your move from 1 - 9 or 'q' to quit: ")

            if choice.lower() == "q":
                print("Thanks. Goodbye!")
                sys.exit(0)

            pos = int(choice) - 1

            if pos < 0 or pos > 8:
                print("Please choose a valid number (from 1 - 9)")
                continue

            if board[pos] != " ":
                print("That slot is filled. Please select another slot..")
                continue

            return pos

        except ValueError:
            print("You have entered an invalid number. Please choose a number from 1 - 9 or type 'q' to quit")


def computer_easy_move(board):
    available = [i for i, c in enumerate(board) if c == " "]
    return random.choice(available)


def play_round():
    board = [" "] * 9
    current_user = "X"
    print("The board positions are numbered like this")
    print()
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print()

    while True:
        print_board(board)
        if current_user == "X":
            move = get_move(board, current_user)
            board[move] = current_user
        else:
            print("Computer is thinking...")
            move = computer_easy_move(board)
            board[move] = current_user

        if check_win(board, current_user):
            print_board(board)
            print(f"Player {current_user} wins! 🎉")
            return current_user

        if check_draw(board):
            print_board(board)
            print("It was a draw")
            return "Draw"

        current_user = "O" if current_user == "X" else "X"


def main():
    print("Welcome to C.O.R's Tic-Tac-Toe game!")

    while True:
        game = play_round()
        again = input("Want to play again? 'y/n': ").strip().lower()
        if again not in ("y", "yes"):
            print("Thanks for playing. Goodbye!")
            break



if __name__ == "__main__":
    main()
