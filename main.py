from tictac import TicTac

""" Text Based Game """
# def create_board():
#     """ Create a blank 3x3 grid """
#     grid = [['' for _ in range(3)] for _ in range(3)]
#     return grid
#
#
# def choose_symbols():
#     """ Choose a symbol for the players """
#     symbol_1 = input("Player 1, do you want to be X or O? ")
#     symbol_1 = symbol_1.upper()
#
#     # Assign symbol to player 2
#     if symbol_1 == 'X':
#         symbol_2 = 'O'
#         print(f"Player 1 is {symbol_1} and Player 2 is {symbol_2}")
#     else:
#         symbol_2 = 'X'
#         print(f"Player 1 is {symbol_1} and Player 2 is {symbol_2}")
#
#     print("\n")
#     return symbol_1.upper(), symbol_2.upper()
#
#
# def print_board(game_board):
#     """ print current board """
#     for items in game_board:
#         print(items)
#
#
# def get_player_turn(game_moves, p1, p2):
#     """ Determine which player takes the turn based on the number of moves """
#     return p1 if game_moves % 2 == 0 else p2
#
#
# def get_valid_player_entry(game_board):
#     """ Ask player to enter the cell for the turn.
#     Check if the entry for the rows and columns chosen is correct and raise an error if incorrect.
#     Also Check if the user chosen cell already has an entry. """
#     while True:
#         try:
#             row_input = int(input("Choose a row from 1 to 3: "))
#             column_input = int(input("Choose a column from 1 to 3: "))
#             if 1 <= row_input <= 3 and 1 <= column_input <= 3:
#                 if game_board[row_input - 1][column_input - 1] == '':
#                     return row_input, column_input
#                 else:
#                     print("Cell is already full. Please try again")
#             else:
#                 print("Invalid Input. Please enter a valid row and column")
#         except ValueError:
#             print("Invalid Input. Please enter a valid row and column")
#
#
# def check_winner(game_board, game_player_1, game_player_2):
#     """ Takes the current state of the board and the player symbols and checks the winner """
#     # Check the rows
#     for rows in game_board:
#         # Return the winner if all elements in the row are a players symbol
#         if all(elements == game_player_1 for elements in rows):
#             return game_player_1
#         elif all(elements == game_player_2 for elements in rows):
#             return game_player_2
#
#     # Check the columns
#     for col in range(3):
#         # Return the winner if all elements in the column are a players symbol
#         if all(game_board[rows][col] == game_player_1 for rows in range(3)):
#             return game_player_1
#         elif all(game_board[rows][col] == game_player_2 for rows in range(3)):
#             return game_player_2
#
#     # Check diagonals and return the winner if all the diagonals match
#     if all(game_board[i][i] == game_player_1 for i in range(3)):
#         return game_player_1
#     elif all(game_board[i][i] == game_player_2 for i in range(3)):
#         return game_player_2
#
#     if all(game_board[i][2-i] == game_player_1 for i in range(3)):
#         return game_player_1
#     elif all(game_board[i][2-i] == game_player_2 for i in range(3)):
#         return game_player_2
#
#     # Return None if no winner is found
#     return None
#
#
# # Create Blank Board
# board = create_board()
# # Display Board
# print_board(board)
# # Assign Symbols to players
# player_1, player_2 = choose_symbols()
#
# # Start the game
# moves = 0
#
# while moves < 9:
#     # Decide which player takes the turn
#     player = get_player_turn(moves, player_1, player_2)
#     print(f"\n{player}'s Turn\n")
#     # Get players input for placing the symbol
#     row, column = get_valid_player_entry(board)
#     print("\n")
#     moves += 1
#     # Place player symbol on the board
#     board[row - 1][column - 1] = player
#     # Display board after updating
#     print_board(board)
#     # Check if there is a winner
#     winner = check_winner(board, player_1, player_2)
#
#     # End Game if there is a winner and display winners name
#     if winner:
#         winning_player = "Player 1" if winner == player_1 else player_2
#         print(f"The winner is {winning_player}")
#         break
#
#     # Game Drawn if there is no winner
#     if moves == 9 and not winner:
#         print("\nThe game is a draw")
#

""" GUI Based """
if __name__ == '__main__':
    game = TicTac()
    game.run_game()
