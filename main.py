import pygame
import random
from enum import Enum

# Define colors
COLORS = {
    "RED": (255, 0, 0),
    "GREEN": (0, 255, 0),
    "BLUE": (0, 0, 255),
    "YELLOW": (255, 255, 0),
    "CYAN": (0, 255, 255),
    "MAGENTA": (255, 0, 255),
    "WHITE": (255, 255, 255),
    "BLACK": (0, 0, 0),
    "GRAY": (128, 128, 128)
}

# Define Enum
class CellType(Enum):
    TYPE1 = 1
    TYPE2 = 2
    TYPE3 = 3

# Map Enums to Colors
ENUM_COLOR_MAP = {
    CellType.TYPE1: COLORS["RED"],
    CellType.TYPE2: COLORS["GREEN"],
    CellType.TYPE3: COLORS["BLUE"]
}

# Grid size
GRID_SIZE = 3
CELL_SIZE = 800 // (GRID_SIZE * GRID_SIZE)  # Size of each small cell
WINDOW_SIZE = 800

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("3x3 Enum Grid")

# Generate a random 3x3 grid of 3x3 enums
grid = [[random.choice(list(CellType)) for _ in range(GRID_SIZE * GRID_SIZE)] for _ in range(GRID_SIZE * GRID_SIZE)]

# Function to draw grid
def draw_grid():
    for row in range(GRID_SIZE * GRID_SIZE):
        for col in range(GRID_SIZE * GRID_SIZE):
            cell_type = grid[row][col]
            color = ENUM_COLOR_MAP[cell_type]
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Draw grid lines
    for i in range(GRID_SIZE * GRID_SIZE + 1):
        thickness = 3 if i % GRID_SIZE == 0 else 1  # Thicker lines for 3x3 sections
        pygame.draw.line(screen, COLORS["BLACK"], (i * CELL_SIZE, 0), (i * CELL_SIZE, WINDOW_SIZE), thickness)
        pygame.draw.line(screen, COLORS["BLACK"], (0, i * CELL_SIZE), (WINDOW_SIZE, i * CELL_SIZE), thickness)

# Main loop
running = True
while running:
    screen.fill(COLORS["WHITE"])
    draw_grid()
    
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()