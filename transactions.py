import json


class Transactions:
    def __init__(self):
        self.all_transaction = {}
        self.trans_details = {}
        self.details = {}

    def user_update_amount(self, customer_acc, customer_balance):
        try:
            f = open("Accountfile.txt", "r+")
            raw_data = f.read()
            self.details = json.loads(raw_data)

            # implementing changes made by the user
            self.details[str(customer_acc)]['customer_bal'] = customer_balance

            # implementation on file
            f.read()
            f.seek(0)
            f.write(json.dumps(self.details))
            f.truncate()
            return True
        except:
            print("Data is not Available")
            return False

    # function for the user transactions
    def user_transactions(self, customer_acc, customer_name, cash, customer_balance, customer_action, date):
        try:

            # fetching file
            f = open("Transactions.txt", "r+")
            raw_data = f.read()
            if raw_data != "":

                self.all_transaction = json.loads(raw_data)
                # loop getting accounts form transaction file
                for key, value in self.all_transaction.items():
                    if str(key) == str(customer_acc):
                        self.trans_details = value
                dummy = {'customer_name': customer_name, 'cash': cash, 'customer_balance': customer_balance,
                         'customer_action': customer_action, 'date': date}
                self.trans_details[date] = dummy
                # print(self.trans_details)
                self.all_transaction[str(customer_acc)] = self.trans_details
                f.seek(0)
                f.write(json.dumps(self.all_transaction))
                f.truncate()
                f.close()
                return True
            # in a case if the file is empty
            else:
                dummy = {'customer_name': customer_name, 'cash': cash, 'customer_balance': customer_balance,
                         'customer_action': customer_action, 'date': date}
                self.trans_details[date] = dummy
                self.all_transaction[customer_acc] = self.trans_details
                f.write(json.dumps(self.all_transaction))
                f.close()
                return True

        # in case if the file is not found
        except FileNotFoundError:
            f = open("Transactions.txt", "a")
            dummy = {'customer_name': customer_name, 'cash': cash, 'customer_balance': customer_balance,
                     'customer_action': customer_action, 'date': date}
            self.trans_details[date] = dummy
            self.all_transaction[customer_acc] = self.trans_details
            f.write(json.dumps(self.all_transaction))
            f.close()
            return True
