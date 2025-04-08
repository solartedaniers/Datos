import pygame
import math
from datetime import datetime
from classes.circular_list import DoublyCircularLinkedList
from utils.helpers import draw_lines, draw_roman_numbers, draw_hands
import pytz

pygame.init()

WIDTH, HEIGHT = 600, 600
CENTER = (WIDTH // 2, HEIGHT // 2)
RADIUS = 250

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Reloj Echo por Daniers")

background = pygame.image.load("assets/wood_background.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

tick_sound = pygame.mixer.Sound("songs/tick.mp3")

bird_images = []
for i in range(1, 13):
    bird_path = f"assets/birds/bird{i}.jpg"
    bird = pygame.image.load(bird_path)
    bird = pygame.transform.scale(bird, (200, 200))
    bird_images.append(bird)

birds = DoublyCircularLinkedList()
for bird in bird_images:
    birds.insert(bird)

current_bird = birds.head

font = pygame.font.SysFont(None, 36)
small_font = pygame.font.SysFont(None, 25)

clock_numbers = DoublyCircularLinkedList()
for i in range(1, 13):
    clock_numbers.insert(i)

countries = [
    "Colombia",
    "México",
    "España",
    "Argentina"
]

timezones = {
    "Colombia": "America/Bogota",
    "México": "America/Mexico_City",
    "España": "Europe/Madrid",
    "Argentina": "America/Argentina/Buenos_Aires"
}

selected_country_index = 0
selected_country = countries[selected_country_index]

clock = pygame.time.Clock()
last_second = -1
last_hour = -1

running = True
while running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                selected_country_index = (selected_country_index + 1) % len(countries)
                selected_country = countries[selected_country_index]
            if event.key == pygame.K_LEFT:
                selected_country_index = (selected_country_index - 1) % len(countries)
                selected_country = countries[selected_country_index]

    tz = pytz.timezone(timezones[selected_country])
    now = datetime.now(tz)

    hour = now.hour % 12
    minute = now.minute
    second = now.second

    if second != last_second:
        tick_sound.play()
        last_second = second

    if hour != last_hour:
        current_bird = current_bird.next
        last_hour = hour

    bird_rect = current_bird.value.get_rect(center=CENTER)
    screen.blit(current_bird.value, bird_rect)

    draw_lines(screen, CENTER, RADIUS, (0, 0, 0), (0, 0, 0), second)

    draw_roman_numbers(screen, CENTER, RADIUS, font, (0, 0, 0), clock_numbers)

    draw_hands(screen, CENTER, RADIUS, hour, minute, second)

    text = small_font.render(f"Zona Horaria: {selected_country}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
