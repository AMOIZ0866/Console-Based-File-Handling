# task1
# python_task
in this task we have made a cli based atm machine there are two major modeules of this system:
1. User Panel
2. Admin Panel

On the start of program it requries pin 
=> To access the admin panel you have to enter '****'
=> To access user panel enter the pin 

Admin Panel:
Admin can create account with unique name and cnic (it will autotamically alot 0000 pin to user)
Admin can check the details and perfroms further fucntion mentioned in the menu

User Panel:
 if the user is new he/she will enter 0000 as pin then it will ask the cnic number and account number from the user for confrimation of account and ask user to update the pin
 (Pin is encrypted by using the from cryptography.fernet package)
 user can also perform all the functions in the main
