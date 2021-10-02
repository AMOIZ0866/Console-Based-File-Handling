import json
import operator
from calendar import monthrange
from datetime import datetime, timedelta, date
from operator import itemgetter
from collections import OrderedDict
from dateutil.relativedelta import relativedelta


class Reports:
    def __init__(self):
        self.all_transaction = {}
        self.trans_details = {}
        self.details = {}

    # function for the user transactions
    def user_print_statement(self, customer_acc):
        try:
            # fetching file
            f = open("Transactions.txt", "r+")
            raw_data = f.read()
            if raw_data != "":
                self.all_transaction = json.loads(raw_data)
                base = datetime.now()
                date_list = [base - timedelta(days=x) for x in range(7)]
                # loop getting accounts form transaction file
                for key, value in self.all_transaction.items():
                    if str(key) == str(customer_acc):
                        self.trans_details = value
                # sorting the user transaction list
                sorted_trans_list = OrderedDict(
                    sorted(self.trans_details.items(), key=lambda x: datetime.strptime(x[0], '%m/%d/%Y %H:%M:%S.%f'),
                           reverse=True))
                print(f"Date\t\tCash\t\tAction")

                # printing sorted transactions
                for d in date_list:
                    for trans in sorted_trans_list:
                        x = datetime.strptime(sorted_trans_list[trans]['date'], '%m/%d/%Y %H:%M:%S.%f')
                        if d.date() == x.date():
                            print(
                                f"{x.date()}\t{sorted_trans_list[trans]['cash']}\t\t{sorted_trans_list[trans]['customer_action']}")
            else:
                print("No Transaction is Found in the Record")

        # in case if the file is not found
        except FileNotFoundError:
            print("No Record is Found! ")

    # function for the user month transaction
    def user_statement(self, customer_acc, search, com):
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
                # sorting the user transaction list
                sorted_trans_list = OrderedDict(
                    sorted(self.trans_details.items(), key=lambda x: datetime.strptime(x[0], '%m/%d/%Y %H:%M:%S.%f'),
                           reverse=True))
                print(f"Date\t\tCash\t\tAction")

                # printing sorted transactions
                for trans in sorted_trans_list:
                    x = datetime.strptime(sorted_trans_list[trans]['date'], '%m/%d/%Y %H:%M:%S.%f')
                    # if the user select the month search
                    if search.upper == "M":
                        if x.strftime("%b").upper() == com.upper():
                            print(
                                f"{x.date()}\t{sorted_trans_list[trans]['cash']}\t\t{sorted_trans_list[trans]['customer_action']}")
                    # if the user select the year search
                    elif search.upper() == "Y":
                        if x.strftime("%Y").upper() == com.upper():
                            print(
                                f"{x.date()}\t{sorted_trans_list[trans]['cash']}\t\t{sorted_trans_list[trans]['customer_action']}")
            else:
                print("No Transaction is Found in the Record")
                # in case if the file is not found
        except FileNotFoundError:
            print("No Record is Found! ")

    # function for the admin month/year transaction
    def admin_user_statement(self, user_type, search, com):
        dummy = {}
        try:
            # fetching file
            f = open("Transactions.txt", "r+")
            raw_data = f.read()
            if raw_data != "":
                self.all_transaction = json.loads(raw_data)

                # loop getting accounts form transaction file
                if user_type.upper() == "A":
                    for key, trans in self.all_transaction.items():
                        dummy = trans
                        for value in dummy:
                            self.trans_details[value] = dummy[value]
                else:
                    customer_acc = input("Customer Account No: ")
                    for key, value in self.all_transaction.items():
                        if str(key) == str(customer_acc):
                            self.trans_details = value

                # sorting the user transaction list
                sorted_trans_list = OrderedDict(
                    sorted(self.trans_details.items(), key=lambda x: datetime.strptime(x[0], '%m/%d/%Y %H:%M:%S.%f'),
                           reverse=True))
                print(f"Date\t\t\tCash\t\tAction\t\tUSER NAME")

                # # printing sorted transactions
                for trans in sorted_trans_list:
                    x = datetime.strptime(sorted_trans_list[trans]['date'], '%m/%d/%Y %H:%M:%S.%f')
                    # if the admin select the month search
                    if search.upper == "M":
                        if x.strftime("%b").upper() == com.upper():
                            print(
                                f"{x.date()}\t\t{sorted_trans_list[trans]['cash']}\t\t{sorted_trans_list[trans]['customer_action']}\t\t{sorted_trans_list[trans]['customer_name']}")
                    # if the admin select year search
                    elif search.upper() == "Y":
                        if x.strftime("%Y").upper() == com.upper():
                            print(
                                f"{x.date()}\t\t{sorted_trans_list[trans]['cash']}\t\t{sorted_trans_list[trans]['customer_action']}\t\t{sorted_trans_list[trans]['customer_name']}")
            else:
                print("No Transaction is Found in the Record")
        # in case if the file is not found
        except FileNotFoundError:
            print("No Record is Found! ")

    # function for the admin month/year transaction
    def admin_reports(self):
        try:
            # fetching file
            f = open("Transactions.txt", "r+")
            raw_data = f.read()
            if raw_data != "":
                self.all_transaction = json.loads(raw_data)
                # loop getting accounts form transaction file
                base = datetime.now()
                date_list = [base - timedelta(days=x) for x in range(7)]
                for key, trans in self.all_transaction.items():
                    dummy = trans
                    for value in dummy:
                        self.trans_details[value] = dummy[value]
                sorted_trans_list = OrderedDict(
                    sorted(self.trans_details.items(), key=lambda x: datetime.strptime(x[0], '%m/%d/%Y %H:%M:%S.%f'),
                           reverse=True))
                newlist = {}
                for d in date_list:
                    cashin_total = 0
                    cashout_total = 0
                    for trans in sorted_trans_list:
                        x = datetime.strptime(sorted_trans_list[trans]['date'], '%m/%d/%Y %H:%M:%S.%f')
                        if d.date() == x.date():
                            if sorted_trans_list[trans]['customer_action'] == 'Debit':
                                cashin_total += sorted_trans_list[trans]['cash']
                            else:
                                cashout_total += sorted_trans_list[trans]['cash']
                            dum = {"cash_in": cashin_total, "cash_out": cashout_total}
                            newlist[d.date()] = dum
                print("Date\t\tCash In\t\tCash Out")
                for dat in newlist:
                    print(f"{dat.strftime('%Y/%m/%d')}\t{newlist[dat]['cash_in']}\t\t{newlist[dat]['cash_out']}")
            else:
                print("No Transaction is Found in the Record")
        # in case if the file is not found
        except FileNotFoundError:
            print("No Record is Found! ")

    def admin_reports_m(self):
        try:
            # fetching file
            f = open("Transactions.txt", "r+")
            raw_data = f.read()
            if raw_data != "":
                self.all_transaction = json.loads(raw_data)
                # loop getting accounts form transaction file
                for key, trans in self.all_transaction.items():
                    dummy = trans
                    for value in dummy:
                        self.trans_details[value] = dummy[value]
                sorted_trans_list = OrderedDict(
                    sorted(self.trans_details.items(), key=lambda x: datetime.strptime(x[0], '%m/%d/%Y %H:%M:%S.%f'),
                           reverse=True))
                newlist = {}

                month_name = input("Enter Month Name E.g: Jan,Feb...: ")
                year_name = int(input("Enter the Year E.g 2020, 2021..: "))
                datetime_object = datetime.strptime(month_name, "%b")
                month_number = datetime_object.month
                num_days = monthrange(year_name, month_number)[1]
                sdate = date(year_name, month_number, 1)  # start date
                edate = date(year_name, month_number, num_days)  # end date

                date_list = edate - sdate  # as timedelta

                for d in range(date_list.days + 1):
                    day = sdate + timedelta(days=d)
                    cashin_total = 0
                    cashout_total = 0
                    for trans in sorted_trans_list:
                        x = datetime.strptime(sorted_trans_list[trans]['date'], '%m/%d/%Y %H:%M:%S.%f')
                        if day == x.date():
                            if sorted_trans_list[trans]['customer_action'] == 'Debit':
                                cashin_total += sorted_trans_list[trans]['cash']
                            else:
                                cashout_total += sorted_trans_list[trans]['cash']
                            dum = {"cash_in": cashin_total, "cash_out": cashout_total}
                            newlist[day] = dum
                print("Date\t\tCash In\t\tCash Out")
                for dat in newlist:
                    print(f"{dat.strftime('%Y/%m/%d')}\t{newlist[dat]['cash_in']}\t\t{newlist[dat]['cash_out']}")

            else:
                print("No Transaction is Found in the Record")
        # in case if the file is not found
        except FileNotFoundError:
            print("No Record is Found! ")
        except ValueError:
            print("Please Enter the Correct Month Name E.g: Jan,Feb...")

    def admin_reports_y(self):
        try:
            # fetching file
            f = open("Transactions.txt", "r+")
            raw_data = f.read()
            if raw_data != "":
                self.all_transaction = json.loads(raw_data)
                # loop getting accounts form transaction file
                for key, trans in self.all_transaction.items():
                    dummy = trans
                    for value in dummy:
                        self.trans_details[value] = dummy[value]
                sorted_trans_list = OrderedDict(
                    sorted(self.trans_details.items(), key=lambda x: datetime.strptime(x[0], '%m/%d/%Y %H:%M:%S.%f'),
                           reverse=True))
                newlist = {}
                months_list = ['January', 'February', 'March', 'April', 'May', 'June','July', 'August', 'September', 'October', 'November', 'December']
                year_name = int(input("Enter the Year E.g 2020, 2021..: "))
                for mon in months_list:

                    datetime_object = datetime.strptime(mon, "%B")
                    month_number = datetime_object.month
                    num_days = monthrange(year_name, month_number)[1]
                    sdate = date(year_name, month_number, 1)  # start date
                    edate = date(year_name, month_number, num_days)  # end date
                    date_list = edate - sdate  # as timedelta
                    for d in range(date_list.days + 1):
                        day = sdate + timedelta(days=d)
                        cashin_total = 0
                        cashout_total = 0
                        for trans in sorted_trans_list:
                            x = datetime.strptime(sorted_trans_list[trans]['date'], '%m/%d/%Y %H:%M:%S.%f')
                            if day == x.date():
                                if sorted_trans_list[trans]['customer_action'] == 'Debit':
                                    cashin_total += sorted_trans_list[trans]['cash']
                                else:
                                    cashout_total += sorted_trans_list[trans]['cash']
                                dum = {"cash_in": cashin_total, "cash_out": cashout_total}
                                newlist[mon] = dum
                print("Month\t\tCash In\t\tCash Out")
                # # print(newlist)
                for dat in newlist:
                    print(f"{dat}\t\t{newlist[dat]['cash_in']}\t\t{newlist[dat]['cash_out']}")

            else:
                print("No Transaction is Found in the Record")
        # in case if the file is not found
        except FileNotFoundError:
            print("No Record is Found! ")
        except ValueError:
            print("Please Enter the Correct Month Name E.g: Jan,Feb...")
