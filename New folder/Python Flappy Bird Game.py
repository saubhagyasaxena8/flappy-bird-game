                                                             # Flappy-Bird-Game          

import pygame
import sys
import random

# Game Constants
WIDTH = 400
HEIGHT = 600
FPS = 60
GRAVITY = 0.5
JUMP_HEIGHT = 8

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Floppy Bird")
clock = pygame.time.Clock()

# Game Variables
bird_img = pygame.image.load("gallery\sprites\Bird.png").convert_alpha()
bird_rect = bird_img.get_rect(center=(100, HEIGHT // 2))
pipe_img = pygame.image.load("gallery\sprites\pipe.png").convert_alpha()

pipes = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1500)

score = 0
game_over = False

font = pygame.font.Font(None, 36)

def create_pipe():
    pipe_height = random.randint(150, 400)
    bottom_pipe = pipe_img.get_rect(midtop=(WIDTH, pipe_height))
    top_pipe = pipe_img.get_rect(midbottom=(WIDTH, pipe_height - 150))
    return bottom_pipe, top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= HEIGHT:
            screen.blit(pipe_img, pipe)
        else:
            flipped_pipe = pygame.transform.flip(pipe_img, False, True)
            screen.blit(flipped_pipe, pipe)

def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return True
    if bird_rect.top <= 0 or bird_rect.bottom >= HEIGHT:
        return True
    return False

def update_score():
    global score
    score += 1

def display_score():
    score_surface = font.render(f"Score: {score}", True, WHITE)
    score_rect = score_surface.get_rect(center=(WIDTH // 2, 50))
    screen.blit(score_surface, score_rect)

# Game Loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_rect.y -= JUMP_HEIGHT

        if event.type == SPAWNPIPE:
            pipes.extend(create_pipe())

    screen.fill(BLACK)

    bird_rect.y += GRAVITY
    screen.blit(bird_img, bird_rect)

    pipes = move_pipes(pipes)
    draw_pipes(pipes)

    if pipes:
        if pipes[0].right < 0:
            pipes.pop(0)
            update_score()

    game_over = check_collision(pipes)
    display_score()

    pygame.display.update()
    clock.tick(FPS)
