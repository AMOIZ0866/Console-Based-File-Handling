import json
import random
from os import system


class AccountDetails:
    def __init__(self):
        self.customer_name = ""
        self.customer_cnic = ""
        self.customer_acc = str(random.randint(00000000, 1111111))
        self.customer_pin = "0000"
        self.account_status = "Active"
        self.customer_balance = 0
        self.account_limit = 0
        self.details = {}

    #
    def generate_account_number(self):
        self.customer_acc = str(random.randint(00000000, 1111111))

    # function to enter accounts details
    def add_account_details(self):
        self.customer_name = input("Enter Customer Name: ")
        self.customer_cnic = (input("Enter the CNIC: "))
        self.account_limit = int(input("Enter the Account Limit: "))

    # function to create new account by admin
    def create_account(self):
        self.customer_acc = str(random.randint(00000000, 1111111))
        system('clear')
        self.details = {}
        create_account = False
        account_check = True
        self.add_account_details()
        try:

            # fetching file
            f = open("Accountfile.txt", "r+")
            raw_data = f.read()
            if raw_data != "":
                self.details = json.loads(raw_data)
                while create_account is False:

                    # verifying the unique name and Cnic
                    if self.details.get('customer_name') == self.customer_name:
                        print("Customer Name is Already Used! Please Enter the Unique Customer Name ")
                        self.addaccountdetails()
                    elif self.details.get('customer_cnic') == self.customer_cnic:
                        print("CNIC is Already Used! ")
                        self.addaccountdetails()


                    else:

                        # implementing the new user data
                        det = {"customer_name": self.customer_name, "customer_cnic": self.customer_cnic,
                               "customer_acc": self.customer_acc, "customer_pin": self.customer_pin,
                               "acc_status": self.account_status, "account_limit": self.account_limit,
                               "customer_bal": self.customer_balance}
                        self.details[self.customer_acc] = det
                        f = open("Accountfile.txt", "r+")
                        f.read()
                        f.seek(0)
                        f.write(json.dumps(self.details))
                        f.truncate()
                        print("Account Created !")
                        f.close()
                        create_account = True

            # in case if the file is empty
            else:
                det = {"customer_name": self.customer_name, "customer_cnic": self.customer_cnic,
                       "customer_acc": self.customer_acc, "customer_pin": self.customer_pin,
                       "acc_status": self.account_status, "account_limit": self.account_limit,
                       "customer_bal": self.customer_balance}
                self.details[self.customer_acc] = det
                f.write(json.dumps(self.details))
                f.close()
                print("Account Created !")

        # in case if the file is not found
        except FileNotFoundError:
            f = open("Accountfile.txt", "a")
            det = {"customer_name": self.customer_name, "customer_cnic": self.customer_cnic,
                   "customer_acc": self.customer_acc, "customer_pin": self.customer_pin,
                   "acc_status": self.account_status, "account_limit": self.account_limit,
                   "customer_bal": self.customer_balance}
            self.details[self.customer_acc] = det
            f.write(json.dumps(self.details))
            print("Account Created !")

    # function of the admin panel to check the user details
    def check_account(self):
        account_ava = False
        try:
            f = open("Accountfile.txt", "r")
            raw_data = f.read()
            if raw_data != "":
                self.details = json.loads(raw_data)
                while account_ava is False:
                    system("clear")
                    # search on the base of account number or name
                    self.customer_acc = input("Enter The Account No ")
                    if self.details.get(self.customer_acc):
                        x = self.details.get(self.customer_acc)
                        print(f"Customer Name: {x['customer_name']}")
                        print(f"Account No: {x['customer_acc']}")
                        print(f"CNIC: {x['customer_cnic']}")
                        print(f"Status: {x['acc_status']}")
                        print(f"Account Limit: {x['account_limit']}")
                        print(f"Account Balance: {x['customer_bal']}")

                    else:
                        print('No Customer is Found')
                    request = input('Press Any Key to Search Again\nPress 0 to Main Menu.\n')
                    if request == "0":
                        account_ava = True
            else:
                print("Sorry No Data is Available")

        except FileNotFoundError:
            print("Sorry No File is Available")

    # function to check the availability of Account
    def check_account_ava(self, customer_acc):
        try:
            f = open("Accountfile.txt", "r")
            raw_data = f.read()
            if raw_data != "":
                self.details = json.loads(raw_data)
                # search on the base of account number or name
                if self.details.get(customer_acc):
                    x = self.details.get(customer_acc)
                    return x['customer_name'], x['customer_bal']
                else:
                    return "This Account is not Available", 0
            else:
                return "Sorry No Data is Available", 0

        except FileNotFoundError:
            return "Sorry No Data is Available", 0
