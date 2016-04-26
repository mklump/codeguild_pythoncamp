# -*- coding: utf-8 -*-
"""
Python Coding Bootcamp (pdxcodeguild)
Program exercise file input/output in Python
by Matthew James K
LAB/STEP requirements:

Practice: ATM

Write a program that functions as a simple ATM for a single account.

An account will be a class: it will have a field for the balance.

Write functions for the account class that:
Deposit to the account.
Check if enough funds for a withdrawal.
Withdraw an allowed amount.
Calculate 0.5% interest on the account.

Implement a user interface that lets a user pick each of those actions and updates the account. After each action it will print the balance.

Advanced
    Save the account balance to a file after each operation. Read that balance on startup so the balance persists across program starts.
    Add to each account class an account ID number.
    Allow the user to open more than one account. Let them perform all of the above operations by account number.

Added Friday 10:52AM, and being summarily ignored because this was not part of the original design:
    Add a function called  get_standing  have it return a bool with whether the account has less than $1000 in it.
    Predatorily charge a transaction fee every time a withdrawal or deposit happens if the account is in bad standing.
"""

class ATMBankAccount:

    #balance = 0.0 # leave out for this excercise, no class variables until later - use only instance variables here.

    def __init__(self, account_id, balance):
        """
        Two argument "magic" constructor
        """
        self.account_id = account_id
        self.balance = balance

    def __eq__(self, other_account):
        """
        Overloaded == equality operator
        """
        return (
            self.account_id == other_account.account_id
            and self.balance == other_account.balance
            )

    def __repr__(self):
        """
        String definition representation of this object. 'this' instead of 'self' but are still the same.
        Prints out the account_ID and the balance of self.this account.
        """
        return 'ATMBankAccount({}, {})'.format(
            self.account_id,
            self.balance
            )

    def deposit_to_account(list_of_all_accounts_known, ID_account_to_deposit_to, money_amount_to_deposit):
        """
        This class function deposits to the specified account ID the specified amount of money.
        :param 1: list_of_all_accounts_known as the list of all known as a list of ATMBankAccount objects
        :param 2: ID_account_to_deposit_to as the account ID to deposit the money to
        :param 3: money_amount_to_deposit the amount of money to deposit as an integer
        """
        for account in list_of_all_accounts_known:
            if ID_account_to_deposit_to == account.account_id:
                account.balance += money_amount_to_deposit

    def is_sufficient_funds_for_withdrawal(list_of_all_accounts_known, ID_account_to_check_amount, amount_needed_for_withdrawl): 
        """
        This class function checks to see if the specified account ID has sufficient funds for the specified withdrawl.
        :param 1: list_of_all_accounts_known as the list of all known as a list of ATMBankAccount objects
        :param 2: ID_account_to_deposit_to as the account ID to check for available money sufficinet fund for withdrawl
        :param 3: amount_needed_for_withdrawl as the amount of the requested withdrawl
        :returns: True if there are sufficient funds, otherwise False
        """
        for account in list_of_all_accounts_known:
            if ID_account_to_check_amount == account.account_id and amount_needed_for_withdrawl <= account.balance:
                return True
            # end if checking
        return False

    def withdrawl_fund_from_account(list_of_all_accounts_known, ID_account_to_withdrawl_from, money_amount_to_withdrawl):
        """
        This class function withdrawls the spefcified amount of money from the specified account, if there are sufficient funds.
        :param 1: list_of_all_accounts_known as the list of all known as a list of ATMBankAccount objects
        :param 2: ID_account_to_deposit_to as the account ID to withdrawl from
        :param 3: amount_needed_for_withdrawl as the amount of the requested withdrawl
        :returns: True if the operation succeeded, otherwise False
        """
        for account in list_of_all_accounts_known:
            if ID_account_to_withdrawl_from == account.account_id and True == is_sufficient_funds_for_withdrawal(
                list_of_all_accounts_known, ID_account_to_withdrawl_from, money_amount_to_withdrawl
                ):
                account.balance -= money_amount_to_withdrawl
                return True
            # end if checking
        return False

    def calculate_half_percent_interest_on_account(list_of_all_accounts_known, ID_account_to_give_interest):
        """
        This class function automatically adds 0.5% interest for the specified account ID.
        :param 1: list_of_all_accounts_known as the list of all known as a list of ATMBankAccount objects
        :param 2: ID_account_to_give_interest as the account ID of which to add 0.5% interest to automatically
        """
        for account in list_of_all_accounts_known:
            if ID_account_to_give_interest == account.account_id:
                account.balance += (account.balance * 0.005)

    def write_out_account_numbers_and_balances(list_of_all_accounts_known):
        """
        This class method will write out all accounts and their balances to the local file practise_accounts.txt.
        :param 1: list_of_all_accounts_known as the list of all known working accounts to write out to the file.
        """
        with open('./practise_accounts.txt', mode='wt') as accounts_and_balances_to_write_out:
            for accounts in list_of_all_accounts_known:
                accounts_and_balances_to_write_out.writelines('{0} {1}\n'.format(accounts.account_id, accounts.balance));
        # end of withblock, close open file writing

    def read_in_account_numbers_and_balances():
        """
        This class method will read in all accounts and their balances from the local file practise_accounts.txt.
        :returns: All the known account ID and their related balances as a ATMBankAccount object list of accounts
        with associated balances.
        """
        accounts_balances = []
        with open('./practise_accounts.txt', mode='rt') as all_known_accounts_and_balances:
            customer_accounts_balances = all_known_accounts_and_balances.readlines()
            for account_and_balance in customer_accounts_balances:
                account_entry = account_and_balance.strip().split()
                accounts_balances.append(ATMBankAccount(account_entry[0], account_entry[1]))
        return accounts_balances
