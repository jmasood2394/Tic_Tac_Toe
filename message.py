import pygame.font


class Message:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.winner = game.winner

        self.font = pygame.font.SysFont(None, 35)

    def winning_message(self):
        msg = f"The winner is {self.winner}"
        msg_image = self.font.render(msg, True, (0, 0, 0))
        msg_rect = (450, 250)
        self.screen.blit(msg_image, msg_rect)
