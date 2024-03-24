def count_evens(nums):
    k = 0
    for i in nums:
        if i % 2 == 0:
            k += 1
        
    return k

def big_diff(nums):
    return max(nums) - min(nums)


def centered_average(nums):
    mi = min(nums)
    ma = max(nums)
    
    return (sum(nums) - mi - ma) / (len(nums) - 2 )


def sum13(nums):
    total = 0
    skip_next = False

    for num in nums:
        if num == 13:
            skip_next = True
        elif not skip_next:
            total += num
        else:
            skip_next = False
    
    return total


def sum67(nums):
    total = 0
    ignore_section = False

    for num in nums:
        if num == 6:
            ignore_section = True
        elif ignore_section and num == 7:
            ignore_section = False
        elif not ignore_section:
            total += num

    return total

def has22(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i + 1] == 2:
            return True
        
        
    return False


