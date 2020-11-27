def hello_name(name):
  return("Hello " + name + "!")
  
  def make_abba(a, b):
  return(a + b + b + a)
  
  def make_tags(tag, word):
  return("<" + tag + ">" + word + "</" + tag + ">")
  
  def make_out_word(out, word):
  return(out[0:2] + word + out[2] + out[3])

def extra_end(str):
  return(str[-2]+str[-1]+str[-2]+str[-1]+str[-2]+str[-1])
  
  def first_two(str):
  return(str[0:2])
  
 def first_half(str):
  half = len(str)/2
  return(str[0:half])

def without_end(str):
  return(str[1:-1])

def combo_string(a, b):
  if len(a) >= len(b):
    return(b + a + b)
  else:
    return(a + b +a)
    
def non_start(a, b):
  if len(a) == 1:
    aval = ""
  else:
    aval = a[1:-1] + a[-1]
  if len(b) == 1:
    bval = ""
  else:
    bval = b[1:-1] + b[-1]
  return(aval+bval)

def left2(str):
  if len(str) > 2:
    return(str[2:-1] + str[-1] + str[0:2])
  else:
    return(str[0:2])

value = int(input("What is the number you would like to test?: "))
if 0 == (value % 2): 
    print("The number is even")
else:
    print("The number is odd")

humyears = int(input("How many years old is your dog?: "))
dogage = 4*(humyears-2)+21
if (humyears == 1):
    print("Your dog is 10.5 in dog years")
else:
    print("Your dog is " + str(dogage) + " in dog years")

letter = input("input a letter: ").lower()
if letter in ["a", "e", "i", "o", "u"]:
    print("letter is a vowel")
elif letter == "y":
    print("letter is sometimes a vowel")
else:
    print("letter is not a vowel")

sides = int(input("How many sides does your shape have?: "))
if sides == 3:
    print("it's atriangle")
elif sides == 4:
    print("it's a quadrilateral")
elif sides == 5:
    print("it's a pentagon")
elif sides == 6:
    print("it's a hexagon")
elif sides == 7:
    print("it's a heptagon")
elif sides == 8:
    print("it's a octagon")
elif sides == 9:
    print("it's a nonagon")
elif sides == 10:
    print("it's a decagon")           
else:
    print("Error, invalid #")             

month = input("Input a month: ").lower()
if month in ["january", "march", "may", "july", "august"]:
    print("There are 31 days in this month")
elif month in ["april", "june", "september"]:
    print("There are 30 days in this month")
elif month == "february":
    print("There are 28 days in this month, 29 on leap years")
else:
    print("invalid input")

noiselvl = int(input("How many decibels is the sound?: "))
if noiselvl < 10:
    print("invalid, too silent")
elif noiselvl <= 40:
    print("As quiet as a silent room") 
elif noiselvl < 70:
    print("Between quiet room and alarm clock")
elif noiselvl == 70:
    print("As loud as a alarm clock")
elif noiselvl < 106:
    print("Between alarm clock and gas lawnmower")
elif noiselvl == 106:
    print("As loud as a gas lawnmower")
elif noiselvl < 130:
    print("Between gas lawnmower and jackhammer")
elif noiselvl == 130:
    print("As loud as a jackhammer")
elif noiselvl >= 185:
    print("You are dead")
elif noiselvl >= 140:
    print("Louder than a jackhammer")

side1 = int(input("What is the length of side #1 in meters: "))
side2 = int(input("What is the length of side #2 in meters: "))
side3 = int(input("What is the length of side #3 in meters: "))
if (side1 == side2) and (side2 == side3):
    print("It is an equalateral triangle")
elif (side1 == side2) or (side2 == side3) or (side3 == side1):
    print("It is an isosceles triangle")
else:
    print("It is a scalar triangle")

alval = input("What is the alphabetical value for the note?: ").lower()
numval = int(input("What is the octive's numerical value?: "))
if alval == "c":
    basefre = 32.5
elif alval == "d":
    basefre = 36.5
elif alval == "e":
    basefre = 41
elif alval == "f":
    basefre = 43.5
elif alval == "g":
    basefre = 49
elif alval == "a":
    basefre = 55
elif alval == "b":
    basefre = 61.5
else:
    print("Invalid input")
freq = basefre*(2**(numval-1))
print("The note's frequency is around " + str(freq) + "Hz")

freq = int(input("What is the frequency of the note in hertz?: "))
if (freq % 261.63) <= 1 or (261.63 % freq) <= 1:
    print("The note is C4")
elif (freq % 293.66) <= 1 or (293.66 % freq) <= 1:
    print("The note is D4")
elif freq % 329.63 <= 1 or 329.63 % freq <= 1:
    print("The note is E4")
elif freq % 349.23 <= 1 or 349.23 % freq <= 1:
    print("The note is F4")
elif freq % 392 <= 1 or 392 % freq <= 1:
    print("The note is G4")
elif freq % 440 <= 1 or 440 % freq <= 1:
    print("The note is A4")
elif freq % 493.88 <= 1 or 493.88 % freq <= 1:
    print("The note is B4")
else:
    print("Unknown")

prez = input("Input the first initial of the first name then first initial of the last name of the person on your bill: ").lower()
if prez == "gw":
    print("The value of the bill is $1")
elif prez == "tj":
    print("The value of the bill is $2")
elif prez == "al":
    print("The value of the bill is $5")
elif prez == "ah":
    print("The value of the bill is $10")
elif prez == "aj":
    print("The value of the bill is $25")
elif prez == "ug":
    print("The value of the bill is $50")
elif prez == "bf":
    print("The value of the bill is $100")
else:
    print("No bill exists")

mon = input("What month is it?: ").lower()
day = input("What day on the month is it?: ")
if (mon + day) == "january1":
    print("Happy new year!")
elif (mon + day) == "july1":
    print("Happy Canada day!")
elif (mon + day) == "december25":
    print("Merry Christmas!")
else:
    print("No holiday or invalid input")

num = input("What is the y coordinate (intiger)?: ")
alp = input("What is the x coordinate (letter)?: ").lower()
if num in ["1", "3", "5", "7"]:
    trunum = 1
elif num in ["2", "4", "6", "8"]:
    trunum = 2
else:
    print("invalid input")
if alp in ["a", "c", "e", "g"]:
    trualp = 1
if alp in ["b", "d", "f", "h"]:
    trualp = 2
final = trualp*trunum
if final == 2:
    print("The tile is white")
else:
    print("The tile is black")

