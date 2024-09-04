import random

# check out page 203

def getRandomNumber(n):
    return random.randint(0,n)

def checkNumber(guess,hidden):
    if (guess==hidden):# check if guess is equal to hidden
        return 0
    elif (guess>hidden): # if guess is greater than hidden
        return 1
    else:
        return 2


h = getRandomNumber(20)
print("...")
for j in range(10):
    i = input() # stores something in i
    #print(type(i))
    i = int(i) #converts to an int (number type)
    if (checkNumber(i,h)==0):
        print("You guessed correctly, the number is "+str(h))
        break
    elif (checkNumber(i,h)==1):
        print("Too high")
    else: 
        print("Too low")

if (checkNumber(i,h)==0):
    print("You won.....")
else:
    print("Game Over")