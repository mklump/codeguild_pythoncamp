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
?Deposit to the account.
?Check if enough funds for a withdrawal.
?Withdraw an allowed amount.
?Calculate 0.5% interest on the account.

Implement a user interface that lets a user pick each of those actions and updates the account. After each action it will print the balance.

Advanced
?Save the account balance to a file after each operation. Read that balance on startup so the balance persists across program starts.
?Add to each account class an account ID number.
?Allow the user to open more than one account. Let them perform all of the above operations by account number.

Added Friday 10:52AM, and being summarily ignored because this was not part of the original design:
•Add a function called  get_standing  have it return a bool with whether the account has less than $1000 in it.
•Predatorily charge a transaction fee every time a withdrawal or deposit happens if the account is in bad standing.
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

	def __str__(self):
		"""
		String definition representation of this object. 'this' instead of 'self' but are still the same.
		Prints out the account_ID and the balance of self.this account.
		"""
		return 'ATMBankAccount({}, {})'.format(
			self.account_id,
			self.balance
			)

	def deposit_to_account(ID_account_to_deposit_to, money_amount_to_deposit):
		raise NotImplementedError

	def check_if_enough_funds_for_withdrawal(ID_account_to_check_amount, amount_needed_for_withdrawl):
		raise NotImplementedError

	def withdrawl_fund_from_account(ID_account_to_withdrawl_from, money_amount_to_withdrawl):
		raise NotImplementedError

	def calculate_half_percent_interest_on_account(ID_account_to_give_interest):
		raise NotImplementedError

	def write_out_account_numbers_and_balances(list_of_all_accounts_known):
		"""
		This class method will write out all accounts and their balances to the local file practise_accounts.txt.
		:param 1: list_of_all_accounts_known as the list of all known working accounts to write out to the file.
		"""
		with open('./practise_accounts.txt', mode='wt') as accounts_and_balances_to_write_out:
			for accounts in list_of_all_accounts_known:
				accounts_and_balances_to_write_out.writelines('{0} {1}'.format(accounts.account_id, accounts.balance));
		# end of withblock, close open file writing

	def read_in_account_numbers_and_balances():
		"""
		This class method will read in all accounts and their balances from the local file practise_accounts.txt.
		:returns: All the known account ID and their related balances as a ATMBankAccount object list of accounts
		with associated balances.
		"""
		accounts_balances = []
		with open('./practise_accounts.txt') as all_known_accounts_and_balances:
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
	print('Enter 1 to open account, 2 to check your balance, 3 to deposit to your account, 4 to show all accounts')
	print('5 to withdrawl from your account, or 6 to automatically earn 0.5% interest on your account, or q to quit:')
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
		#elif '2' == user_answer:
		#elif '3' == user_answer:
		#elif '4' == user_answer:
		#elif '5' == user_answer:
		#elif '6' == user_answer:
		#user_answer = prompt_user_what_to_do_next()
		break
	ATMBankAccount.write_out_account_numbers_and_balances(list_of_all_accounts_known)

main()