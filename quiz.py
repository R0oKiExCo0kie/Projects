#Project 1
print("Welcome To The Computer Quiz\n")
def main():
    counter=0
    user=int(input("Enter 1.Play and 2.Exit: "))
    if user==1:
        print("Lets Start")
        answer=input("1.What does CPU stands For:")
        if answer.lower()=="central processing unit":
            print("Thats correct!")
            counter+=1
        else:
            print("Incorrect\n--------------")
        answer=input("2.What does GPU Stands For: ")
        if answer.lower()=='graphics processing unit':
            print("Thats correct!")
            counter+=1
        else:
            print("Incorrect\n--------------")
        answer=input("2.What does RAM Stands For: ")
        if answer.lower()=='random access memory':
            print("Thats correct!")
            counter+=1
        else:
            print("Incorrect\n--------------")        
        print()
        print(f"You answered {counter} out of 3")
        if counter==3:    
            print("Good Job")
        elif counter ==2:
            print('Nice')
        else:
            print("Couldve been Better")
        print()
        main()
    elif user==2:
        print("See ya")
        quit()
    else:
        print("Enter a Valid Choice")
        main()
main()