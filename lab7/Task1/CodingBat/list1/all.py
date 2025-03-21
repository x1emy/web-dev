def first_last6(nums):
    return nums[0] == 6 or nums[-1] == 6

def same_first_last(nums):
    return len(nums) >= 1 and nums[0] == nums[-1]

def make_pi():
    return [3, 1, 4]

def common_end(a, b):
    return a[0] == b[0] or a[-1] == b[-1]

def sum3(nums):
    return sum(nums)

def rotate_left3(nums):
    return nums[1:] + nums[:1]

def reverse3(nums):
    return nums[::-1]

def max_end3(nums):
    max_value = max(nums[0], nums[-1])
    return [max_value] * 3

def sum2(nums):
    return sum(nums[:2])

def make_ends(nums):
    return [nums[0], nums[-1]]

def has23(nums):
    return 2 in nums or 3 in nums


print(first_last6([1, 2, 6]))       # → True
print(first_last6([6, 1, 2, 3]))    # → True
print(first_last6([13, 6, 1, 2, 3])) # → False

print(same_first_last([1, 2, 3]))   # → False
print(same_first_last([1, 2, 3, 1])) # → True
print(same_first_last([1, 2, 1]))   # → True

print(make_pi())                    # → [3, 1, 4]

print(common_end([1, 2, 3], [7, 3]))  # → True
print(common_end([1, 2, 3], [7, 3, 2]))  # → False
print(common_end([1, 2, 3], [1, 3]))  # → True

print(sum3([1, 2, 3]))              # → 6
print(sum3([5, 11, 2]))             # → 18
print(sum3([7, 0, 0]))              # → 7

print(rotate_left3([1, 2, 3]))      # → [2, 3, 1]
print(rotate_left3([5, 11, 9]))     # → [11, 9, 5]
print(rotate_left3([7, 0, 0]))      # → [0, 0, 7]

print(reverse3([1, 2, 3]))          # → [3, 2, 1]
print(reverse3([5, 11, 9]))         # → [9, 11, 5]
print(reverse3([7, 0, 0]))          # → [0, 0, 7]

print(max_end3([1, 2, 3]))          # → [3, 3, 3]
print(max_end3([11, 5, 9]))         # → [11, 11, 11]
print(max_end3([2, 11, 3]))         # → [3, 3, 3]

print(sum2([1, 2, 3]))              # → 3
print(sum2([1, 1]))                 # → 2
print(sum2([1, 1, 1, 1]))           # → 2

print(make_ends([1, 2, 3]))         # → [1, 3]
print(make_ends([1, 2, 3, 4]))      # → [1, 4]
print(make_ends([7, 4, 6, 2]))      # → [7, 2]

print(has23([2, 5]))                # → True
print(has23([4, 3]))                # → True
print(has23([4, 5]))                # → False
