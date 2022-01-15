import os.path
import random


def genAcc():
    accNo = "13303"
    strng = "0123456789"
    i = 0
    while i <= 4:
        i += 1
        rand = random.randrange(0, len(strng)-1)
        accNo += strng[rand]
    return accNo


def add():
    name = input('Enter Your name:- ')
    accNum = genAcc()
    passwd = input('Enter password:- ')
    balance = 0.0
    try:
        balance = float(input("Give your first deposite:- "))
    except:
        print("invalid input")
        balance = float(input("Give your first deposite:- "))

    balance = str(balance)
    with open('account.txt', 'a') as f:
        f.write(name + ' | ' + accNum +
                ' | ' + passwd+' | '+balance)
    return accNum


def view():
    with open('account.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            name, accNo, password, balance = data.split(' | ')
            return [name, accNo, password, balance]


def upAcc(name, accNum, passwd, balance):
    balance = str(balance)
    with open('account.txt', 'w') as f:
        f.write(name + ' | ' + accNum +
                ' | ' + passwd+' | '+balance)


file_exists = os.path.exists('account.txt')
# print(file_exists)

if file_exists == False:
    print("You did not have any account  here")
    tmp = input("To create an account enter add and q to exit:- ")
    if tmp.lower() == "a" or tmp.lower() == "add":
        accNo = add()
        print("Your Account is created \nYour account No:-",
              accNo, "\n\tPlease save it")
    else:
        exit()
if file_exists == True:
    data = view()
    name, accNo, passw, balance = data
    balance = float(balance)
    print("Hello", name, "\n")
    usAccno = input("Please give your Account No:- ")
    usPassw = input("Please give your Account Password No:- ")
    if accNo == usAccno and passw == usPassw:
        print("Welcome", name, "\n")
        while True:
            opt = input(
                "1.Check Balance \n2.Withdrawl \n3.Deposite \n4.Exit  \nEnter Your Choice:- ")
            if opt == "1":
                print("\n\tYour balance is :-", balance, "₹")
            elif opt == "2":
                mon = float(
                    input("Enter the Amount You want to Withdrawl::- "))
                if mon > 0:
                    if balance > mon:
                        balance = balance-mon
                        upAcc(name, accNo, passw, balance)
                    else:
                        print("\n\tnot enough money ")
                else:
                    print("Please Enter in positive....!!!! ")
            elif opt == "3":
                mon = float(
                    input("Enter the Amount You want to Deposite::- "))
                if mon > 0:
                    if balance > mon:
                        balance = balance+mon
                        upAcc(name, accNo, passw, balance)
            elif opt == "4":
                break
            else:
                print("Wrong input")

    else:
        print("Invalid credintial")
        exit()
