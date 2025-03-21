def make_bricks(small, big, goal):
    return goal % 5 <= small and goal - min(goal // 5, big) * 5 <= small

def lone_sum(a, b, c):
    return sum(x for x in [a, b, c] if [a, b, c].count(x) == 1)

def lucky_sum(a, b, c):
    for x in [a, b, c]:
        if x == 13:
            return sum(n for n in [a, b, c] if n != x and [a, b, c].index(n) < [a, b, c].index(x))
    return a + b + c

def fix_teen(n):
    return 0 if 13 <= n <= 19 and n not in [15, 16] else n

def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

def round10(num):
    return (num + 5) // 10 * 10

def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)

def close_far(a, b, c):
    return (abs(a - b) <= 1 and abs(a - c) >= 2 and abs(b - c) >= 2) or \
           (abs(a - c) <= 1 and abs(a - b) >= 2 and abs(b - c) >= 2)

def make_chocolate(small, big, goal):
    max_big = min(goal // 5, big)
    remainder = goal - max_big * 5
    return remainder if remainder <= small else -1



print(make_bricks(3, 1, 8))  # → True
print(make_bricks(3, 1, 9))  # → False
print(make_bricks(3, 2, 10)) # → True

print(lone_sum(1, 2, 3))  # → 6
print(lone_sum(3, 2, 3))  # → 2
print(lone_sum(3, 3, 3))  # → 0

print(lucky_sum(1, 2, 3))  # → 6
print(lucky_sum(1, 2, 13)) # → 3
print(lucky_sum(1, 13, 3)) # → 1

print(no_teen_sum(1, 2, 3))  # → 6
print(no_teen_sum(2, 13, 1)) # → 3
print(no_teen_sum(2, 1, 14)) # → 3

print(round_sum(16, 17, 18)) # → 60
print(round_sum(12, 13, 14)) # → 30
print(round_sum(6, 4, 4))    # → 10

print(close_far(1, 2, 10)) # → True
print(close_far(1, 2, 3))  # → False
print(close_far(4, 1, 3))  # → True

print(make_chocolate(4, 1, 9))  # → 4
print(make_chocolate(4, 1, 10)) # → -1
print(make_chocolate(4, 1, 7))  # → 2
