import time
import smtplib
from datetime import datetime, timedelta, date

today = date.today()


class BankAccount:
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance
        self.transaction = []

    def WithdrawCash(self, user_amount):
        if user_amount > self.balance:
            print('Withdraw amount is more than account balance!!\nRetry again.\n')
        else:
            print('Withdrawing cash...')
            time.sleep(3)
            self.balance -= user_amount
            print(f'Amount successfully withdrawn!.\nYour remaining amount is {self.balance}$\n')
            self.transaction.append(
                f"Amount withdrawn from account {user_amount}$\nRemaining balance in account {self.balance}$")

    def DepositCash(self, user_amount):
        self.balance += user_amount
        print(f'Total amount available is {self.balance}$\n')
        self.transaction.append(
            f"Amount deposited into account {user_amount}$\nUpdated balance in account {self.balance}$")

    def CheckBalance(self):
        print(f'Balance available: {self.balance}$\n')

    def TransactionSummary(self):
        return "\n".join(self.transaction)


def GetEmail(user_mail, user_password, message):
    try:
        smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_obj.starttls()
        smtp_obj.login(user_mail, user_password)

        from_add = user_mail
        to_add = user_mail
        subject = f"Transaction Summary on {today} "
        msg = f"Subject: {subject}\n\n{message}".encode("utf-8")
        smtp_obj.sendmail(from_add, to_add, msg)
        print("Thank you email sent successfully!")
    except Exception as exc:
        print(f"Failed to send email. Error: {exc}")


def user_details():
    user = input("Please state your name: ").strip()
    card_no = input('Enter your card number: ').strip()

    while True:
        try:
            amount = float(input('Enter the total amount of cash you have: '))
            if amount < 0:
                raise ValueError('Amount cannot be in negatives')
            break
        except ValueError as e:
            print(f'Error: {e}')

    account = BankAccount(user, amount)
    print(f'Hello {user}, please choose from the below options.')

    while True:
        print("Please choose from below options.")
        print('1. Withdraw\n2. Deposit\n3. Check Balance\n4. Exit')
        user_choice = int(input())
        if user_choice == 1:
            withdraw_amount = float(input('Enter the amount you want to withdraw: '))
            account.WithdrawCash(withdraw_amount)
        elif user_choice == 2:
            deposit_amount = float(input('Enter the amount of cash you want to deposit: '))
            account.DepositCash(deposit_amount)
        elif user_choice == 3:
            account.CheckBalance()
        elif user_choice == 4:
            print('Thank you for using the service. Hope to see you soon!')
            break
        else:
            print('Invalid option! Please choose from given options only.')

        if user_choice in [1, 2]:
            print('Do You want to get an email?')
            email_option = input('If YES enter Y, if NO then enter N ')
            if email_option == 'y' or email_option == 'Y':
                email = input('Enter your email id: ')
                password = input('Enter your password: ')
                transaction_summary = account.TransactionSummary()
                msg = (
                    f"Dear {user},\n\n"
                    f"Here is your recent transaction summary:\n\n{transaction_summary}\n\n"
                    "Thank you for using Madhu's Banking System!"
                    "Hope to see you soon!!"
                )
                GetEmail(email, password, msg)
            else:
                pass




user_details()