# end of class AutomaticTellerMachine:

def prompt_user_what_to_do_next():
    """
    Specifically prompt the user for an action with 
    """
    print('What do you, user, want to do next for banking?')
    print('Enter 1 to open account, 2 to check your balance, 3 to deposit to your account, 4 to withdrawl from your account,')
    print('or 5 to automatically earn 0.5% interest on your account, or q to quit:')
    return input()

def create_an_account_for_user(list_of_all_accounts_known, starting_account_balance_amount):
    """
    This helper function creates a new account for the asking user, and returns this list of all known accounts
    with the newly created account appended to the end of the account list.
    :param 1: list_of_all_accounts_known as the list of all known working accounts as a list
    :param 2: starting_account_balance_amount as the newly created starting account balance as an integer
    :returns: list_of_all_accounts_known with the newly created account
    """
    #account_numbers, balance_ammounts = zip(*zip(list_of_all_accounts_known)) # Error - cannot unzip single object, only list of two elements
    last_unique_account_ID = list_of_all_accounts_known[len(list_of_all_accounts_known) - 1].account_id
    new_account = ATMBankAccount(str(int(last_unique_account_ID) + 1), str(starting_account_balance_amount))
    return list_of_all_accounts_known.append(new_account)

def prompt_user_for_starting_balance():
    """
    This helper function asks the user for what the starting account balance should be, and returns that number.
    :returns: the starting account balance of the new account as an integer.
    """
    print('What starting account balance do you want to have for your new account?')
    return input()

def print_out_account_balances(list_of_all_accounts_known):
    """
    The helper function prints to standard out all of the user's accounts, and there balances.
    :param 1: list_of_all_accounts_known as the list of all known working accounts as a list to output.
    """
    for account in list_of_all_accounts_known:
        print('{0} {1}'.format(account.account_id, account.balance))

def prompt_user_account_to_deposit():
    """
    This helper function prompts the user from standard in for what account to deposit to.
    :returns: account number to deposit to a string
    """
    print('What account do you want to deposit to?:')
    return input()

def prompt_user_money_to_deposit():
    """
    This helper function prompts the user from standard in for what amount of money to deposit.
    :returns: ammount of money to deposit as a string
    """
    print('What amount of money do you want to deposit?:')
    return input()

def prompt_user_account_to_withdrawl():
    """
    This helper function prompts the user from standard in for what account to withdrawl from.
    :returns: account number to withdrawl from as a string
    """
    print('What account do you want to withdrawl from?:')
    return input()

def prompt_user_money_to_withdrawl():
    """
    This helper function prompts the user from standard in for what amount of money to withdrawl.
    :returns: ammount of money to withdrawl as a string
    """
    print('What amount of money do you want to withdrawl?:')
    return input()

def prompt_user_account_to_get_interest():
    """
    This helper function prompts the user from standard in for what account to get interest.
    :returns: account number ID to get automatic interest
    """
    print('What account do you want 0.5% automatic interest?:')
    return input()

def main():
    """
    Main function/test driver main single thread of execution for this console program.
    """
    user_answer = prompt_user_what_to_do_next()
    while 'q' != user_answer:
        list_of_all_accounts_known = ATMBankAccount.read_in_account_numbers_and_balances()
        if '1' == user_answer:
            starting_account_balance_ammount = prompt_user_for_starting_balance()
            create_an_account_for_user(list_of_all_accounts_known, int(starting_account_balance_ammount))
        elif '2' == user_answer:
            print_out_account_balances(list_of_all_accounts_known)
        elif '3' == user_answer:
            user_to_account_deposit = prompt_user_account_to_deposit()
            user_money_to_deposit = prompt_user_money_to_deposit()
            ATMBankAccount.deposit_to_account(list_of_all_accounts_known, user_to_account_deposit, user_money_to_deposit)
            print_out_account_balances(list_of_all_accounts_known)
        elif '4' == user_answer:
            user_to_account_withdrawl = prompt_user_to_withdrawl()
            user_money_to_withdrawl = prompt_user_money_to_withdrawl()
            ATMBankAccount.withdrawl_fund_from_account(list_of_all_accounts_known, user_to_account_withdrawl, user_money_to_withdrawl)
            print_out_account_balances(list_of_all_accounts_known)
        elif '5' == user_answer:
            user_account_to_get_interest = prompt_user_account_to_get_interest()
            ATMBankAccount.calculate_half_percent_interest_on_account(list_of_all_accounts_known, user_account_to_get_interest)
            print_out_account_balances(list_of_all_accounts_known)
        user_answer = prompt_user_what_to_do_next()
        break
    ATMBankAccount.write_out_account_numbers_and_balances(list_of_all_accounts_known)

main()