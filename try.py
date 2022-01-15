

def add():
    name = input('Enter field name: ')
    userid = input('Enter user id: ')
    passwd = input('Enter password: ')
    balance = 0.0
    with open('password.txt', 'a') as f:
        f.write(name + ' | ' + userid +
                ' | ' + passwd + ' | '+balance, "\n")


def view():
    print('\nName | Userid | Password')
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            name, userid, password = data.split(' | ')
            print("Name: "+name+" Userid: " +
                  userid+" Password: "+password)


while True:
    opt = input(
        'To add a passsword use "add",\nTo view old password use "view" \n ! q to exit: ').lower()
    if opt == 'q':
        break
    if opt == 'add' or opt == 'a':
        add()
    elif opt == 'view' or opt == 'v':
        view()

    else:
        continue
