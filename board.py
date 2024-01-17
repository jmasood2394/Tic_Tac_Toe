import pygame


class Board:
    def __init__(self, game):
        """ Initialize Game Board and assign player symbol """
        self.screen = game.screen
        # Game Board to store player cell choice
        self.board = [['' for _ in range(3)] for _ in range(3)]
        # List to store the mouse position based on the click
        self.gui_board = [[[None, None], [None, None], [None, None]],
                          [[None, None], [None, None], [None, None]],
                          [[None, None], [None, None], [None, None]]]
        self.board_image = pygame.image.load("images/Board.png")
        self.image_x = pygame.image.load("images/X.png")
        self.image_o = pygame.image.load("images/O.png")
        # Assign X to player 1
        self.player = 'X'

    def draw_board(self):
        """ Draw board on the screen """
        self.screen.blit(self.board_image, (64, 64))

    def add_player_symbol(self):
        """ Add player symbol to the board based on the mouse position and switch player """
        current_pos = pygame.mouse.get_pos()
        # convert the position tuple to x and y co-ordinate to center of the cell
        converted_x = (current_pos[0] - 65) / 835 * 2
        converted_y = current_pos[1] / 835 * 2
        if self.board[round(converted_y)][round(converted_x)] == '':
            self.board[round(converted_y)][round(converted_x)] = self.player

            # Switch player
            if self.player == 'O':
                self.player = 'X'
            else:
                self.player = 'O'

    def update_gui_board(self):
        """ Add image to the GUI Board based on the game board """
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 'X':
                    # Create an X image and rect
                    self.gui_board[i][j][0] = self.image_x
                    self.gui_board[i][j][1] = self.image_x.get_rect(center=(j*300+150, i*300+150))
                elif self.board[i][j] == 'O':
                    self.gui_board[i][j][0] = self.image_o
                    self.gui_board[i][j][1] = self.image_o.get_rect(center=(j * 300 + 150, i * 300 + 150))

    def check_draw(self):
        """ Check if the board is full """
        for row in self.board:
            if '' in row:
                return False
        return True

    def check_winner(self):
        """ Check if a player has won """
        # Check Rows
        for row in self.board:
            if all(cell == 'X' for cell in row):
                return 'X'
            elif all(cell == 'O' for cell in row):
                return 'O'

        # Check columns
        for col in range(3):
            if all(self.board[r][col] == 'X' for r in range(3)):
                return 'X'
            elif all(self.board[r][col] == 'O' for r in range(3)):
                return 'O'

        # Check Diagonals
        if all(self.board[i][i] == 'X' for i in range(3)):
            return 'X'
        elif all(self.board[i][i] == 'O' for i in range(3)):
            return 'O'

        if all(self.board[i][2 - i] == 'X' for i in range(3)):
            return 'X'
        elif all(self.board[i][2 - i] == 'O' for i in range(3)):
            return 'O'

        return None

    def update_winner_board(self, winner):
        """ Update the image of the winning symbol """
        winning_image_path = f"images/Winning_{winner}.png"
        winning_image = pygame.image.load(winning_image_path)

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == winner:
                    self.gui_board[i][j][0] = winning_image
                    self.gui_board[i][j][1] = winning_image.get_rect(center=(j * 300 + 150, i * 300 + 150))

    def display_updated_board(self):
        """ Display updated Board """
        for i in range(3):
            for j in range(3):
                if self.gui_board[i][j][0] is not None:
                    self.screen.blit(self.gui_board[i][j][0], self.gui_board[i][j][1])

    def reset_board(self):
        """ Reset the game board and the gui board """
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.gui_board = [[[None, None], [None, None], [None, None]],
                          [[None, None], [None, None], [None, None]],
                          [[None, None], [None, None], [None, None]]]