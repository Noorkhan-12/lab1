import pygame
import random
import sys

# ================================
# === RACER GAME ===
# ================================
def run_racer_game():
    pygame.init()
    WIDTH, HEIGHT = 400, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Racer with Coins")
    clock = pygame.time.Clock()

    GRAY = (50, 50, 50)
    YELLOW = (255, 255, 0)
    BLUE = (0, 0, 255)

    car = pygame.image.load("car.png")
    car = pygame.transform.scale(car, (50, 100))
    car_rect = car.get_rect(center=(WIDTH // 2, HEIGHT - 100))

    coin_radius = 15
    coin_list = []
    coin_spawn_time = 30
    coin_timer = 0
    coin_score = 0

    car_speed = 5
    road_speed = 5
    font = pygame.font.SysFont(None, 36)

    def draw_coin(x, y):
        pygame.draw.circle(screen, YELLOW, (x, y), coin_radius)

    def show_score(score):
        score_text = font.render(f"Coins: {score}", True, BLUE)
        screen.blit(score_text, (WIDTH - 130, 10))

    running = True
    while running:
        clock.tick(60)
        screen.fill(GRAY)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and car_rect.left > 0:
            car_rect.x -= car_speed
        if keys[pygame.K_RIGHT] and car_rect.right < WIDTH:
            car_rect.x += car_speed

        coin_timer += 1
        if coin_timer >= coin_spawn_time:
            coin_timer = 0
            new_coin_x = random.randint(coin_radius, WIDTH - coin_radius)
            coin_list.append([new_coin_x, 0])

        for coin in coin_list[:]:
            coin[1] += road_speed
            draw_coin(coin[0], coin[1])
            if car_rect.collidepoint(coin[0], coin[1]):
                coin_list.remove(coin)
                coin_score += 1
            elif coin[1] > HEIGHT:
                coin_list.remove(coin)

        screen.blit(car, car_rect)
        show_score(coin_score)
        pygame.display.update()


# ================================
# === SNAKE GAME ===
# ================================
def run_snake_game():
    pygame.init()
    BLOCK_SIZE = 20
    WIDTH, HEIGHT = 600, 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake with Levels")
    clock = pygame.time.Clock()

    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    DARK_GRAY = (40, 40, 40)
    font = pygame.font.SysFont(None, 35)

    snake = [(100, 100)]
    direction = (BLOCK_SIZE, 0)
    score = 0
    level = 1
    speed = 10

    def draw_snake():
        for block in snake:
            pygame.draw.rect(screen, GREEN, (*block, BLOCK_SIZE, BLOCK_SIZE))

    def place_food():
        while True:
            x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
            y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
            if (x, y) not in snake:
                return (x, y)

    def draw_score_level():
        text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
        screen.blit(text, (10, 10))

    food = place_food()
    running = True
    while running:
        clock.tick(speed)
        screen.fill(DARK_GRAY)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and direction != (0, BLOCK_SIZE):
            direction = (0, -BLOCK_SIZE)
        if keys[pygame.K_DOWN] and direction != (0, -BLOCK_SIZE):
            direction = (0, BLOCK_SIZE)
        if keys[pygame.K_LEFT] and direction != (BLOCK_SIZE, 0):
            direction = (-BLOCK_SIZE, 0)
        if keys[pygame.K_RIGHT] and direction != (-BLOCK_SIZE, 0):
            direction = (BLOCK_SIZE, 0)

        head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        snake.insert(0, head)

        if (head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT):
            return
        if head in snake[1:]:
            return

        if head == food:
            score += 1
            if score % 4 == 0:
                level += 1
                speed += 2
            food = place_food()
        else:
            snake.pop()

        draw_snake()
        pygame.draw.rect(screen, RED, (*food, BLOCK_SIZE, BLOCK_SIZE))
        draw_score_level()
        pygame.display.update()


# ================================
# === PAINT APP ===
# ================================
def run_paint_app():
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Paint App")
    clock = pygame.time.Clock()

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    colors = [BLACK, (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
    current_color = BLACK

    drawing = False
    last_pos = None
    shape_mode = "free"
    start_pos = None
    radius = 10

    def draw_ui():
        for i, color in enumerate(colors):
            pygame.draw.rect(screen, color, (10 + i*40, 10, 30, 30))
        pygame.draw.rect(screen, (200, 200, 200), (10, 50, 100, 30))
        pygame.draw.rect(screen, (200, 200, 200), (120, 50, 100, 30))
        pygame.draw.rect(screen, (200, 200, 200), (230, 50, 100, 30))
        pygame.draw.rect(screen, (200, 200, 200), (340, 50, 100, 30))

        font = pygame.font.SysFont(None, 24)
        screen.blit(font.render("Free", True, BLACK), (35, 55))
        screen.blit(font.render("Rect", True, BLACK), (145, 55))
        screen.blit(font.render("Circle", True, BLACK), (255, 55))
        screen.blit(font.render("Eraser", True, BLACK), (360, 55))

    screen.fill(WHITE)
    running = True
    while running:
        clock.tick(60)
        draw_ui()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if y < 40:
                    index = (x - 10) // 40
                    if 0 <= index < len(colors):
                        current_color = colors[index]
                        shape_mode = "free"
                elif 50 <= y <= 80:
                    if 10 <= x <= 110:
                        shape_mode = "free"
                    elif 120 <= x <= 220:
                        shape_mode = "rect"
                    elif 230 <= x <= 330:
                        shape_mode = "circle"
                    elif 340 <= x <= 440:
                        shape_mode = "eraser"
                else:
                    drawing = True
                    start_pos = event.pos
                    if shape_mode == "free":
                        last_pos = event.pos

            elif event.type == pygame.MOUSEBUTTONUP:
                if shape_mode in ["rect", "circle"] and drawing:
                    end_pos = event.pos
                    if shape_mode == "rect":
                        x1, y1 = start_pos
                        x2, y2 = end_pos
                        width = x2 - x1
                        height = y2 - y1
                        pygame.draw.rect(screen, current_color, (x1, y1, width, height), 2)
                    elif shape_mode == "circle":
                        x1, y1 = start_pos
                        x2, y2 = end_pos
                        radius = int(((x2 - x1)**2 + (y2 - y1)**2)**0.5)
                        pygame.draw.circle(screen, current_color, start_pos, radius, 2)
                drawing = False
                last_pos = None

            elif event.type == pygame.MOUSEMOTION and drawing:
                if shape_mode == "free":
                    pygame.draw.line(screen, current_color, last_pos, event.pos, radius)
                    last_pos = event.pos
                elif shape_mode == "eraser":
                    pygame.draw.circle(screen, WHITE, event.pos, radius)

        pygame.display.update()


# ================================
# === MAIN SELECTOR MENU ===
# ================================
def main():
    print("🎮 Select a game to play:")
    print("1. Racer with Coins")
    print("2. Snake with Levels")
    print("3. Paint App")
    choice = input("Enter 1, 2, or 3: ").strip()

    if choice == "1":
        run_racer_game()
    elif choice == "2":
        run_snake_game()
    elif choice == "3":
        run_paint_app()
    else:
        print("❌ Invalid choice. Please restart the program.")
        sys.exit()

if __name__ == "__main__":
    main()
