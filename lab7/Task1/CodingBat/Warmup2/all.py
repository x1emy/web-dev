def string_times(string, n):
    return string * n

def front_times(string, n):
    front = string[:3]
    return front * n

def string_bits(string):
    return string[::2]

def string_splosion(string):
    result = ""
    for i in range(len(string) + 1):
        result += string[:i]
    return result

def last2(string):
    if len(string) < 2:
        return 0
    last2_sub = string[-2:]
    count = 0
    for i in range(len(string) - 2):
        if string[i:i+2] == last2_sub:
            count += 1
    return count

def array_count9(nums):
    return nums.count(9)

def array_front9(nums):
    return 9 in nums[:4]

def array123(nums):
    for i in range(len(nums) - 2):
        if nums[i:i+3] == [1, 2, 3]:
            return True
    return False

def string_match(a, b):
    count = 0
    length = min(len(a), len(b))
    for i in range(length - 1):
        if a[i:i+2] == b[i:i+2]:
            count += 1
    return count

print(string_times('Hi', 2))         # → 'HiHi'
print(string_times('Hi', 3))         # → 'HiHiHi'
print(string_times('Hi', 1))         # → 'Hi'

print(front_times('Chocolate', 2))   # → 'ChoCho'
print(front_times('Chocolate', 3))   # → 'ChoChoCho'
print(front_times('Abc', 3))         # → 'AbcAbcAbc'

print(string_bits('Hello'))          # → 'Hlo'
print(string_bits('Hi'))             # → 'H'
print(string_bits('Heeololeo'))      # → 'Hello'

print(string_splosion('Code'))       # → 'CCoCodCode'
print(string_splosion('abc'))        # → 'aababc'
print(string_splosion('ab'))         # → 'aab'

print(last2('hixxhi'))               # → 1
print(last2('xaxxaxaxx'))            # → 1
print(last2('axxxaaxx'))             # → 2

print(array_count9([1, 2, 9]))       # → 1
print(array_count9([1, 9, 9]))       # → 2
print(array_count9([1, 9, 9, 3, 9])) # → 3

print(array_front9([1, 2, 9, 3, 4])) # → True
print(array_front9([1, 2, 3, 4, 9])) # → False
print(array_front9([1, 2, 3, 4, 5])) # → False

print(array123([1, 1, 2, 3, 1]))     # → True
print(array123([1, 1, 2, 4, 1]))     # → False
print(array123([1, 1, 2, 1, 2, 3]))  # → True

print(string_match('xxcaazz', 'xxbaaz'))  # → 3
print(string_match('abc', 'abc'))         # → 2
print(string_match('abc', 'axc'))         # → 0
