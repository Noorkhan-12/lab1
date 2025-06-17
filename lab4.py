# 1. Get today's date and the date 5 days ago
from datetime import datetime, timedelta

current_date = datetime.now()
five_days_earlier = current_date - timedelta(days=5)

print("Today:", current_date)
print("5 Days Ago:", five_days_earlier)


# 2. Print yesterday's, today's, and tomorrow's dates
from datetime import date, timedelta

today = date.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)


# 3. Remove microseconds from current datetime
from datetime import datetime

now = datetime.now()
without_microseconds = now.replace(microsecond=0)

print("With Microseconds:", now)
print("Without Microseconds:", without_microseconds)


# 4. Find the difference between two datetime objects in seconds
from datetime import datetime

dt1 = datetime(2025, 6, 13, 12, 0, 0)
dt2 = datetime(2025, 6, 12, 10, 0, 0)
time_difference = dt1 - dt2
seconds_diff = time_difference.total_seconds()

print("Difference in Seconds:", seconds_diff)

# 1. Generate square numbers up to n
def square_generator(n):
    for i in range(n + 1):
        yield i ** 2

for num in square_generator(5):
    print(num, end=" ")
print()


# 2. Generate even numbers up to n
def even_numbers_up_to(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

limit = int(input("Enter a number: "))
evens = list(even_numbers_up_to(limit))
print("Even numbers:", ", ".join(map(str, evens)))


# 3. Numbers divisible by both 3 and 4 up to n
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

for num in divisible_by_3_and_4(50):
    print(num, end=" ")
print()


# 4. Generate squares in a range
def range_squares(start, end):
    for i in range(start, end + 1):
        yield i ** 2

for val in range_squares(3, 7):
    print(val)


# 5. Countdown from n to 0
def countdown_from(n):
    while n >= 0:
        yield n
        n -= 1

for num in countdown_from(5):
    print(num, end=" ")
print()