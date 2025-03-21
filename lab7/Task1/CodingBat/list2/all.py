def count_evens(nums):
    return sum(1 for num in nums if num % 2 == 0)

def big_diff(nums):
    return max(nums) - min(nums)

def centered_average(nums):
    nums.sort()
    return sum(nums[1:-1]) // (len(nums) - 2)

def sum13(nums):
    total, skip = 0, False
    for num in nums:
        if num == 13:
            skip = True
            continue
        if skip:
            skip = False
            continue
        total += num
    return total

def sum67(nums):
    total, skip = 0, False
    for num in nums:
        if num == 6:
            skip = True
        elif num == 7 and skip:
            skip = False
        elif not skip:
            total += num
    return total

def has22(nums):
    return any(nums[i] == 2 and nums[i+1] == 2 for i in range(len(nums) - 1))

# Тесты

print(count_evens([2, 1, 2, 3, 4]))  # → 3
print(count_evens([2, 2, 0]))        # → 3
print(count_evens([1, 3, 5]))        # → 0

print(big_diff([10, 3, 5, 6]))  # → 7
print(big_diff([7, 2, 10, 9]))  # → 8
print(big_diff([2, 10, 7, 2]))  # → 8

print(centered_average([1, 2, 3, 4, 100]))        # → 3
print(centered_average([1, 1, 5, 5, 10, 8, 7]))  # → 5
print(centered_average([-10, -4, -2, -4, -2, 0]))  # → -3

print(sum13([1, 2, 2, 1]))  # → 6
print(sum13([1, 1]))        # → 2
print(sum13([1, 2, 2, 1, 13]))  # → 6

print(sum67([1, 2, 2]))                  # → 5
print(sum67([1, 2, 2, 6, 99, 99, 7]))    # → 5
print(sum67([1, 1, 6, 7, 2]))            # → 4

print(has22([1, 2, 2]))  # → True
print(has22([1, 2, 1, 2]))  # → False
print(has22([2, 1, 2]))  # → False
