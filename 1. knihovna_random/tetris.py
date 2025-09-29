import pygame
import random

# Game constants
WIDTH, HEIGHT = 300, 600
BLOCK_SIZE = 30
COLUMNS, ROWS = WIDTH // BLOCK_SIZE, HEIGHT // BLOCK_SIZE

# Tetromino shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 0, 0], [1, 1, 1]],  # J
    [[0, 0, 1], [1, 1, 1]],  # L
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]],  # Z
]
COLORS = [(0,255,255),(255,255,0),(128,0,128),(0,0,255),(255,165,0),(0,255,0),(255,0,0)]

def rotate(shape):
    return [list(row) for row in zip(*shape[::-1])]

def collide(board, shape, offset):
    off_x, off_y = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                if x + off_x < 0 or x + off_x >= COLUMNS or y + off_y >= ROWS:
                    return True
                if y + off_y >= 0 and board[y + off_y][x + off_x]:
                    return True
    return False

def merge(board, shape, offset, color_idx):
    off_x, off_y = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell and y + off_y >= 0:
                board[y + off_y][x + off_x] = color_idx + 1

def clear_rows(board):
    new_board = [row for row in board if any(cell == 0 for cell in row)]
    cleared = ROWS - len(new_board)
    for _ in range(cleared):
        new_board.insert(0, [0]*COLUMNS)
    return new_board, cleared

def draw_board(screen, board):
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, COLORS[cell-1], (x*BLOCK_SIZE, y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                pygame.draw.rect(screen, (50,50,50), (x*BLOCK_SIZE, y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

def draw_shape(screen, shape, offset, color_idx):
    off_x, off_y = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell and y + off_y >= 0:
                pygame.draw.rect(screen, COLORS[color_idx], ((x+off_x)*BLOCK_SIZE, (y+off_y)*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                pygame.draw.rect(screen, (50,50,50), ((x+off_x)*BLOCK_SIZE, (y+off_y)*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()
    board = [[0]*COLUMNS for _ in range(ROWS)]
    score = 0

    shape_idx = random.randint(0, len(SHAPES)-1)
    shape = SHAPES[shape_idx]
    color_idx = shape_idx
    offset = [COLUMNS//2 - len(shape[0])//2, -2]

    fall_time = 0
    fall_speed = 500

    running = True
    while running:
        dt = clock.tick(60)
        fall_time += dt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    new_offset = [offset[0]-1, offset[1]]
                    if not collide(board, shape, new_offset):
                        offset = new_offset
                elif event.key == pygame.K_RIGHT:
                    new_offset = [offset[0]+1, offset[1]]
                    if not collide(board, shape, new_offset):
                        offset = new_offset
                elif event.key == pygame.K_DOWN:
                    new_offset = [offset[0], offset[1]+1]
                    if not collide(board, shape, new_offset):
                        offset = new_offset
                elif event.key == pygame.K_UP:
                    new_shape = rotate(shape)
                    if not collide(board, new_shape, offset):
                        shape = new_shape

        if fall_time > fall_speed:
            fall_time = 0
            new_offset = [offset[0], offset[1]+1]
            if not collide(board, shape, new_offset):
                offset = new_offset
            else:
                merge(board, shape, offset, color_idx)
                board, cleared = clear_rows(board)
                score += cleared * 100
                shape_idx = random.randint(0, len(SHAPES)-1)
                shape = SHAPES[shape_idx]
                color_idx = shape_idx
                offset = [COLUMNS//2 - len(shape[0])//2, -2]
                if collide(board, shape, offset):
                    running = False

        screen.fill((0,0,0))
        draw_board(screen, board)
        draw_shape(screen, shape, offset, color_idx)
        font = pygame.font.SysFont("Arial", 24)
        score_text = font.render(f"Score: {score}", True, (255,255,255))
        screen.blit(score_text, (10,10))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()