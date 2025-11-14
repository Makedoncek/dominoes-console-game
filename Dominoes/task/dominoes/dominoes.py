import random

def setup_game():
    while True:

        domino_set = [[i, j] for i in range(7) for j in range(i, 7)]

        random.shuffle(domino_set)
        computer_pieces = domino_set[:7]
        player_pieces = domino_set[7:14]
        stock_pieces = domino_set[14:]

        domino_snake = []
        status = ''

        for i in range(6, -1, -1):
            double_to_find = [i, i]
            if double_to_find in computer_pieces:
                domino_snake.append(double_to_find)
                computer_pieces.remove(double_to_find)
                status = "player"
                break
            elif double_to_find in player_pieces:
                domino_snake.append(double_to_find)
                player_pieces.remove(double_to_find)
                status = "computer"
                break

        if status != '':
            break
    return stock_pieces, player_pieces, computer_pieces, domino_snake, status

def print_board(stock_pieces, player_pieces, computer_pieces, domino_snake):
    print("=" * 70)
    print("Stock size:", len(stock_pieces))
    print("Computer pieces:", len(computer_pieces), "\n")

    if len(domino_snake) <= 6:
        str_domino_snake = "".join(str(el) for el in domino_snake)
        print(str_domino_snake)
    else:
        str_domino_snake = ""
        # first 3 elements
        for i in range(3):
            str_domino_snake += str(domino_snake[i])

        str_domino_snake += "..."

        for i in range(-3, 0):
            str_domino_snake += str(domino_snake[i])
        print(str_domino_snake)

    print()

    print("Your pieces:")
    for i, piece in enumerate(player_pieces):
        print(f"{i + 1}:{piece}")

def check_game_over(player_pieces, computer_pieces, domino_snake):
    # end-game conditions
    if len(player_pieces) == 0:
        print("Status: The game is over. You won!")
        return True
    elif len(computer_pieces) == 0:
        print("Status: The game is over. The computer won!")
        return True
    else:
        left_end = domino_snake[0][0]
        right_end = domino_snake[-1][1]
        if left_end == right_end:
            count_similar = 0
            for piece in domino_snake:
                count_similar += piece.count(left_end)
            if count_similar == 8:
                print("Status: The game is over. It's a draw!")
                return True

    return False

def handle_player_turn(player_pieces, stock_pieces, domino_snake):
    print("\nStatus: It's your turn to make a move. Enter your command.")
    while True:
        try:
            player_choice = int(input())
        except ValueError:
            print("Invalid input. Please try again.")
            continue
        if -len(player_pieces) <= player_choice <= len(player_pieces):

            if player_choice > 0:
                right_end = domino_snake[-1][1]
                piece_index = player_choice - 1

                if right_end in player_pieces[piece_index]:
                    piece_to_move = player_pieces.pop(piece_index)
                    if right_end != piece_to_move[0]:
                        piece_to_move = piece_to_move[::-1]
                    domino_snake.append(piece_to_move)
                    break
                else:
                    print("Illegal move. Please try again.")

            elif player_choice < 0:
                left_end = domino_snake[0][0]
                piece_index = abs(player_choice) - 1

                if left_end in player_pieces[piece_index]:
                    piece_to_move = player_pieces.pop(piece_index)
                    if left_end != piece_to_move[1]:
                        piece_to_move = piece_to_move[::-1]
                    domino_snake.insert(0,piece_to_move)
                    break
                else:
                    print("Illegal move. Please try again.")

            elif player_choice == 0:
                if len(stock_pieces) > 0:
                    new_piece = (stock_pieces.pop())
                    player_pieces.append(new_piece)
                break

        else:
            print("Invalid input. Please try again.")

    return player_pieces, stock_pieces, domino_snake

def handle_computer_turn(computer_pieces, stock_pieces, domino_snake):
    print("\nStatus: Computer is about to make a move. Press Enter to continue...")
    input()

    counts = [0] * 7
    pieces_to_count = computer_pieces + domino_snake
    for piece in pieces_to_count:
        for num in piece:
            counts[num] += 1
    scored_pieces = []
    for [a,b] in computer_pieces:
        score = counts[a] + counts[b]
        scored_pieces.append((score,[a,b]))
    scored_pieces.sort(reverse=True)
    sorted_dominoes = [piece for score, piece in scored_pieces]

    left_end = domino_snake[0][0]
    right_end = domino_snake[-1][1]
    for piece in sorted_dominoes:
        if left_end in piece:
            computer_pieces.remove(piece)
            if left_end != piece[1]:
                piece = piece[::-1]
            domino_snake.insert(0, piece)

            return computer_pieces, stock_pieces, domino_snake

        elif right_end in piece:
            computer_pieces.remove(piece)
            if right_end != piece[0]:
                piece = piece[::-1]
            domino_snake.append(piece)

            return computer_pieces, stock_pieces, domino_snake

        # when no options left, take piece from stock_pieces(if possible)
    if len(stock_pieces) > 0:
        new_piece = stock_pieces.pop()
        computer_pieces.append(new_piece)
    return computer_pieces, stock_pieces, domino_snake


if __name__ == "__main__":
    stock_pieces, player_pieces, computer_pieces, domino_snake, status = setup_game()

    while True:
        print_board(stock_pieces, player_pieces, computer_pieces, domino_snake)
        if check_game_over(player_pieces, computer_pieces, domino_snake):
            break

        if status == "computer":
            computer_pieces, stock_pieces, domino_snake = handle_computer_turn(computer_pieces, stock_pieces, domino_snake)
            status = "player"


        elif status == "player":
            player_pieces, stock_pieces, domino_snake = handle_player_turn(player_pieces, stock_pieces, domino_snake)
            status = "computer"
