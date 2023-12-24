#import RPi.GPIO as GPIO
import pygame  # or import tkinter
import sys

#GPIO.setmode(GPIO.BCM)  # Use Broadcom pin-numbering
#GPIO.setup([PIN1, PIN2], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

pygame.init()

# Get the desktop sizes
desktop_sizes = pygame.display.get_desktop_sizes()

# Select an appropriate window size based on the desktop sizes
SCREEN_WIDTH, SCREEN_HEIGHT = desktop_sizes[0]  # Choose the appropriate index if multiple displays are detected

# Set the screen to the full resolution
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption('Scoreboard')

running = True
score_player1 = 0
score_player2 = 0

# Colors
BLACK = pygame.Color('black')
WHITE = pygame.Color('white')
RED = pygame.Color('red')
BLUE = pygame.Color('blue')

# Fonts
font = pygame.font.Font(pygame.font.get_default_font(), 74)

# Calculate positions
# Get the Pygame window size
window_width, window_height = screen.get_width(), screen.get_height()
center_x = window_width // 2
top_y = window_height // 8
bottom_y = 2 * window_height // 4

def render_text_with_outline(text, font, main_color, outline_color, outline_width):
    # Render the main text
    text_surface = font.render(text, True, main_color)

    # Create a surface with the text and outline
    outline_surface = pygame.Surface((text_surface.get_width() + outline_width*2, text_surface.get_height() + outline_width*2), pygame.SRCALPHA)
    outline_surface.fill((0, 0, 0, 0))  # Fill with transparent color
    text_rect = text_surface.get_rect(center=(outline_surface.get_width() // 2, outline_surface.get_height() // 2))
    outline_surface.blit(text_surface, text_rect)  # Blit the text onto the outline surface

    # Draw the outline
    for i in range(-outline_width, outline_width + 1, max(1, outline_width // 10)):
        for j in range(-outline_width, outline_width + 1, max(1, outline_width // 10)):
            if i != 0 or j != 0:
                outline_rect = text_rect.move(i, j)
                outline_surface.blit(text_surface, outline_rect)

    return outline_surface

def draw_scoreboard():
    background_image = pygame.image.load('./data/background.bmp')
    background_image = pygame.transform.scale(background_image, (window_width, window_height))
    screen.blit(background_image, (0, 0))
    
    # Player names
    player1_name = "Player 1"
    player2_name = "Player 2"

    # Fonts
    pygame.font.init()
    label_font = pygame.font.Font(pygame.font.get_default_font(), 100)
    score_font = pygame.font.Font(pygame.font.get_default_font(), 250)  # Larger font for scores

    # Create outlined text
    score_player1_text = render_text_with_outline(str(score_player1), score_font, BLUE, WHITE, 2)
    score_player2_text = render_text_with_outline(str(score_player2), score_font, RED, WHITE, 2)
    
    # Calculate positions
    player_one_score_pos = (center_x // 2) - (score_player1_text.get_width() // 2)
    player_two_score_pos = center_x + (center_x // 2) - (score_player2_text.get_width() // 2)
    
    # Draw the outline coloured text on the screen
    # (adjust x, y positions as needed)
    screen.blit(score_player1_text, (player_one_score_pos, bottom_y))
    screen.blit(score_player2_text, (player_two_score_pos, bottom_y))

    # Render Text
    player1_label = label_font.render(player1_name, True, WHITE)
    player2_label = label_font.render(player2_name, True, WHITE)
    score_player1_text = score_font.render(str(score_player1), True, WHITE)
    score_player2_text = score_font.render(str(score_player2), True, WHITE)

    # Draw Player Labels and Scores
    screen.blit(player1_label, ((center_x // 2) - (player1_label.get_width() // 2), top_y))
    screen.blit(player2_label, (center_x + (center_x // 2) - (player2_label.get_width() // 2), top_y))
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
            elif event.key == pygame.K_UP:
                score_player1 += 1
            elif event.key == pygame.K_DOWN:
                score_player1 -= 1
            elif event.key == pygame.K_LEFT:
                score_player2 += 1
            elif event.key == pygame.K_RIGHT:
                score_player2 -= 1
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



