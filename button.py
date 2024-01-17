import pygame.font


class Button:
    """ Buttons for the game """
    def __init__(self, game, msg):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 300, 150
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """ Turn message into rendered image and center on the button """
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw blank button and then draw message."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def winning_message(self, winner):
        """ Display Winner """
        msg = f"{winner} Wins!"
        self._prep_msg(msg)
        self.draw_button()

    def draw_message(self):
        """ Display Draw Game """
        msg = f"Game is a Draw!"
        self._prep_msg(msg)
        self.draw_button()
