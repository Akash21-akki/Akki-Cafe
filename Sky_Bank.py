print("Welcome to Sky Bank")

# Account Details
a = int(input("Enter Account Number: "))
i = input("Enter IFSC Code: ")
t = input("Your Account Type: ")
b = input("Enter Branch Name: ")

# Account balance
balance = 100000

# Type withdrawal amount according to your account balance
withdrawal_amount = int(input("Enter withdrawal amount: "))
    
if withdrawal_amount <= balance:
        balance -= withdrawal_amount
        print(f"Withdrawal Amount is {withdrawal_amount}")
        print(f"Remaining balance {balance}")
        
else:
        print("Insufficient balance")
        print("Please Add Money to your Account")

# For extra moeny withdrawal option
extra = input("Want more withdraw?: (Yes/No)")

if extra == "Y".lower() or extra == "Yes".lower():
        withdrawal_amount2 = int(input("Enter Amount: "))
        
        if withdrawal_amount2 <= balance:
            balance -= withdrawal_amount2
            print(f"Withdrawal Amount is {withdrawal_amount2}")
            print(f"Remaining balance {balance}")

print("Thank You for Banking us")