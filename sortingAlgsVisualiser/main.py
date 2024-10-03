import time
import pygame
import random

pygame.init()

WIDTH, HEIGHT = 1200, 800
DEFAULT_ARRAY_LENGTH = 50
CELL_SIZE = 7
GAP_SIZE = 1
WHITE = pygame.Color(255, 255, 255)
GREEN = pygame.Color(0, 255, 0)
BLACK = pygame.Color(0, 0, 0)

#pygame.time.Clock()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Data Sorting Algorithms Visualiser")

def generate_random_array(length=DEFAULT_ARRAY_LENGTH):
    array = [0 for _ in range(length)]
    for i in range(length):
        array[i] += random.randint(1, 100)
    return array

def draw_data_set(array):
    length = len(array)
    for i in range(length):
        data_rect = pygame.Rect((CELL_SIZE*(i+1), 0, CELL_SIZE, CELL_SIZE*array[i]))
        pygame.draw.rect(window, GREEN, data_rect)
        pygame.display.flip()

def draw_bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            # 100% useless, it's just to keep the os responsive
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

                rect1 = pygame.Rect(CELL_SIZE*(j+1), 0, CELL_SIZE, HEIGHT)
                rect2 = pygame.Rect(CELL_SIZE*(j+2), 0, CELL_SIZE, HEIGHT)

                window.fill(BLACK, rect1)
                window.fill(BLACK, rect2)

                pygame.display.flip()

                n_rect1 = pygame.Rect(CELL_SIZE*(j+1), 0, CELL_SIZE, CELL_SIZE*array[j])
                n_rect2 = pygame.Rect(CELL_SIZE*(j+2), 0, CELL_SIZE, CELL_SIZE*array[j+1])

                pygame.draw.rect(window, GREEN, n_rect1)
                pygame.draw.rect(window, GREEN, n_rect2)

                pygame.display.flip()

            pygame.time.delay(10)

        window.fill(WHITE, pygame.Rect(CELL_SIZE*(n-i-1), 0, CELL_SIZE, CELL_SIZE*max(array[:-1-i])))
        pygame.display.flip()
        pygame.time.delay(1)

def show_sorting_data(array, sort="bubble"):
    match sort:
        case "bubble":
            draw_bubble_sort(array)

run = True
generated = False
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

    if not generated:
        arr = generate_random_array(100)
        draw_data_set(arr)
        generated = True

        time.sleep(2)
        show_sorting_data(arr)
