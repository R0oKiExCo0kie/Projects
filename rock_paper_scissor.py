import random
u_w=0
c_w=0
options=['rock','paper','scissors']
while True:
    user=int(input("Enter 1.Rock 2.Paper 3.Scissor 0.Quit \nEnter your Choice: "))
    if user==0:
        quit()
    if user==1:
        comp=random.choice(options)
        print(f"Computer Chose {comp}\n")
        if comp=="rock":
            print("Its a tie")
        elif comp=='paper':
            print("you Lose!")
            c_w+=1
        else:
            print("You Win!")
            u_w+=1
        print()
    elif user==2:
        comp=random.choice(options)
        print(f"Computer Chose {comp}\n")
        if comp=="rock":
            print("You Win!")
            u_w+=1
        elif comp=='paper':
            print("Its a Tie!")
        else:
            print("You Lose!")
            c_w+=1
        print()
    elif user==3:
        comp=random.choice(options)
        print(f"Computer Chose {comp}\n")
        if comp=="rock":
            print("you Lose!")
            c_w+=1
        elif comp=='paper':
            print("You Win!")
            u_w+=1
        else:
            print("Its A tie!")
        print()