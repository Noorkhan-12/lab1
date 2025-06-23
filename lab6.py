import os
import time
import math
import string
from functools import reduce
import operator

# Task 1: List directories and files
def list_directories_and_files():
    user_path = input("Enter a path to list directories and files: ").strip()

    if not os.path.exists(user_path):
        print("The given path does not exist.")
        return

    print("\nDirectories:")
    dirs = [item for item in os.listdir(user_path) if os.path.isdir(os.path.join(user_path, item))]
    print(dirs)

    print("\nFiles:")
    files = [item for item in os.listdir(user_path) if os.path.isfile(os.path.join(user_path, item))]
    print(files)

    print("\nAll contents:")
    print(os.listdir(user_path))


# Task 2: Check file access permissions
def check_access_permissions():
    path = input("Enter the path to check access: ").strip()
    if os.path.exists(path):
        print("✓ Path exists")
        print("✓ Readable" if os.access(path, os.R_OK) else "✗ Not readable")
        print("✓ Writable" if os.access(path, os.W_OK) else "✗ Not writable")
        print("✓ Executable" if os.access(path, os.X_OK) else "✗ Not executable")
    else:
        print("✗ Path does not exist")


# Task 3: Extract directory and filename
def show_directory_and_filename():
    full_path = input("Enter a full file path: ").strip()
    if os.path.exists(full_path):
        print("Directory:", os.path.dirname(full_path))
        print("Filename:", os.path.basename(full_path))
    else:
        print("Invalid path.")


# Task 4: Count lines in a text file
def count_file_lines():
    file_name = input("Enter the filename: ").strip()
    try:
        with open(file_name, 'r') as file:
            lines = sum(1 for _ in file)
        print("Total lines:", lines)
    except FileNotFoundError:
        print("File not found.")


# Task 5: Write a list to a file
def write_list_to_file():
    fruits = ["apple", "banana", "cherry", "date"]
    file_name = input("Enter a filename with .txt extension: ").strip()
    with open(file_name, 'w') as f:
        f.write('\n'.join(fruits))
    print(f"List written to {file_name}")


# Task 6: Create 26 text files (A-Z)
def create_alphabet_files():
    for letter in string.ascii_uppercase:
        with open(f"{letter}.txt", 'w') as f:
            f.write(f"This is the file for letter {letter}")
    print("Created 26 text files (A-Z).")


# Task 7: Copy content from one file to another
def copy_file_content():
    src = input("Source file (.txt): ").strip()
    dest = input("Destination file (.txt): ").strip()
    try:
        with open(src, 'r') as source, open(dest, 'w') as target:
            target.write(source.read())
        print(f"Copied content from {src} to {dest}")
    except FileNotFoundError:
        print("Source file not found.")


# Task 8: Delete a file
def delete_file():
    path = input("Enter the path of the file to delete: ").strip()
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            try:
                os.remove(path)
                print("File deleted successfully.")
            except Exception as e:
                print("Error deleting file:", e)
        else:
            print("No write permission to delete the file.")
    else:
        print("File not found.")


# Task 9: Multiply all numbers in a list
def multiply_list_elements():
    numbers = [2, 3, 4, 5]
    product = reduce(operator.mul, numbers)
    print("Product of list:", product)


# Task 10: Count upper and lower case letters
def count_letter_cases(text):
    upper = sum(1 for c in text if c.isupper())
    lower = sum(1 for c in text if c.islower())
    print("Uppercase:", upper)
    print("Lowercase:", lower)


# Task 11: Check if a string is palindrome
def check_palindrome(text):
    if text == text[::-1]:
        print("✓ It's a palindrome")
    else:
        print("✗ Not a palindrome")


# Task 12: Delayed square root
def delayed_square_root(number, delay_ms):
    time.sleep(delay_ms / 1000)
    print(f"Square root of {number} after {delay_ms} ms is {math.sqrt(number)}")


# Task 13: Check if all elements in a tuple are true
def check_all_true(elements):
    print("All elements true:", all(elements))


# Sample calls (you can comment/uncomment based on your need)
# list_directories_and_files()
# check_access_permissions()
# show_directory_and_filename()
# count_file_lines()
# write_list_to_file()
# create_alphabet_files()
# copy_file_content()
# delete_file()
# multiply_list_elements()
# count_letter_cases("Hello World!")
# check_palindrome("madam")
# delayed_square_root(144, 1500)
# check_all_true((True, 1, "text", 3.14))