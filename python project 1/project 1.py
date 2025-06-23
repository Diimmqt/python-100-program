import pygame
import random

# Inisialisasi pygame
pygame.init()

# Ukuran layar
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

# Warna
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)  # Warna hijau untuk ular dan makanan
DARK_GREEN = (0, 200, 0)  # Warna hijau tua untuk latar belakang
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Font untuk skor
font = pygame.font.Font(None, 36)

# Setup layar
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Kecepatan permainan
clock = pygame.time.Clock()
speed = 10

# Fungsi untuk posisi makanan secara acak
def random_position():
    return [random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE, 
            random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE]

# Inisialisasi ular dan makanan
snake = [[100, 100]]
direction = "RIGHT"
food = random_position()
score = 0  # Inisialisasi skor

# Loop utama game
running = True
while running:
    screen.fill(DARK_GREEN)  # Mengubah latar belakang menjadi hijau tua

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_s and direction != "UP":
                direction = "DOWN"
            elif event.key == pygame.K_a and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_d and direction != "LEFT":
                direction = "RIGHT"

    # Update posisi ular
    head = snake[0][:]
    if direction == "UP":
        head[1] -= CELL_SIZE
    elif direction == "DOWN":
        head[1] += CELL_SIZE
    elif direction == "LEFT":
        head[0] -= CELL_SIZE
    elif direction == "RIGHT":
        head[0] += CELL_SIZE

    # Cek tabrakan dengan dinding atau tubuh sendiri
    if head in snake or head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        running = False

    # Tambahkan kepala baru ke ular
    snake.insert(0, head)

    # Cek apakah ular makan makanan
    if head == food:
        food = random_position()
        score += 10  # Tambah skor
    else:
        snake.pop()  # Hapus ekor jika tidak makan

    # Gambar makanan
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))

    # Gambar ular
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

    # Tampilkan skor di layar
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(speed)

# Game Over Screen
screen.fill(DARK_GREEN)
game_over_text = font.render(f"Game Over! Final Score: {score}", True, WHITE)
screen.blit(game_over_text, (WIDTH // 4, HEIGHT // 2))
pygame.display.flip()
pygame.time.delay(3000)  # Tampilkan selama 3 detik sebelum keluar

pygame.quit()
