print("                             ")
print("WELCOME TO ATM")
print("                             ")
accounts = {
    100200101 : ["Likitha", "15-08-2006", 100000, 2806],
    100200102 : ["Abhi", "02-01-2009", 150000, 2010],
    100200103 : ["Sailusha", "07-06-2004", 90000, 3003],
    100200104 : ["Akhila", "04-07-2001", 89000, 1514],
    100200105 : ["Asritha", "23-07-2003", 50000, 9899],
    100200106 : ["Prakyath", "22-07-2004", 65000, 4567],
    100200107 : ["Nikitha", "04-09-2003", 69000, 8754],
    100200108 : ["Saathvika", "01-09-2002", 78500, 3478],
    }
dob_month = {1:"January", 2:"Feb", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}
while True:
    def withdrawal():
        print("--------------------")
        account_number=int(input("Enter your account number please: "))
        if account_number not in accounts:
            print("Account number entered is INVALID")
        else:
            pin=int(input("Enter your PIN number: "))
            if accounts[account_number][-1] == None:
                print("Generate PIN for your account: ")
            else:
                if accounts[account_number][-1] != pin :
                    print("INVALID PIN")
                else:
                    amount=int(input("Enter the amount for Withdrawal: "))
                    if amount > accounts[account_number][-2]:
                        print("Insufficient Balance")
                    else:
                        print("Withdraw Sucessful ")
                        accounts[account_number][-2]-=amount
                        print("Current Balance in account:")
                        print(accounts[account_number][-2])
    def deposit():
        print("--------------------")
        account_number =int(input("Enter your account number: "))
        if account_number not in accounts:
            print("Account number entered is INVALID")
        else:
            amount=int(input("Enter amount for deposit: "))
            accounts[account_number][-2]+=amount
            print("Deposit Sucessful ")
            print("Current Balance in account")
            print(accounts[account_number][-2])
            print("--------------------")
    def pin_generation():
        print("--------------------")
        account_number=int(input("Enter your account number: "))
        if account_number not in accounts:
            print("Account number entered is INVALID")
        else:
            if accounts[account_number][-1]==None:
                pin=int(input("Enter new PIN: "))
                cpin=int(input("Confirm PIN: "))
                if pin != cpin:
                    print("Pin does not match")
                else:
                    accounts[account_number][-1]=pin
                    print("Pin generated sucessfully")
            else:
                print("PIN already exits")
        print("--------------------")          
    def mini_statement():
        print("--------------------")
        account_number=int(input("Enter you account number: "))
        if account_number not in accounts:
            print("Account number entered is INVALID")
        else:
            pin=int(input("Enter your PIN number: "))
            if pin != accounts[account_number][-1]:
                print("INVALID PIN")
            else:
                print(f"Name: {accounts[account_number][0]}")
                print(f"Account Number: {account_number}")
                dob = accounts[account_number][1].split("-")
                date =dob[0]
                month=dob_month[int(dob[1])]
                year=dob[2]
                dob=date + "-" + month + "-" + year
                print(f"Date of Birth: {dob}")
                print(f"Account Balance: {accounts[account_number][-2]}")
        print("--------------------")
    print("--------------------")
    print("Choose your action: ")
    print("1.Withdrawal")
    print("2.Deposit")
    print("3.Pin Generation")
    print("4.Mini Statement")
    print("5.Exit")
    action = int(input("Enter your option number: "))
    print()
    if action == 1:
        withdrawal()
    elif action == 2:
        deposit()
    elif action == 3:
        pin_generation()
    elif action == 4:
        mini_statement()
    else:
        break
