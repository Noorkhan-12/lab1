import re

# Match a string that has an 'a' followed by zero or more 'b's
def match_a_followed_by_b(s):
    pattern = r"a(b*)"
    return re.fullmatch(pattern, s) is not None

print(match_a_followed_by_b("a"))        # True
print(match_a_followed_by_b("ab"))       # True
print(match_a_followed_by_b("abb"))      # True
print(match_a_followed_by_b("ac"))       # False

# Match a string that has an 'a' followed by two to three 'b's
def match_a_followed_by_two_to_three_b(s):
    pattern = r"ab{2,3}"
    return re.fullmatch(pattern, s) is not None

print(match_a_followed_by_two_to_three_b("abb"))    # True
print(match_a_followed_by_two_to_three_b("abbb"))   # True
print(match_a_followed_by_two_to_three_b("abbbb"))  # False

# Match a string that has an 'a' followed by anything and ends with 'b'
def match_a_followed_by_anything_ending_in_b(s):
    pattern = r"a.*b$"
    return re.fullmatch(pattern, s) is not None

print(match_a_followed_by_anything_ending_in_b("a quick brown fox jumps over the lazy dog b"))  # True
print(match_a_followed_by_anything_ending_in_b("a quick brown fox"))  # False

# Find sequences of lowercase letters joined with an underscore
def find_lowercase_with_underscore(s):
    pattern = r"[a-z]+(_[a-z]+)+"
    return re.findall(pattern, s)

print(find_lowercase_with_underscore("hello_world_this_is_python"))  # ['hello_world', 'world_this', 'this_is']

# Find sequences of uppercase letter followed by lowercase letters
def find_uppercase_followed_by_lowercase(s):
    pattern = r"[A-Z][a-z]+"
    return re.findall(pattern, s)

print(find_uppercase_followed_by_lowercase("Hello World"))  # ['Hello', 'World']

# Replace all occurrences of space, comma, or dot with a colon
def replace_with_colon(s):
    return re.sub(r"[ ,\.]", ":", s)

print(replace_with_colon("Hello, world. How are you?"))  # Hello:world:How:are:you?

# Split a string at uppercase letters
def split_at_uppercase(s):
    return re.findall(r'[A-Z][^A-Z]*', s)

print(split_at_uppercase("HelloWorldThisIsPython"))  # ['Hello', 'World', 'This', 'Is', 'Python']

# Insert spaces between words starting with a capital letter
def insert_spaces_between_capitals(s):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', s)

print(insert_spaces_between_capitals("HelloWorldThisIsPython"))  # Hello World This Is Python

# Convert a snake case string to camel case
def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

print(snake_to_camel("hello_world"))  # helloWorld

# Convert a given camel case string to snake case
def camel_to_snake(camel_str):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower()

print(camel_to_snake("HelloWorld"))  # hello_world