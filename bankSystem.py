balance = 0.00


def deposite():
    global balance
    mon = float(input("Enter the Amount You want to Deposite::- "))
    if mon > 0:
        balance = balance+mon
    else:
        print("Please Enter in positive.....!!!!")
        deposite()


def withdrawl():
    global balance
    mon = float(input("Enter the Amount You want to Withdrawl::- "))
    if mon > 0:
        if balance > mon:
            balance = balance-mon
            viewBalance()
        else:
            print("\n\tnot enough money ")
    else:
        print("Please Enter in positive....!!!! ")


def viewBalance():
    global balance
    print("\n\tYour balance is :-", balance, "₹")


def mainFunc():
    try:
        while True:
            opt = input(
                "1.Check Balance \n2.Withdrawl \n3.Deposite \n4.Exit  \nEnter Your Choice:- ")
            if opt == "1":
                viewBalance()
            elif opt == "2":
                withdrawl()
            elif opt == "3":
                deposite()
            elif opt == "4":
                break
            else:
                print("Wrong option\n")

    except:
        print("Invalid input\n")
        mainFunc()


 # Start here
print("\n!!!!-----WELCOME IN OUR PROGRAMME-----!!!!\n")
mainFunc()
print("\n!!!!-----THANK YOU USE AGAIN-----!!!!")
