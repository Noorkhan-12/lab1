import pygame
import sys
import random
import math

# ---------------- RACER GAME ----------------
def run_racer_game():
    pygame.init()  # Initialize Pygame

    # Set window size and caption
    WIDTH, HEIGHT = 400, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Racer Game")

    # Set up clock and font
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 20)

    # Define colors
    WHITE = (255, 255, 255)
    RED = (200, 0, 0)
    BLACK = (0, 0, 0)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)

    # Player car settings
    player = pygame.Rect(175, 500, 50, 70)
    player_speed = 5

    # Enemy car settings
    enemy = pygame.Rect(random.randint(0, 350), 0, 50, 70)
    enemy_speed = 3

    # Coin setup
    coins = []
    coin_timer = 0
    coin_spawn_delay = 30
    coin_weights = [1, 2, 3]
    score = 0

    running = True
    while running:
        screen.fill(WHITE)  # Clear screen each frame

        # Quit game if user closes window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Move car with arrow keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.left > 0:
            player.x -= player_speed
        if keys[pygame.K_RIGHT] and player.right < WIDTH:
            player.x += player_speed

        # Draw car with rounded corners and wheels
        pygame.draw.rect(screen, RED, player, border_radius=10)
        pygame.draw.circle(screen, BLACK, (player.left + 10, player.bottom), 7)
        pygame.draw.circle(screen, BLACK, (player.right - 10, player.bottom), 7)

        # Move enemy car
        pygame.draw.rect(screen, BLACK, enemy)
        enemy.y += enemy_speed
        if enemy.top > HEIGHT:
            enemy = pygame.Rect(random.randint(0, 350), 0, 50, 70)

        # Spawn coins every few frames
        coin_timer += 1
        if coin_timer >= coin_spawn_delay:
            coin_timer = 0
            coin_x = random.randint(20, WIDTH - 20)
            coins.append({"x": coin_x, "y": 0, "weight": random.choice(coin_weights)})

        # Move coins and check collision with car
        for coin in coins[:]:
            coin["y"] += 4
            pygame.draw.circle(screen, YELLOW, (coin["x"], coin["y"]), 10)
            if player.collidepoint(coin["x"], coin["y"]):
                score += coin["weight"]
                coins.remove(coin)
            elif coin["y"] > HEIGHT:
                coins.remove(coin)

        # Show score
        text = font.render(f"Score: {score}", True, GREEN)
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

# ---------------- SNAKE GAME ----------------
def run_snake_game():
    pygame.init()

    WIDTH, HEIGHT = 600, 600
    CELL_SIZE = 20
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 20)

    # Define colors
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    YELLOW = (255, 255, 0)
    WHITE = (255, 255, 255)

    snake = [(100, 100)]  # Initial snake body
    snake_dir = (CELL_SIZE, 0)  # Moving right
    foods = []
    food_weights = [1, 2, 3]
    food_lifetime = 50
    score = 0

    # Food placement function
    def spawn_food():
        x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        weight = random.choice(food_weights)
        foods.append({"pos": (x, y), "weight": weight, "timer": food_lifetime})

    spawn_food()
    running = True
    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Handle direction input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and snake_dir != (0, CELL_SIZE):
            snake_dir = (0, -CELL_SIZE)
        if keys[pygame.K_DOWN] and snake_dir != (0, -CELL_SIZE):
            snake_dir = (0, CELL_SIZE)
        if keys[pygame.K_LEFT] and snake_dir != (CELL_SIZE, 0):
            snake_dir = (-CELL_SIZE, 0)
        if keys[pygame.K_RIGHT] and snake_dir != (-CELL_SIZE, 0):
            snake_dir = (CELL_SIZE, 0)

        # Move the snake
        head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
        snake.insert(0, head)

        # Check for wall or self-collision
        if not (0 <= head[0] < WIDTH and 0 <= head[1] < HEIGHT) or head in snake[1:]:
            return

        # Check for food collision
        eaten = False
        for food in foods[:]:
            if head == food["pos"]:
                score += food["weight"]
                foods.remove(food)
                spawn_food()
                eaten = True
                break
        if not eaten:
            snake.pop()

        # Draw food and update timers
        for food in foods[:]:
            pygame.draw.circle(screen, YELLOW, (food["pos"][0] + CELL_SIZE // 2, food["pos"][1] + CELL_SIZE // 2), CELL_SIZE // 2)
            food["timer"] -= 1
            if food["timer"] <= 0:
                foods.remove(food)
                spawn_food()

        # Draw snake as green circles
        for part in snake:
            pygame.draw.circle(screen, GREEN, (part[0] + CELL_SIZE // 2, part[1] + CELL_SIZE // 2), CELL_SIZE // 2)

        # Show score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(10)

# ---------------- PAINT APP ----------------
def run_paint_app():
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Paint App")
    clock = pygame.time.Clock()

    # Colors and font
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (100, 100, 255)
    font = pygame.font.SysFont("Arial", 20)

    drawing = False
    start_pos = None
    shape = "square"  # Default shape

    # Draw a square
    def draw_square(surf, start, end):
        size = max(abs(end[0] - start[0]), abs(end[1] - start[1]))
        rect = pygame.Rect(start[0], start[1], size, size)
        rect.normalize()
        pygame.draw.rect(surf, BLUE, rect, 2)

    # Draw right triangle
    def draw_right_triangle(surf, start, end):
        points = [start, (start[0], end[1]), end]
        pygame.draw.polygon(surf, BLUE, points, 2)

    # Draw equilateral triangle
    def draw_equilateral_triangle(surf, start, end):
        x1, y1 = start
        x2, y2 = end
        angle = math.radians(60)
        dx, dy = x2 - x1, y2 - y1
        x3 = x1 + dx * math.cos(angle) - dy * math.sin(angle)
        y3 = y1 + dx * math.sin(angle) + dy * math.cos(angle)
        pygame.draw.polygon(surf, BLUE, [start, end, (int(x3), int(y3))], 2)

    screen.fill(WHITE)
    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                start_pos = event.pos
                drawing = True
            elif event.type == pygame.MOUSEBUTTONUP and drawing:
                end_pos = event.pos
                if shape == "square":
                    draw_square(screen, start_pos, end_pos)
                elif shape == "right_triangle":
                    draw_right_triangle(screen, start_pos, end_pos)
                elif shape == "equilateral_triangle":
                    draw_equilateral_triangle(screen, start_pos, end_pos)
                drawing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    shape = "square"
                elif event.key == pygame.K_2:
                    shape = "right_triangle"
                elif event.key == pygame.K_3:
                    shape = "equilateral_triangle"

        pygame.display.flip()

# ---------------- MAIN MENU ----------------
def main():
    print("Choose a game to play:")
    print("1 - Racer Game")
    print("2 - Snake Game")
    print("3 - Paint App")
    choice = input("Enter number (1/2/3): ")

    if choice == "1":
        run_racer_game()
    elif choice == "2":
        run_snake_game()
    elif choice == "3":
        run_paint_app()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
