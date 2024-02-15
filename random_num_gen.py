import random
def main():
    try:
        top=int(input("Enter a Number: "))
        if top<=0:
            print("Enter the Number larger than 0")
            main()
        rand=random.randint(0,top)
        c=0
        chance=0
        while True:
            try:
                answer=int(input("Guess the Number: "))
                chance+=1
                if answer<rand:
                    c+=1
                    print("Your Guessed low")
                elif answer>rand:
                    c+=1
                    print("You guessed High")
                elif answer==rand:
                    print("You guessed it Correctly")
                    print(f"You guessed took {c} chances out {chance} ")
                    break

            except:
                print("Please guess an integer")
                continue
    except:
        print("Please Enter a Integer")

main()