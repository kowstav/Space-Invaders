import pygame
import random
import os

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders Reloaded")

# Load assets
ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")
player_img = pygame.image.load(os.path.join(ASSETS_DIR, "player.png"))
enemy_img = pygame.image.load(os.path.join(ASSETS_DIR, "enemy.png"))
laser_img = pygame.image.load(os.path.join(ASSETS_DIR, "laser.png"))

# Player settings
player_x = WIDTH // 2 - player_img.get_width() // 2
player_y = HEIGHT - player_img.get_height() - 10
player_speed = 5

# Laser settings
lasers = []  # each laser is [x, y]
laser_speed = 7

# Enemy settings
num_enemies = 6
enemies = []  # each enemy is [x, y, speed]
enemy_speed = 1
for i in range(num_enemies):
    x = random.randint(0, WIDTH - enemy_img.get_width())
    y = random.randint(50, 150)
    enemies.append([x, y, enemy_speed])

# Score
score = 0
font = pygame.font.SysFont(None, 36)

# Game Over flag
game_over = False

def show_score():
    score_surf = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_surf, (10, 10))


def show_game_over():
    over_surf = font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(over_surf, (WIDTH//2 - over_surf.get_width()//2, HEIGHT//2))

# Game loop
clock = pygame.time.Clock()
while True:
    screen.fill((0, 0, 0))  # Black background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_SPACE:
                # Create new laser
                lasers.append([player_x + player_img.get_width()//2 - laser_img.get_width()//2, player_y])

    keys = pygame.key.get_pressed()
    if not game_over:
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_img.get_width():
            player_x += player_speed

    # Draw player
    screen.blit(player_img, (player_x, player_y))

    # Update and draw lasers
    for laser in lasers[:]:
        laser[1] -= laser_speed
        screen.blit(laser_img, (laser[0], laser[1]))
        if laser[1] < 0:
            lasers.remove(laser)

    # Update and draw enemies
    for enemy in enemies:
        if game_over:
            break
        enemy[0] += enemy[2]
        # Change direction and move down
        if enemy[0] <= 0 or enemy[0] >= WIDTH - enemy_img.get_width():
            enemy[2] *= -1
            enemy[1] += 40

        # Check for game over
        if enemy[1] > player_y:
            game_over = True

        # Check for collision
        for laser in lasers[:]:
            laser_rect = pygame.Rect(laser[0], laser[1], laser_img.get_width(), laser_img.get_height())
            enemy_rect = pygame.Rect(enemy[0], enemy[1], enemy_img.get_width(), enemy_img.get_height())
            if laser_rect.colliderect(enemy_rect):
                try:
                    lasers.remove(laser)
                except ValueError:
                    pass
                enemy[0] = random.randint(0, WIDTH - enemy_img.get_width())
                enemy[1] = random.randint(50, 150)
                score += 1

        screen.blit(enemy_img, (enemy[0], enemy[1]))

    # Display score or game over
    if game_over:
        show_game_over()
    else:
        show_score()

    pygame.display.update()
    clock.tick(60)