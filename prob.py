import random
# import _ as _ 

# exploring returns
# exploring and/ors

# chooser function should return a string with a description of the number choice
# for example "Chose number 1"
def chooser(num):
    rnum = random.randint(1,num)
    return str(rnum)

def main():
    nu = input("___")
    nu = int(nu)
    s = chooser(nu)
    if (s=="4" or s=="13"):
        print("you should choose 5")
    else:
        print("You should pick number "+s)


main()