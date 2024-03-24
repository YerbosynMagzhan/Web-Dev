def sleep_in(weekday, vacation):
   return not weekday or vacation

def monkey_trouble(a_smile, b_smile):
   return (a_smile and b_smile) or (not a_smile and not b_smile)

def sum_double(a, b):
   return a + b

def diff21(n):
  if n <= 21:
    return 21 - n
  else:
    return (n - 21) * 2
 
def parrot_trouble(talking, hour):
   return (talking and (hour < 7 or hour > 20))

def makes10(a, b):
   return(a == 10 or b == 10 or a+b == 10)

def near_hundred(n):
   return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

def pos_neg(a, b, negative):
   if negative:
      return (a < 0 and b < 0)
   else:
      return ((a < 0 and b > 0) or (a > 0 and b < 0))
   
def not_string(str):
   if len(str) >= 3 and str[:3] == "not":
      return str
   return "not " + str


def missing_char(str, n):
   front = str[:n]
   back = str[n+1:]
   return front + back

def front_back(str):
   if len(str) <= 1:
      return str
   mid = str[1:len(str)-1]
   return str[len(str)-1] + mid + str[0]


def front3(str):
   front_end = 3
   if len(str) < front_end:
      front_end = len(str)
   front = str[:front_end]
   return front + front + front 
  