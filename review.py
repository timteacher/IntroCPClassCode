"""a = int(input())
b = int(input())
c = int(input())"""

# do something if a == 1 and b == 1 and c == 1

# hex - hexadecimal 

# decimal - 0, 1, 2 ,3, 4, 5, 6, 7, 8, 
# 16 = 1 (10) + 6 (1) ==> "16"
# binary - 0, 1
# hexadecimal - 0, 1, 2 ,3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F
# 16 = 1 (16) + 0 (1) ==> "10"
# 17 = 1 (16) + 1 (1) ==> "11"
import random
colors = ["Blue","Green","Red","Yellow","Purple"]
hexcodes = ["060270","7DDA58", "E4080A", "FFDE59", "CC6CE7"]



for i in range(10):
    r = random.randint(0,4)
    #print("Your color is "+ colors[r]+ ", which has a hex code of "+hexcodes[r])
    # string concatenation
cleaningsupplies = ["Clorox Wipes","Bleach","Soap","Windex","Laundry Detergent","Mop Water"]
rooms = ["Bedroom","Bathroom","Kitchen","Study","Window","Laundry"]

#            range(start, stop)
#            range(start, stop, step)
for i in range(0,6,2):
    print("I used {0}, to clean the {1}.".format(cleaningsupplies[i], rooms[i]))
    # string format

# .split()/programming problem/reading code

# problem 1 on page 279


# THE fibonacci sequence starts 1, 1, 2, 3, 5, 8, ... Each number in the sequence
# (after the first two) is the sum of the previous two. Write a program
# that computes and outputs the nth Fibonacci number, where n is a value 
# entered by the user. 
