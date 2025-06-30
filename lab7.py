import pygame
import datetime
import math
import os
import sys

# ------------------------ RABBIT CLOCK ------------------------ #
def run_rabbit_clock():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Rabbit Clock")
    clock = pygame.time.Clock()

    CENTER_X = 400
    CENTER_Y = 300
    MINUTE_HAND_LENGTH = 100
    SECOND_HAND_LENGTH = 130

    PINK = (255, 192, 203)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)

    running = True
    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw rabbit face
        pygame.draw.circle(screen, PINK, (CENTER_X, CENTER_Y), 100)
        pygame.draw.ellipse(screen, PINK, (CENTER_X - 80, CENTER_Y - 180, 30, 90))
        pygame.draw.ellipse(screen, PINK, (CENTER_X + 50, CENTER_Y - 180, 30, 90))
        pygame.draw.circle(screen, BLACK, (CENTER_X - 30, CENTER_Y - 20), 8)
        pygame.draw.circle(screen, BLACK, (CENTER_X + 30, CENTER_Y - 20), 8)
        pygame.draw.polygon(screen, RED, [(CENTER_X, CENTER_Y), (CENTER_X - 10, CENTER_Y + 10), (CENTER_X + 10, CENTER_Y + 10)])

        # Clock hands
        now = datetime.datetime.now()
        minute_angle = math.radians(90 - (now.minute * 6))
        second_angle = math.radians(90 - (now.second * 6))

        min_x = CENTER_X + MINUTE_HAND_LENGTH * math.cos(minute_angle)
        min_y = CENTER_Y - MINUTE_HAND_LENGTH * math.sin(minute_angle)
        sec_x = CENTER_X + SECOND_HAND_LENGTH * math.cos(second_angle)
        sec_y = CENTER_Y - SECOND_HAND_LENGTH * math.sin(second_angle)

        pygame.draw.line(screen, BLUE, (CENTER_X, CENTER_Y), (min_x, min_y), 6)
        pygame.draw.line(screen, RED, (CENTER_X, CENTER_Y), (sec_x, sec_y), 3)
        pygame.draw.circle(screen, BLACK, (CENTER_X, CENTER_Y), 5)

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

# ------------------------ MUSIC PLAYER ------------------------ #
def run_music_player():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Music Player")

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    font = pygame.font.SysFont("Arial", 30)
    clock = pygame.time.Clock()

    songs = ["song1.mp3", "song2.mp3", "song3.mp3"]
    current = 0

    def play(index):
        if os.path.exists(songs[index]):
            pygame.mixer.music.load(songs[index])
            pygame.mixer.music.play()
        else:
            print(f"{songs[index]} not found!")

    play(current)
    running = True
    while running:
        screen.fill(WHITE)
        title = font.render(f"Playing: {songs[current]}", True, BLACK)
        screen.blit(title, (30, 50))
        instructions = font.render("P=Play  S=Stop  N=Next  B=Back", True, BLACK)
        screen.blit(instructions, (30, 100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pygame.mixer.music.unpause()
                elif event.key == pygame.K_s:
                    pygame.mixer.music.pause()
                elif event.key == pygame.K_n:
                    current = (current + 1) % len(songs)
                    play(current)
                elif event.key == pygame.K_b:
                    current = (current - 1) % len(songs)
                    play(current)

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

# ------------------------ BALL GAME ------------------------ #
def run_ball_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Red Ball Movement")
    clock = pygame.time.Clock()

    RED = (255, 0, 0)
    WHITE = (255, 255, 255)
    x = 400
    y = 300
    r = 25
    speed = 20

    running = True
    while running:
        screen.fill(WHITE)
        pygame.draw.circle(screen, RED, (x, y), r)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x - r - speed >= 0:
            x -= speed
        if keys[pygame.K_RIGHT] and x + r + speed <= 800:
            x += speed
        if keys[pygame.K_UP] and y - r - speed >= 0:
            y -= speed
        if keys[pygame.K_DOWN] and y + r + speed <= 600:
            y += speed

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

# ------------------------ MAIN MENU ------------------------ #
def main():
    print("\n🎮 Choose an option:")
    print("1 - Rabbit Clock")
    print("2 - Music Player")
    print("3 - Red Ball Movement Game")
    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        run_rabbit_clock()
    elif choice == "2":
        run_music_player()
    elif choice == "3":
        run_ball_game()
    else:
        print("Invalid choice. Exiting.")
        sys.exit()

if __name__ == "__main__":
    main()
