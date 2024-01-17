import sys
from time import sleep
import pygame

from settings import Settings
from board import Board
from button import Button


class TicTac:
    def __init__(self):
        """ Initialize the game and create resources """
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        # Game Window
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Tic Tac Toe!")

        self.board = Board(self)

        self.game_active = False

        # Make the Play button
        self.play_button = Button(self, "Play!")

        self.winner = None

    def run_game(self):
        """ Start the main loop for the game """
        while True:
            # Watch Keyboard and mouse events
            self._check_events()
            # Redraw the screen during each loop
            self._update_screen()
            # Frame limit
            self.clock.tick(60)

    def _check_events(self):
        """ Respond to key presses and mouse events """
        for event in pygame.event.get():
            # Quit Game
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
            # Draw symbols on the board and check win or draw
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_active:
                    self.board.add_player_symbol()
                    self.board.update_gui_board()
                    # check for winner and update board accordingly
                    self.winner = self.board.check_winner()
                    self._game_status()
            # Display Play button
                else:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """ Start New Game when player clicks play"""
        if self.play_button.rect.collidepoint(mouse_pos):
            self.game_active = True
            self.board.reset_board()

    def _game_status(self):
        """ Check win or draw """
        if self.winner:
            self.board.update_winner_board(self.winner)
            self.play_button.winning_message(self.winner)
            self.game_active = False
        elif self.board.check_draw():
            self.play_button.draw_message()
            self.game_active = False

    def _update_screen(self):
        """ Update images on the screen """
        self.screen.fill(self.settings.bg_color)
        self.board.draw_board()
        self.board.display_updated_board()

        if not self.game_active:
            self.play_button.draw_button()
        # make the most recently drawn screen visible
        pygame.display.update()
