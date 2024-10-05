import time
import pygame
import random

pygame.init()

WIDTH, HEIGHT = 1200, 800
ARRAY_LENGTH = 150
CELL_SIZE = 7
GAP_SIZE = 1
WHITE = pygame.Color(255, 255, 255)
GREEN = pygame.Color(0, 255, 0)
RED = pygame.Color(255, 0, 0)
BLUE = pygame.Color(0, 0, 255)
BLACK = pygame.Color(0, 0, 0)

#pygame.time.Clock()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Data Sorting Algorithms Visualiser")

def generate_random_array(length=ARRAY_LENGTH):
    array = [0 for _ in range(length)]
    for i in range(length):
        array[i] += random.randint(1, 100)
    return array

def draw_data_set(array, color=WHITE):
    length = len(array)
    for i in range(length):
        data_rect = pygame.Rect((CELL_SIZE*(i+1), 0, CELL_SIZE, CELL_SIZE*array[i]))
        pygame.draw.rect(window, color, data_rect)
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

                n_rect1 = pygame.Rect(CELL_SIZE*(j+1), 0, CELL_SIZE, (CELL_SIZE*array[j]))
                n_rect2 = pygame.Rect(CELL_SIZE*(j+2), 0, CELL_SIZE, (CELL_SIZE*array[j+1]))

                pygame.draw.rect(window, WHITE, n_rect1)
                pygame.draw.rect(window, WHITE, n_rect2)

                pygame.display.flip()

                pygame.time.delay(1)

        window.fill(GREEN, pygame.Rect(CELL_SIZE*(n-i), 0, CELL_SIZE, (CELL_SIZE*array[n-1-i])))
        pygame.display.flip()
        pygame.time.delay(1)

def draw_insertion_sort(array):
    n = ARRAY_LENGTH
    i = 0
    while i < n:
        j = i
        while j > 0 and array[j-1] > array[j]:
            # 100% useless, it's just to keep the os responsive
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            array[j-1], array[j] = array[j], array[j-1]

            rect1 = pygame.Rect(CELL_SIZE*(j), 0, CELL_SIZE, HEIGHT)
            rect2 = pygame.Rect(CELL_SIZE*(j+1), 0, CELL_SIZE, HEIGHT)

            window.fill(BLACK, rect1)
            window.fill(BLACK, rect2)

            pygame.display.flip()

            n_rect1 = pygame.Rect(CELL_SIZE*(j), 0, CELL_SIZE, (CELL_SIZE*array[j-1]))
            n_rect2 = pygame.Rect(CELL_SIZE*(j+1), 0, CELL_SIZE, (CELL_SIZE*array[j]))

            pygame.draw.rect(window, WHITE, n_rect1)
            pygame.draw.rect(window, WHITE, n_rect2)

            pygame.display.flip()

            pygame.time.delay(1)

            j -= 1

        i += 1
    
    draw_data_set(array, GREEN)

def draw_merge(array, l, m, r):
    ...

def draw_merge_sort(array, l, r):
    ...

def ending_animation(array, color):
    n = len(array)

    for i in range(n):
        # 100% useless, it's just to keep the os responsive
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                exit()

        rect = pygame.Rect((CELL_SIZE*(i+1), 0, CELL_SIZE, CELL_SIZE*array[i]))
        pygame.draw.rect(window, color, rect)
        pygame.display.flip()
        pygame.time.delay(10)
    draw_data_set(array)


def show_sorting_data(array, sort="b"):
    match sort:
        case "b":
            draw_bubble_sort(array)
        case "i":
            draw_insertion_sort(array)
        case "m":
            draw_merge_sort(array)


run = True
first_itr = False
sort_type = "b"
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                draw_data_set(arr)
                show_sorting_data(arr, sort_type)
                ending_animation(arr, BLUE)
                
            elif event.key == pygame.K_r:
                window.fill(BLACK)
                pygame.display.flip()
                arr = generate_random_array(ARRAY_LENGTH)
                draw_data_set(arr)
            
            elif event.key == pygame.K_b:
                sort_type = "b"
            elif event.key == pygame.K_i:
                sort_type = "i"
            elif event.key == pygame.K_m:
                sort_type = "m"
                

    if not first_itr:
        first_itr = True
        arr = generate_random_array(ARRAY_LENGTH)
        draw_data_set(arr)
