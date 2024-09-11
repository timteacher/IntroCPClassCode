"""
A person is eligible to be a US senator if they are at least 30 years old 
and have been a US citizen for at least 9 years. To be a US representative 
these numbers are 25 and 7, respectively. Write a program that accepts a 
person's age and years of citizenship as input and outputs their eligibility 
for the Senate and House.
"""

def li(age, cy):
    if (age>=30 and cy>=9):
        # eligible to be a senator (both)
        print("s")
    elif (age>=25 and cy>=7):
        # eligible to be a rep 
        print("r")
    else:
        print("not")

li(3,2)
li(5,2)
li(27,9)
li(31,10)