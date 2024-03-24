def make_bricks(small, big, goal):
    return goal % 5 <= small and goal - (big * 5) <= small

def sum_unique(a, b, c):
    if a == b == c:
        return 0
    elif a == b:
        return c
    elif a == c:
        return b
    elif b == c:
        return a
    else:
        return a + b + c
    
def lucky_sum(a, b, c):
    if a == 13:
        return 0
    elif b == 13:
        return a
    elif c == 13:
        return a + b
    else:
        return a + b + c


def no_teen_sum(a, b, c):
    def fix_teen(n):
        if 13 <= n <= 19 and n not in [15, 16]:
            return 0
        return n
    
    return fix_teen(a) + fix_teen(b) + fix_teen(c)


def round_sum(a, b, c):
    def round10(num):
        if num % 10 >= 5:
            return num + (10 - num % 10)
        else:
            return num - (num % 10)
    
    return round10(a) + round10(b) + round10(c)

def close_far(a, b, c):
    a_b_diff = abs(a - b)
    a_c_diff = abs(a - c)
    b_c_diff = abs(b - c)

    return (
        (a_b_diff <= 1 and a_c_diff >= 2 and b_c_diff >= 2) !=
        (a_c_diff <= 1 and a_b_diff >= 2 and b_c_diff >= 2)
    )

def make_chocolate(small, big, goal):
    big_needed = min(big, goal // 5)
    remaining_goal = goal - (big_needed * 5)
    if small >= remaining_goal:
        return remaining_goal
    return -1
