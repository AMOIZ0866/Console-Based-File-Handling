import userauth as user
from accounts import AccountDetails
from os import system
from transactions import Transactions
from settings import AccountSetting
from reports import Reports
import datetime


class AdminPanel:
    def __init__(self):
        self.acc = AccountDetails()
        self.trans = Transactions()
        self.setting = AccountSetting()
        self.rep = Reports()

    # function for the main menu of the admin panel
    def admin_menu(self):
        res = "a"
        while res != "x":
            print("Press 1 To Create New Account\nPress 2 To Check Details\nPress 3 To Check Transactions")
            print("Press 4 To Freeze/Active Account\nPress 5 To Delete Account\nPress 6 To Set Transaction Limit")
            print("Press 7 for Reports")
            res = str(input())
            if res == "1":
                self.acc.create_account()
            elif res == "2":
                self.acc.check_account()
            elif res == "3":
                self.user_reporting()
            elif res == "4":
                self.setting.user_update_status()
            elif res == "5":
                self.setting.del_account()
            elif res == "6":
                self.setting.user_update_limit()
            elif res == "7":
                com = input("Enter the 'W' for Last Week Search OR 'M' For the Month Search OR 'Y' For the Year Search")
                if com.upper() == 'W':
                    self.rep.admin_reports()
                elif com.upper() == 'M':
                    self.rep.admin_reports_m()
                elif com.upper() == 'Y':
                    self.rep.admin_reports_y()
                else:
                    print("Wrong Command! ")

            else:
                print("Wrong Input")
            res = input("Press x to Exit\nPress Any key For Further Actions")
            system("clear")

    def user_reporting(self):
        cont = True
        while cont is True:
            user_type = input("Press A to Search All Users\nPress S to Search Single User\n")
            com = input("Press Y for the Year Search\nPress M for the Monthly Search\n")
            if com.upper() == "M":
                month = input("Enter Month: (E.g: Jan,Feb...):")
                self.rep.admin_user_statement(user_type, com, month)
            elif com.upper() == "Y":
                year = input("Enter Month: (E.g:2021...): ")
                self.rep.admin_user_statement(user_type, com, year)
            else:
                print("Wrong Command!")
            com = input("Press 0 to Exit or Any key to Continue Further")
            if com == "0":
                cont = False
