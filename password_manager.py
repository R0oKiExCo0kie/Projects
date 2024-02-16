from cryptography.fernet import fernet
print("             PASSWORD MANAGER")
passwd=input("Enter The Master Password:")


def list_pass():
    with open('passwords.txt','r') as file:
        for line in file.readlines():
            data=line.rstrip()
            name,passwd=data.split(" ")
            print(f"Name {name} , Password {passwd}")
def add_pass():
    name=input("Account Name:")
    pwd=input("Password: ")
    with open('passwords.txt','a') as file:
        file.write(f"{name} {pwd}\n")

while True:
    mode=int(input("Enter 1.List Password 2.Add New Password\nEnter your Choice: "))
    if mode==1:
        list_pass()
    elif mode==2:
        add_pass()
    else:
        print("invalid Mode")
        print()
        continue