def first_last6(nums):
    return nums[len(nums) - 1] == 6 or nums[0] == 6

def same_first_last(nums):
    return len(nums) > 0 and  nums[0] == nums[len(nums) - 1]
  
def make_pi():
    return [3, 1, 4]
  
def common_end(a, b):
    return a[-1] == b[-1] or a[0] == b[0]
 
def sum3(nums):
    return sum(nums)
  
def rotate_left3(nums):
    return [nums[1], nums[2], nums[0]]


def reverse3(nums):
    return [nums[2], nums[1], nums[0]]
  
def max_end3(nums):
    m = max([nums[0], nums[2]])
    return [m, m, m]

def sum2(nums):
    if len(nums) >= 2:
        return nums[0] + nums[1]
    return sum(nums)
  
def middle_way(a, b):
    return [a[1], b[1]]

def make_ends(nums):
    return [nums[0], nums[-1]]

def has23(nums):
    return bool(nums.count(2)) or bool(nums.count(3))
