import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/Снимок-экрана-2024-05-09-в-06.00.24.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")
target_width = 80
target_height = 80

target_x = random.randit(0, SCREEN_WIDTH - target_width)
target_y = random.randit(0, SCREEN_HEIGHT - target_height)

color = (random_randit(0, 255), random_randit(0, 255), random_randit(0, 255))



running = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

running = True
while running:
    pass

pygame.quit()