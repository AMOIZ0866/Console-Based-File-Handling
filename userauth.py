import json
from os import system
from cryptography.fernet import Fernet
from passlib.hash import sha256_crypt

class UserAuth:
    def __init__(self):
        self.customer_pin = ""
        self.attempts = 0
        self.customer_acc = 0
        self.account_status = ""
        self.account_limit = 0
        self.customer_cnic = ""
        self.customer_name = ""
        self.customer_balance = 0
        self.all_details = {}
        self.new_userlist = {}
        self.old_userlist = {}


    def user_authentication(self, pin):
        self.customer_pin = pin
        try:
            f = open("Accountfile.txt", "r")
            raw_data = f.read()

            if raw_data != "":
                self.all_details = json.loads(raw_data)

                # loop for getting details
                for person in self.all_details:
                    # list of new users
                    if self.all_details[person]['customer_pin'] == "0000":
                        self.new_userlist[self.all_details[person]['customer_acc']] = self.all_details[person]
                    # list for old users
                    else:
                        self.old_userlist[self.all_details[person]['customer_acc']] = self.all_details[person]
                # Procedure for the New User
                if self.customer_pin == "0000":
                    print("Welcome! Since You are New User So Please Enter CNIC and Account No for the Confirmation")
                    x = self.new_user_auth()
                    return x
                # Procedure for the old user
                else:
                    x = self.old_user_auth()
                    return x
            else:
                print("Sorry! No Data is Avaliable")
        except Exception as e:
            print(e)

    # function for the procedure of new user
    def new_user_auth(self):
        while self.attempts != 3:
            self.customer_cnic = str(input("Enter Your CNIC: "))
            self.customer_acc = str(input("Enter Your Account No: "))

            # verifying the cnic and account
            for users in self.new_userlist:
                if self.new_userlist[users]['customer_cnic'] == self.customer_cnic and self.new_userlist[users]['customer_acc'] == self.customer_acc:
                    self.customer_name = self.new_userlist[users]['customer_name']
                    self.customer_balance = self.new_userlist[users]['customer_bal']
                    self.account_status = self.new_userlist[users]['acc_status']
                    self.account_limit = self.new_userlist[users]['account_limit']

                    #   check the status of account
                    if self.account_status == "Active":
                        print(f"Welcome! {self.customer_name} ")
                        print("Please Set The New Pin To Continue Further ")
                        self.attempts = 3
                        return "New"
                        break
                    else:
                        print("Sorry Your Account is Freeze by Admin. Kindly Contact with Admin")
                        self.attempts = 3
                        return "F"
                        break
                else:
                    pass

            system('clear')
            print("Invalid Information")
            self.attempts += 1

    #  function for the old user
    def old_user_auth(self):
        self.attempts = 0
        while self.attempts != 3:
            # verifying the pin
            for users in self.old_userlist:
                pin = bytes(self.old_userlist[users]['customer_pin'], 'utf-8')
                key = bytes(self.old_userlist[users]['key'], 'utf-8')
                fernet = Fernet(key)
                dec_message = fernet.decrypt(pin).decode()
                if dec_message == self.customer_pin:
                    self.customer_name = self.old_userlist[users]['customer_name']
                    self.customer_acc = self.old_userlist[users]['customer_acc']
                    self.customer_cnic = self.old_userlist[users]['customer_cnic']
                    self.customer_balance = self.old_userlist[users]['customer_bal']
                    self.account_status = self.old_userlist[users]['acc_status']
                    self.account_limit = self.old_userlist[users]['account_limit']
                    #   check the status of account
                    if self.account_status == "Active":
                        print(f"Welcome Back! {self.customer_name} ")
                        self.attempts = 3
                        return "OK"
                        break
                    else:
                        print("Sorry Your Account is Freeze by Admin. Kindly Contact with Admin")
                        self.attempts = 3
                        return "F"
                        break
                else:
                    pass

            # system('clear')
            print("Invalid Information")
            self.attempts += 1
            self.customer_pin = str(input("Enter Your Pin Again: "))