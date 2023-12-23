#import RPi.GPIO as GPIO
import pygame  # or import tkinter
import sys

#GPIO.setmode(GPIO.BCM)  # Use Broadcom pin-numbering
#GPIO.setup([PIN1, PIN2], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

pygame.init()
# Detect current screen resolution
infoObject = pygame.display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = infoObject.current_w, infoObject.current_h

# Set the screen to the full resolution
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption('Scoreboard')

running = True
score_player1 = 0
score_player2 = 0

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Fonts
font = pygame.font.Font(None, 74)
background_image = pygame.image.load('./data/background.png')

# Calculate positions
center_x = SCREEN_WIDTH // 2
top_y = SCREEN_HEIGHT // 4
bottom_y = 3 * SCREEN_HEIGHT // 4

def render_text_with_outline(text, font, main_color, outline_color, outline_width):
    # Render the outline
    base_surface = font.render(text, True, outline_color)
    outline_surface = pygame.Surface(base_surface.get_size(), pygame.SRCALPHA)
    for dx in range(-outline_width, outline_width + 1):
        for dy in range(-outline_width, outline_width + 1):
            font.render(outline_surface, (dx, dy), text, outline_color)

    # Render the main text on top
    font.render(outline_surface, (outline_width, outline_width), text, main_color)

    return outline_surface

def draw_scoreboard():
    screen.blit(background_image, (0, 0))  # Draw the background image

    # Player names
    player1_name = "Player 1"
    player2_name = "Player 2"

    # Fonts
    pygame.font.init()
    label_font = pygame.font.Font(pygame.font.get_default_font(), 100)
    score_font = pygame.font.Font(pygame.font.get_default_font(), 350)  # Larger font for scores

    # Create outlined text
    score_player1_text = render_text_with_outline(str(score_player1), score_font, BLUE, WHITE, 2)
    score_player2_text = render_text_with_outline(str(score_player2), score_font, RED, WHITE, 2)
    
    # Calculate positions
    player_one_score_pos = center_x // 2 - score_player1_text.get_width() // 2
    player_two_score_pos = center_x + center_x // 2 - score_player2_text.get_width() // 2
    
    # Draw the text on the screen
    # (adjust x, y positions as needed)
    screen.blit(score_player1_text, (player_one_score_pos, bottom_y))
    screen.blit(score_player2_text, (player_two_score_pos, bottom_y))

    # Render Text
    player1_label = label_font.render(player1_name, True, WHITE)
    player2_label = label_font.render(player2_name, True, WHITE)
    score_player1_text = score_font.render(str(score_player1), True, BLUE)
    score_player2_text = score_font.render(str(score_player2), True, RED)

    # Draw Player Labels and Scores
    screen.blit(player1_label, (center_x // 2 - player1_label.get_width() // 2, top_y))
    screen.blit(player2_label, (center_x + center_x // 2 - player2_label.get_width() // 2, top_y))
    screen.blit(score_player1_text, (player_one_score_pos, bottom_y))
    screen.blit(score_player2_text, (player_two_score_pos, bottom_y))

    pygame.display.flip()



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Press ESC to exit
                pygame.quit()
                sys.exit()

 #   if GPIO.input(PIN1) == GPIO.HIGH:
 #       score_player1 += 1
 #   if GPIO.input(PIN2) == GPIO.HIGH:
 #       score_player2 += 1

    # Update the display with the new scores
    draw_scoreboard()

    pygame.time.delay(100)
    pygame.time.delay(100)  # Delay to debounce buttons


#GPIO.cleanup()
pygame.quit()



