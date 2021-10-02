
import accounts as acc
import userauth as auth
import reports as re
import userpanel as user
from adminpanel import AdminPanel
# ad = admin.AccountDetails()
# ad.createaccount()
# ad.checkaccount("Abdul Moiz")

# ad = AdminPanel()
# ad.admin_menu()

# rep = re.Reports()
# rep.admin_reports_y()
# rep.user_print_statement("548269")
# rep.user_monthly_statement("548269", "oct")
print("Welcome!")
pin = str(input("Please Enter Pin to Continue: "))
if pin == "****":
    print("Welcome to Admin Panel")
    ad = AdminPanel()
    ad.admin_menu()
else:
    us = user.UserPanel(pin)
    if us.check_auth():
        us.user_menu()
    else:
        pass


