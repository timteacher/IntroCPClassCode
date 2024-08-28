
'''
Happy birthday to you!
Happy birthday to you!
Happy birthday, dear <insert-name>. 
Happy birthday to you!
'''

def happy():
    print("Happy birthday to you!")

def main(name):
    happy()
    happy()
    print("Happy birthday, dear "+name)
    happy()



n = input("What is your name?")
main(n)