import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
FPS = 30

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Falling Objects Game")

# Define the player and object
player_size = 50
player_color = BLACK
player_pos = [WIDTH // 2, HEIGHT - 2 * player_size]

object_size = 50
object_color = RED
object_pos = [random.randint(0, WIDTH - object_size), 0]
object_speed = 10

# Clock for controlling frame rate
clock = pygame.time.Clock()

def drop_objects(object_pos):
    if object_pos[1] >= 0 and object_pos[1] < HEIGHT:
        object_pos[1] += object_speed
    else:
        object_pos[1] = 0
        object_pos[0] = random.randint(0, WIDTH - object_size)

def detect_collision(player_pos, object_pos):
    px, py = player_pos
    ox, oy = object_pos
    if (ox >= px and ox < (px + player_size)) or (px >= ox and px < (ox + object_size)):
        if (oy >= py and oy < (py + player_size)) or (py >= oy and py < (oy + object_size)):
            return True
    return False

# Game loop
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= 10
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += 10

    screen.fill(WHITE)

    drop_objects(object_pos)

    if detect_collision(player_pos, object_pos):
        print("Game Over!")
        game_over = True

    pygame.draw.rect(screen, player_color, (player_pos[0], player_pos[1], player_size, player_size))
    pygame.draw.rect(screen, object_color, (object_pos[0], object_pos[1], object_size, object_size))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
