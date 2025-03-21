def cigar_party(cigars, is_weekend):
    return cigars >= 40 if is_weekend else 40 <= cigars <= 60

def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0
    if you >= 8 or date >= 8:
        return 2
    return 1

def squirrel_play(temp, is_summer):
    return 60 <= temp <= (100 if is_summer else 90)

def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed -= 5
    if speed <= 60:
        return 0
    elif speed <= 80:
        return 1
    return 2

def sorta_sum(a, b):
    return 20 if 10 <= a + b <= 19 else a + b

def alarm_clock(day, vacation):
    if vacation:
        return "off" if day in [0, 6] else "10:00"
    return "10:00" if day in [0, 6] else "7:00"

def love6(a, b):
    return a == 6 or b == 6 or a + b == 6 or abs(a - b) == 6

def in1to10(n, outside_mode):
    return n <= 1 or n >= 10 if outside_mode else 1 <= n <= 10

def near_ten(num):
    return num % 10 <= 2 or num % 10 >= 8


print(cigar_party(30, False))  # → False
print(cigar_party(50, False))  # → True
print(cigar_party(70, True))   # → True

print(date_fashion(5, 10))  # → 2
print(date_fashion(5, 2))   # → 0
print(date_fashion(5, 5))   # → 1

print(squirrel_play(70, False))  # → True
print(squirrel_play(95, False))  # → False
print(squirrel_play(95, True))   # → True

print(caught_speeding(60, False))  # → 0
print(caught_speeding(65, False))  # → 1
print(caught_speeding(65, True))   # → 0

print(sorta_sum(3, 4))   # → 7
print(sorta_sum(9, 4))   # → 20
print(sorta_sum(10, 11)) # → 21

print(alarm_clock(1, False))  # → '7:00'
print(alarm_clock(5, False))  # → '7:00'
print(alarm_clock(0, False))  # → '10:00'

print(love6(6, 4))  # → True
print(love6(4, 5))  # → False
print(love6(1, 5))  # → True

print(in1to10(5, False))   # → True
print(in1to10(11, False))  # → False
print(in1to10(11, True))   # → True

print(near_ten(12))  # → True
print(near_ten(17))  # → False
print(near_ten(19))  # → True
