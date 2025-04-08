import pygame
import math

def draw_roman_numbers(screen, center, radius, font, color, clock_list):
    roman_numerals = ['XII', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI']

    current = clock_list.head
    i = 0

    while True:
        angle = math.radians((360 / 12) * i - 90)
        x = center[0] + math.cos(angle) * (radius - 40)
        y = center[1] + math.sin(angle) * (radius - 40)

        numeral = roman_numerals[current.value - 1]
        text = font.render(numeral, True, color)
        text_rect = text.get_rect(center=(x, y))
        screen.blit(text, text_rect)

        current = current.next
        i += 1
        if current == clock_list.head:
            break


def draw_lines(screen, center, radius, color_min, color_sec, second):
    for i in range(60):
        angle = math.radians((360 / 60) * i - 90)

        if i % 5 == 0:
            length = radius - 15
            width = 3
        else:
            length = radius - 10
            width = 1

        x_start = center[0] + math.cos(angle) * length
        y_start = center[1] + math.sin(angle) * length

        x_end = center[0] + math.cos(angle) * radius
        y_end = center[1] + math.sin(angle) * radius

        pygame.draw.line(screen, color_min, (x_start, y_start), (x_end, y_end), width)


def draw_hands(screen, center, radius, hour, minute, second):
    
    hour_angle = math.radians((360 / 12) * hour - 90 + (30 / 60) * minute)
    hour_length = radius * 0.5
    hour_x = center[0] + math.cos(hour_angle) * hour_length
    hour_y = center[1] + math.sin(hour_angle) * hour_length
    pygame.draw.line(screen, (0, 0, 0), center, (hour_x, hour_y), 6)

    minute_angle = math.radians((360 / 60) * minute - 90)
    minute_length = radius * 0.7
    minute_x = center[0] + math.cos(minute_angle) * minute_length
    minute_y = center[1] + math.sin(minute_angle) * minute_length
    pygame.draw.line(screen, (0, 0, 0), center, (minute_x, minute_y), 4)

    second_angle = math.radians((360 / 60) * second - 90)
    second_length = radius * 0.85
    second_x = center[0] + math.cos(second_angle) * second_length
    second_y = center[1] + math.sin(second_angle) * second_length
    pygame.draw.line(screen, (255, 0, 0), center, (second_x, second_y), 2)
