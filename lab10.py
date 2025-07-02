import sqlite3
import csv
import pygame
import sys
import random

# =========================
# == DATABASE FUNCTIONS ==
# =========================

def init_db():
    conn = sqlite3.connect("game.db")
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS PhoneBook (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    phone TEXT NOT NULL)''')

    c.execute('''CREATE TABLE IF NOT EXISTS Users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    level INTEGER DEFAULT 1)''')

    c.execute('''CREATE TABLE IF NOT EXISTS UserScores (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    score INTEGER,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES Users(id))''')

    conn.commit()
    conn.close()

# =======================
# == PHONEBOOK SYSTEM ==
# =======================

def insert_from_csv(filename):
    conn = sqlite3.connect("game.db")
    c = conn.cursor()
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            c.execute("INSERT OR IGNORE INTO PhoneBook (username, phone) VALUES (?, ?)",
                      (row['username'], row['phone']))
    conn.commit()
    conn.close()

def insert_manual():
    conn = sqlite3.connect("game.db")
    c = conn.cursor()
    username = input("Enter username: ")
    phone = input("Enter phone number: ")
    c.execute("INSERT OR IGNORE INTO PhoneBook (username, phone) VALUES (?, ?)", (username, phone))
    conn.commit()
    conn.close()

def update_phonebook(username, new_username=None, new_phone=None):
    conn = sqlite3.connect("game.db")
    c = conn.cursor()
    if new_username:
        c.execute("UPDATE PhoneBook SET username = ? WHERE username = ?", (new_username, username))
    if new_phone:
        c.execute("UPDATE PhoneBook SET phone = ? WHERE username = ?", (new_phone, username))
    conn.commit()
    conn.close()

def query_phonebook(filter_column=None, value=None):
    conn = sqlite3.connect("game.db")
    c = conn.cursor()
    if filter_column and value:
        c.execute(f"SELECT * FROM PhoneBook WHERE {filter_column} LIKE ?", ('%' + value + '%',))
    else:
        c.execute("SELECT * FROM PhoneBook")
    for row in c.fetchall():
        print(row)
    conn.close()

def delete_entry_by_username(username):
    conn = sqlite3.connect("game.db")
    c = conn.cursor()
    c.execute("DELETE FROM PhoneBook WHERE username = ?", (username,))
    conn.commit()
    conn.close()

def delete_entry_by_phone(phone):
    conn = sqlite3.connect("game.db")
    c = conn.cursor()
    c.execute("DELETE FROM PhoneBook WHERE phone = ?", (phone,))
    conn.commit()
    conn.close()

# ======================
# == USER & GAME DATA ==
# ======================

def get_or_create_user(username):
    conn = sqlite3.connect("game.db")
    c = conn.cursor()
    c.execute("SELECT id, level FROM Users WHERE username = ?", (username,))
    row = c.fetchone()
    if row:
        print(f"Welcome back {username}, you're on level {row[1]}")
        return row[0], row[1]
    else:
        c.execute("INSERT INTO Users (username) VALUES (?)", (username,))
        conn.commit()
        return c.lastrowid, 1

def save_score(user_id, score):
    conn = sqlite3.connect("game.db")
    c = conn.cursor()
    c.execute("INSERT INTO UserScores (user_id, score) VALUES (?, ?)", (user_id, score))
    conn.commit()
    conn.close()

# ===================
# == SNAKE GAME ====
# ===================

def run_snake_game(user_id, level):
    pygame.init()
    WIDTH, HEIGHT = 600, 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)

    snake = [(100, 100)]
    direction = (20, 0)
    food = (random.randint(0, WIDTH//20-1)*20, random.randint(0, HEIGHT//20-1)*20)
    score = 0
    paused = False
    speed = 10 + level * 2

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_score(user_id, score)
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP: direction = (0, -20)
                elif event.key == pygame.K_DOWN: direction = (0, 20)
                elif event.key == pygame.K_LEFT: direction = (-20, 0)
                elif event.key == pygame.K_RIGHT: direction = (20, 0)
                elif event.key == pygame.K_p:
                    paused = not paused
                    if paused:
                        print("Paused. Saving score...")
                        save_score(user_id, score)

        if paused:
            continue

        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

        if new_head in snake or new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
            print("Game Over!")
            save_score(user_id, score)
            break

        snake = [new_head] + snake[:-1]
        if new_head == food:
            snake.append(snake[-1])
            score += 10
            food = (random.randint(0, WIDTH//20-1)*20, random.randint(0, HEIGHT//20-1)*20)

        screen.fill((0, 0, 0))
        for segment in snake:
            pygame.draw.rect(screen, (0, 255, 0), (*segment, 20, 20))
        pygame.draw.rect(screen, (255, 0, 0), (*food, 20, 20))

        text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(speed)

# ===================
# == MAIN MENU =====
# ===================

def main_menu():
    init_db()
    while True:
        print("\n1. Manage PhoneBook\n2. Start Snake Game\n3. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            print("\n1. Insert from CSV\n2. Insert manually\n3. Update\n4. Query\n5. Delete by username\n6. Delete by phone")
            op = input("Select operation: ")
            if op == '1':
                insert_from_csv("phonebook.csv")
            elif op == '2':
                insert_manual()
            elif op == '3':
                u = input("Username to update: ")
                new_u = input("New username (or leave blank): ")
                new_p = input("New phone (or leave blank): ")
                update_phonebook(u, new_u if new_u else None, new_p if new_p else None)
            elif op == '4':
                col = input("Filter by (username/phone or blank): ")
                val = input("Enter value to filter: ") if col else None
                query_phonebook(col if col else None, val)
            elif op == '5':
                delete_entry_by_username(input("Enter username to delete: "))
            elif op == '6':
                delete_entry_by_phone(input("Enter phone to delete: "))
        elif choice == '2':
            uname = input("Enter your username: ")
            uid, level = get_or_create_user(uname)
            run_snake_game(uid, level)
        elif choice == '3':
            break

if __name__ == "__main__":
    main_menu()
