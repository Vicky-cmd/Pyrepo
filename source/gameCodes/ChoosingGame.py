import math

class ChoosingGame:
    def startGame():
        l = 0
        u = int(input("Please Enter an Upper Limit "))

        print("Think of a number between 0 and {0}".format(u))

        instructions = """1. Enter u if the number selected by you is greater than the guessed number
        2. Enter l if the number selected by you is lesser than the guessed number
        3. Enter c if the number selected by you is equal to the guessed number"""
        count=0
        opt = 'n'
        val=1
        while opt!='c' and opt!='q' and val!=0:
            if opt=='l':
                u=val
            elif opt=='u':
                l=val
            else:
                print("*" * 40)
                print(instructions)
                print("*" * 40, "\n")
            count+=1
            val = int(math.ceil((l+u)/2))
            opt = input("Is your number {}? ".format(val))
            
        if opt=='c':
            print("Guessed the number in {} turns".format(count))    

if __name__=="__main__":
    ChoosingGame.startGame()
