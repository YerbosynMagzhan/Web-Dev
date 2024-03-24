def double_char(str):
    s = ""
    for i in str:
        s += i * 2
    return s

def count_hi(str):
    k = 0
    
    for i in range(len(str) - 1):
        s = str[i: i + 2]
        if s == "hi":
            k +=1
      
    return k

def cat_dog(str):
    k = str.count('cat')
    k2 = str.count("dog")
    
    return k == k2


def count_code(str):
    count = 0
    for i in range(len(str) - 3):
        if str[i:i+2] == 'co' and str[i+3] == 'e':
            count += 1
    return count

def end_other(a, b: str):
    a = a.lower()
    b = b.lower()
    return a.endswith(b) or b.endswith(a)

def xyz_there(str):
    for i in range(len(str) - 2):
        if str[i:i+3] == 'xyz' and (i == 0 or str[i-1] != '.'):
            return True
    return False