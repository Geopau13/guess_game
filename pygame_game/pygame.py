

import pygame
import random

pygame.init()

# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Guessing Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Fonts
font_large = pygame.font.Font(None, 48)
font_small = pygame.font.Font(None, 24)

class GuessingGame:
    def __init__(self):
        self.number = random.randint(1, 100)
        self.guesses_taken = 0
        self.is_won = False

    def play(self):
        while not self.is_won:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        guess = int(self.user_input)
                        self.guesses_taken += 1
                        self.check_guess(guess)
                        self.user_input = ""
                    elif event.key == pygame.K_BACKSPACE:
                        self.user_input = self.user_input[:-1]
                    else:
                        self.user_input += event.unicode

            screen.fill(WHITE)
            self.display_message("Welcome to the Guessing Game!", screen_width // 2, 100, font_large, BLACK)
            self.display_message("I'm thinking of a number between 1 and 100.", screen_width // 2, 160, font_small, BLACK)
            self.display_message("Take a guess:", screen_width // 2, 250, font_large, BLACK)
            self.display_message(self.user_input, screen_width // 2, 320, font_large, RED)
            
            pygame.display.flip()

    def check_guess(self, guess):
        if guess < self.number:
            self.display_message("Too low!", screen_width // 2, 400, font_large, GREEN)
        elif guess > self.number:
            self.display_message("Too high!", screen_width // 2, 400, font_large, GREEN)
        else:
            self.is_won = True
            self.display_message(f"Congratulations! You guessed the number in {self.guesses_taken} attempts.", screen_width // 2, 400, font_small, GREEN)

    def display_message(self, text, x, y, font, color):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        screen.blit(text_surface, text_rect)

game = GuessingGame()
game.user_input = ""
game.play()





