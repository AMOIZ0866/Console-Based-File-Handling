## Console Based File Handling in Python.
## Setup Project

1. Clone the project using following command
```
git clone https://github.com/AMOIZ0866/Console-Based-File-Handling.git
```

2. Make sure you have python 3 installed in your system



## Run Test Cases
- User Panel:
  If the user is new he/she will enter 0000 as pin then it will ask the cnic number and account number from the user for confrimation of account and ask user to   
  update the pin(Pin is encrypted by using the from cryptography.fernet package)user can also perform all the functions in the main.

- Admin Panel:
  Admin can create account with unique name and cnic (it will autotamically alot 0000 pin to user)Admin can check the details and perfroms further fucntion 
  mentioned in the menu

## Git Branching Structure
- Default latest branch is **Staging**
- Dev branching naming structure is based on **Jira Ticket No**.
- Every task branch finally merged in Staging upon completion/review.
- **Hot Fix** branches are merged directly in staging upon lead approval.

## How to deploy new changes
- Create a new branch from **Staging** branch
- Update the codebase according to the change-set required
- Create a **Pull Request** with **Staging** branch
- Review & Merge that PR
