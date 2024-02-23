
class User:
    starting_acc = 1000
    total_balance = 0
    total_loan = 0
    accounts = {}

    def __init__(self, name, email, address, type):
        self.name = name
        self.email = email
        self.address = address
        self.type = type
        User.starting_acc += 1
        self.acc_no = User.starting_acc
        self.balance = 0
        self.loan_no = 0
        User.accounts[self.acc_no] = self
        self.transaction_history = []


    def deposit(self, amount):
        self.balance += amount
        User.total_balance += amount
        self.transaction_history.append(f"Deposited Tk. {amount}")
        print (f"\nYour A/C No. {self.acc_no} is credited by Tk. {amount}. Your current balance is {self.balance}.")


    def withdraw(self, amount):
        if Admin.is_bankrupt:
            print ("\nsorry, The Bank is bankrupt.")
        elif amount <= self.balance:
            self.balance -= amount
            User.total_balance -= amount
            self.transaction_history.append(f"Withdrawn Tk. {amount}")
            print(f"\nYour A/C No. {self.acc_no} is debited by Tk. {amount}. Your current balance is {self.balance}.")
        else:
            print (f"\nWithdrawal amount exceeded.")


    def check_balance(self):
        print(f"\nYour current balance if Tk. {self.balance}")


    def check_transaction_history(self):
        for transaction in self.transaction_history:
            print(transaction)


    def take_loan (self, amount):
        if Admin.loan_status == True:
            if self.loan_no < 2:
                self.balance += amount
                User.total_loan += amount
                self.loan_no += 1
                self.transaction_history.append(f"Took loan Tk. {amount}")
                print(f"\nLoan request processed successfully. Your current balance is Tk. {self.balance}")

            else:
                print("\nSorry, You can't take loan more than twice.")

        else:
            print("\nSorry, taking loan service is currently unavailable.")
        

    def transfer_amount(self, transferred_acc):
        if Admin.is_bankrupt:
            print("Sorry, the bank is bankrupt.")
        else:
            if transferred_acc in User.accounts:
                amount = int(input(("Enter amount : ")))
                if amount > self.balance:
                    print("\nSorry, insufficient balance.")
                else:
                    self.balance -= amount
                    self.transaction_history.append(f"Transferred TK. {amount} to A/C No. {transferred_acc}.")
                    print(f"\nMoney transferred successful. Your current balance is {self.balance}.")

            else:
                print("\nSorry, received A/C No. is not found.")



class Admin:

    loan_status = True
    is_bankrupt = False

    def create_account(self, name, email, address, type):
        user = User(name, email, address, type)
        User.accounts[user.acc_no] = user
        print(f"\nAccount created successfully.")


    def delete_user_account(self, acc_no):
        if acc_no in User.accounts:
            del User.accounts[acc_no]
            print(f"\nA/C No. {acc_no} is deleted successfully.")
        else:
            print(f"\nA/C No. {acc_no} is no found.")


    def see_users_account(self):
        for account, user in User.accounts.items():
            print(f"\nName : {user.name}, A/C No. : {account}, Email : {user.email}, Address : {user.address}, A/C Type: {user.type}")


    def check_available_balance(self):
        print(f"\nTotal amount of balance is Tk. {User.total_balance}")

    def amount_of_loan(self):
        print(f"\nTotal amount of loan is Tk. {User.total_loan}")

    def loan_option (self, option):
        Admin.loan_status = option
        if option == True:
            print("\nYou have successfully turned on loan option.")
        else:
            print("\nYou have successfully turned off loan option.")

    def bankrupt_option(self, option):
        Admin.is_bankrupt = option
        if option == True:
            print("\nThe bank is bankrupt now.")
        else:
            print("\nThe bank is at service now.")



#--------------------------------------------------------------------------------------------------------------------------#

print('\n')
print("""---------------- Welcome to DBBL ------------------
----------------- Uttara Branch --------------------
      """)

admin = Admin()
while True:
    print("\nPlease select an option : ")
    print("1. Admin")
    print("2. User")
    print("3. Exit")
    
    option = int(input("Your choice : "))

    if option == 1:
        while True:
            print("\nplease select an option : ")
            print("1. create an account")
            print("2. delete an account")
            print("3. view all accounts")
            print("4. check Total available balance")
            print("5. check Total loan amount")
            print("6. Admin option")
            print("7. exit")

            op = int(input("Your choice : "))

            if op == 1:
                name = input("Enter your name : ")
                email = input ("Enter your email : ")
                address = input ("Enter your address : ")
                type = input ("Which types of account do you want to open? Type sv for savings account and cr for current account : ")
                admin.create_account(name, email, address, type)

            elif op == 2:
                acc = int(input("Enter A/C NO. you want to delete : "))
                admin.delete_user_account(acc)

            elif op == 3:
                admin.see_users_account()
            
            elif op == 4:
                admin.check_available_balance()
            
            elif op == 5:
                admin.amount_of_loan()

            elif op == 6:
                while True:
                    print("\nPlease select an option : ")
                    print("1. loan option")
                    print("2. bankrupt option")
                    print("3. exit")

                    opt = int(input("Your choice : "))

                    if opt == 1 :
                        choice = int(input("Type 1 if you want to activate loan option, otherwise type 0 : "))
                        if choice == 1:
                            admin.loan_option(True)
                        elif choice == 0:
                            admin.loan_option(False)
                        else:
                            print("Invalid input.")

                    elif opt == 2:
                        choice = int(input("Type 1 if you want to declare the bank bankrupt, otherwise type 0 : "))
                        if choice == 1:
                            admin.bankrupt_option(True)
                        elif choice == 0:
                            admin.bankrupt_option(False)
                        else:
                            print("Invalid input.")
                    
                    elif opt == 3:
                        break

                    else:
                        print("Invalid Input.")


            elif op == 7:
                break

            else:
                print("invalid Input.")




    elif option == 2:

        while True:
            print("\nplease select an option : ")
            print("1. create an account")
            print("2. deposit money")
            print("3. withdraw money")
            print("4. check available balance")
            print("5. check transaction history")
            print("6. transfer money")
            print("7. take loan")
            print("8. exit")

            op = int(input("Your choice : "))

            if op == 1:
                name = input("Enter your name : ")
                email = input ("Enter your email : ")
                address = input ("Enter your address : ")
                type = input ("Which types of account do you want to open? Type sv for saving account and cr for current account : ")
                user = User (name, email, address, type)
                print(f"\nAccount created successfully. Your A/C No. is {user.acc_no}.")

            elif op == 2:
                amount = int(input("Enter amount : "))
                user.deposit(amount)

            elif op == 3:
                amount = int(input("Enter amount : "))
                user.withdraw(amount)
            
            elif op == 4:
                user.check_balance()
            
            elif op == 5:
                user.check_transaction_history()

            elif op == 6:
                acc = int(input("Enter received A/C No. : "))
                user.transfer_amount(acc)

            elif op == 7:
                amount = int(input("Enter amount : "))
                user.take_loan(amount)

            elif op == 8:
                break

            else:
                print("Invalid Input.")

    elif option == 3:
        break

    else:
        print("Invalid input.")

    



    