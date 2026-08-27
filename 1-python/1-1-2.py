"""
Let's write a program to divide up the check among diners in a party.

Write a program to input the amount of a restaurant check, tip %, and number of diners

The program should output the total amount with tip, and the amount each diner owes.
"""

check_amount = float(input("Enter the check amount: "))
tip_percent = float(input("Enter the tip percentage (e.g., 15 for 15%): "))
num_diners = int(input("Enter the number of diners: "))

if check_amount < 0 or tip_percent < 0 or num_diners < 0:
	print("Error: values cannot be less than zero.")
	exit(1)
else:
	print(f"Total check amount: ${check_amount:.2f}")
	print(f"Tip amount: ${check_amount * tip_percent / 100:.2f}")
	print(f"Total amount with tip: ${check_amount * (1 + tip_percent / 100):.2f}")
	print(f"Amount per diner: ${check_amount * (1 + tip_percent / 100) / num_diners:.2f}")
	exit(0)
	