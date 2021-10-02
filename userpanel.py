from cryptography.fernet import Fernet
import userauth as user
from accounts import AccountDetails
from os import system
from transactions import Transactions
from settings import AccountSetting
from reports import Reports
import datetime
from passlib.hash import sha256_crypt

class UserPanel(user.UserAuth):
    def __init__(self, pin):
        self.pin = pin
        super(UserPanel, self).__init__()
        self.acc = AccountDetails()
        self.trans = Transactions()
        self.rep = Reports()
        self.setting = AccountSetting()

    # Authentication of the user
    def check_auth(self):
        stat = self.user_authentication(self.pin)
        print(stat)
        if stat == "New":
            self.change_pin()
            return True
        elif stat == "OK":
            return True
        elif stat == "F":
            return False
        else:
            return False

    # function for changing the pin
    def change_pin(self):
        status = False
        # loop to change the pin
        while status is not True:
            new_pin = str(input("Please Enter New Pin: "))
            conf_pin = str(input("Please Enter Confirm Pin Again: "))

            # verify the pins
            if new_pin == conf_pin:
                key = Fernet.generate_key()
                fernet = Fernet(key)
                password = fernet.encrypt(new_pin.encode())
                response = self.setting.user_update_pin(self.customer_acc, password,key)
                # verifying pin is changed or not
                if response is True:
                    print("Pin is Changed Successfully")
                    status = True
                else:
                    pass
            else:
                print("Your are Entering Different Pins: ")

    # function for the main menu of the user panel
    def user_menu(self):
        res = "a"
        while res != "x":
            print("Press 1 for Deposit amount\nPress 2 for Check amount\nPress 3 for Print Statement")
            print("Press 4 for Transfer amount\nPress 5 to WithDrawAmount\nPress 6 to change the Pin")
            print("Press 7 for Transaction History")
            res = str(input())
            if res == "1":
                self.deposit_money()
            elif res == "2":
                self.check_balance()
            elif res == "3":
                print("Record of Last 7 Days Transactions: ")
                self.rep.user_print_statement(self.customer_acc)
            elif res == "4":
                self.transfer_amount()
            elif res == "5":
                self.with_draw_amount()
            elif res == "6":
                self.change_pin()
            elif res == "7":
                self.user_transaction_history()
            else:
                print("Wrong Input")
            res = input("Press x to Exit\nPress Any key For Further Actions")
            system("clear")

    # function for depositing
    def deposit_money(self):
        deposit_amount = int(input("Enter the Deposit Amount: "))
        self.customer_balance += deposit_amount
        # update the balance from file
        res = self.trans.user_update_amount(self.customer_acc, self.customer_balance)
        # update in the transaction file
        res1 = self.trans.user_transactions(self.customer_acc, self.customer_name, deposit_amount,
                                            self.customer_balance, "Debit",
                                            str(datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S.%f")))
        if res is True and res1 is True:
            print("Cash is Deposit Successfully! ")

        # function to check the user transaction history
    def user_transaction_history(self):
        system("clear")
        cont = True
        while cont is True:
            com = input("Press Y for the Year Search\nPress M for the Monthly Search\n")
            if com.upper() == "M":
                month = input("Enter Month: (E.g: Jan,Feb...):")
                self.rep.user_statement(self.customer_acc, com, month)
            elif com.upper() == "Y":
                year = input("Enter Month: (E.g:2021...): ")
                self.rep.user_statement(self.customer_acc, com, year)
            else:
                print("Wrong Command!")
            com = input("Press 0 to Exit or Any key to Continue Further")
            if com == "0":
                cont = False

    # function for checking balance
    def check_balance(self):
        print(f'Your Current Balance: {self.customer_balance}')

    # function to transfer the amount
    def transfer_amount(self):
        cont = True
        while cont is not False:
            trans_acc = input("Enter the Account No ")

            # function check the account availability and get information
            res, pre_bal = self.acc.check_account_ava(trans_acc)

            if res != "This Account is not Available" and res != "Sorry No Data is Available":
                print(f"Account Holder Name: {res}")
                trans_amu = int(input("Enter the Transfer Amount: "))
                if trans_amu < int(self.account_limit) and trans_amu <= self.customer_balance:

                    # update the account balance of account holder
                    total_amu = trans_amu + pre_bal
                    self.trans.user_update_amount(trans_acc, total_amu)

                    # update the account balance of the user
                    self.customer_balance = self.customer_balance - trans_amu
                    self.trans.user_update_amount(self.customer_acc, self.customer_balance)

                    # update the transaction record of the user
                    self.trans.user_transactions(self.customer_acc, self.customer_name, trans_amu,
                                                 self.customer_balance, "Credit",
                                                 str(datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S.%f")))

                    # update the transaction record of the account holder
                    self.trans.user_transactions(trans_acc, res, trans_amu, total_amu, "Debit",
                                                 str(datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S.%f")))

                    print("Transfer Successfully")
                    cont = False

                elif trans_amu > self.account_limit:
                    print(f"Sorry Transfer limit {self.account_limit}")
                else:
                    print("Insufficient Balance")
            else:
                if res == "This Account is not Available":
                    print("Sorry No Account is available with this Account Number! ")
                else:
                    print("Sorry There is Issue in the Server! ")
                x = input("Enter Any Key to Try Again\nEnter 0 to Exit to Main Menu:\n")
                if x == "0":
                    cont = False

    # function to withdraw the amount
    def with_draw_amount(self):
        res, pre_bal = self.acc.check_account_ava(str(self.customer_acc))
        print(f"Avaliable Balance: {pre_bal}")
        trans_amu = int(input("Enter the With Draw Amount: "))
        if trans_amu <= self.customer_balance:
            # update the account balance of the user
            self.customer_balance = self.customer_balance - trans_amu
            self.trans.user_update_amount(self.customer_acc, self.customer_balance)

            # update the transaction record of the user
            self.trans.user_transactions(self.customer_acc, self.customer_name, trans_amu, self.customer_balance,
                                         "Credit", str(datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S.%f")))
            print("With Draw Successfully")
        else:
            print("Insufficient Balance")

