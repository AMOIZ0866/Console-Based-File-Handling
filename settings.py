import json
from accounts import AccountDetails


class AccountSetting:
    def __init__(self):
        self.acc = AccountDetails()
        self.details = {}

    #   function for the pin update made by the user
    def user_update_pin(self, customer_acc, customer_pin, key):
        try:
            f = open("Accountfile.txt", "r+")
            raw_data = f.read()
            self.details = json.loads(raw_data)
            # implementing changes made by the user
            self.details[str(customer_acc)]['customer_pin'] = str(customer_pin, encoding='utf-8')
            self.details[str(customer_acc)]['key'] = str(key, encoding='utf-8')

            # implementation on file
            f.read()
            f.seek(0)
            f.write(json.dumps(self.details))
            f.truncate()
            return True
        except Exception as e:
            print(e)
            print("Data is not Available")
            return False

    # change the limit of the user account by admin
    def user_update_limit(self):
        customer_acc = input("Enter the Account No: ")
        res,bal = self.acc.check_account_ava(customer_acc)
        if res != "This Account is not Available" and res != "Sorry No Data is Available":
            print(f"Account Holder Name: {res}")
            account_limit = int(input("Enter the New Account Limit: "))
            try:
                f = open("Accountfile.txt", "r+")
                raw_data = f.read()
                self.details = json.loads(raw_data)

                # implementing changes made by the admin
                self.details[str(customer_acc)]['account_limit'] = account_limit
                print("Account Limit has been Updated! ")
                # implementation on file
                f.read()
                f.seek(0)
                f.write(json.dumps(self.details))
                f.truncate()
                return True
            except:
                print("Data is not Available")
                return False
        else:
            if res == "This Account is not Available":
                print("Sorry No Account is available with this Account Number! ")
            else:
                print("Sorry There is Issue in the Server! ")

    # change the limit of the user account by admin
    def user_update_status(self):
        customer_acc = input("Enter the Account No: ")
        res = self.acc.check_account_ava(customer_acc)
        if res != "This Account is not Available" and res != "Sorry No Data is Available":
            print(f"Account Holder Name: {res}")
            acc_status = input("Enter 'F' to Freeze Account Or 'A' to Active Account: ")
            try:
                f = open("Accountfile.txt", "r+")
                raw_data = f.read()
                self.details = json.loads(raw_data)

                # implementing changes made by the admin
                if acc_status.upper() == "F":
                    self.details[str(customer_acc)]['acc_status'] = "Freeze"
                    print("Account is Freeze")
                elif acc_status.upper() == "A":
                    self.details[str(customer_acc)]['acc_status'] = "Active"
                    print("Account is Active")
                else:
                    print("Invalid Command")

                # implementation on file
                f.read()
                f.seek(0)
                f.write(json.dumps(self.details))
                f.truncate()
                return True
            except:
                print("Data is not Available")
                return False
        else:
            if res == "This Account is not Available":
                print("Sorry No Account is available with this Account Number! ")
            else:
                print("Sorry There is Issue in the Server! ")

    # change the limit of the user account by admin
    def del_account(self):
        customer_acc = input("Enter the Account No: ")
        res = self.acc.check_account_ava(customer_acc)
        if res != "This Account is not Available" and res != "Sorry No Data is Available":
            print(f"Account Holder Name: {res}")
            try:
                f = open("Accountfile.txt", "r+")
                raw_data = f.read()
                self.details = json.loads(raw_data)
                del self.details[str(customer_acc)]
                print("Account Has Been Deleted! ")
                # implementation on file
                f.read()
                f.seek(0)
                f.write(json.dumps(self.details))
                f.truncate()
                return True
            except:
                print("Data is not Available")
                return False
        else:
            if res == "This Account is not Available":
                print("Sorry No Account is available with this Account Number! ")
            else:
                print("Sorry There is Issue in the Server! ")
