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
    with open('account.txt', 'a') as f:
        f.write(name + ' | ' + accNum +
                ' | ' + passwd + "\n")
    return accNum


def view():
    with open('account.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            name, accNo, password = data.split(' | ')
            return [name, accNo, password]


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
    name, accNo, passw = data
    print("Hello", name, "\n")
    usAccno = input("Please give your Account No:- ")
    usPassw = input("Please give your Account Password No:- ")
    if accNo == usAccno and passw == usPassw:
        print("Welcome", name, "\n")
    else:
        print("Invalid credintial")
