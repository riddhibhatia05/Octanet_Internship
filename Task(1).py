# Define a class called ATM to simulate an Automated Teller Machine
class ATM:
    # Initialize the ATM object with default values for balance, PIN, and transaction history
    def __init__(self, balance=0, pin=1234, transaction_history=[]):
        # Set the initial balance to 0 (or a specified value)
        self.balance = balance
        # Set the initial PIN to 1234 (or a specified value)
        self.pin = pin
        # Create an empty list to store transaction history
        self.transaction_history = transaction_history
        # Set the exchange rate for converting USD to INR (approximate)
        self.exchange_rate = 74.83  # 1 USD = 74.83 INR

    # Method to check the current account balance
    def check_balance(self):
        """
        Check account balance and display it in both USD and INR
        """
        # Print the current balance in USD and INR
        print(f"Your current balance is: ${self.balance:.2f} (USD) / ₹{self.balance * self.exchange_rate:.2f} (INR)")

    # Method to withdraw cash from the account
    def withdraw_cash(self):
        """
        Withdraw cash from account and update balance and transaction history
        """
        # Prompt user to enter amount to withdraw (in USD)
        amount = float(input("Enter amount to withdraw (in USD): $"))
        # Check if the withdrawal amount exceeds the current balance
        if amount > self.balance:
            # If insufficient balance, print an error message
            print("Insufficient balance")
        else:
            # If sufficient balance, subtract the withdrawal amount from the balance
            self.balance -= amount
            # Add a transaction record to the history list
            self.transaction_history.append(f"Withdrawal: -${amount:.2f} (USD) / -₹{amount * self.exchange_rate:.2f} (INR)")
            # Print a success message with the updated balance
            print(f"Withdrawal successful. New balance: ${self.balance:.2f} (USD) / ₹{self.balance * self.exchange_rate:.2f} (INR)")

    # Method to deposit cash into the account
    def deposit_cash(self):
        """
        Deposit cash into account and update balance and transaction history
        """
        # Prompt user to enter amount to deposit (in USD)
        amount = float(input("Enter amount to deposit (in USD): $"))
        # Add the deposit amount to the balance
        self.balance += amount
        # Add a transaction record to the history list
        self.transaction_history.append(f"Deposit: +${amount:.2f} (USD) / +₹{amount * self.exchange_rate:.2f} (INR)")
        # Print a success message with the updated balance
        print(f"Deposit successful. New balance: ${self.balance:.2f} (USD) / ₹{self.balance * self.exchange_rate:.2f} (INR)")

    # Method to change the PIN
    def change_pin(self):
        """
        Change the PIN after verifying the old PIN
        """
        # Prompt user to enter old PIN
        old_pin = int(input("Enter old PIN: "))
        # Check if the entered old PIN matches the current PIN
        if old_pin == self.pin:
            # If match, prompt user to enter new PIN
            new_pin = int(input("Enter new PIN: "))
            # Update the PIN
            self.pin = new_pin
            # Print a success message
            print("PIN changed successfully")
        else:
            # If no match, print an error message
            print("Invalid old PIN")

    # Method to view transaction history
    def view_transaction_history(self):
        """
        Display the transaction history
        """
        # Print the transaction history header
        print("Transaction History:")
        # Iterate through the transaction history list and print each record
        for transaction in self.transaction_history:
            print(transaction)

# Main program to interact with the ATM
def main():
    # Create an ATM object
    atm = ATM()
    # Loop indefinitely until user chooses to exit
    while True:
        # Print the ATM menu
        print("ATM Menu:")
        print("1. Check Balance")
        print("2. Withdraw Cash")
        print("3. Deposit Cash")
        print("4. Change PIN")
        print("5. View Transaction History")
        print("6. Exit")
        # Prompt user to enter their choice
        choice = int(input("Enter your choice: "))
        # Handle each menu option
        if choice == 1:
            atm.check_balance()
        elif choice == 2:
            atm.withdraw_cash()
        elif choice == 3:
            atm.deposit_cash()
        elif choice == 4:
            break
          elif choice == 4:
            atm.change_pin()
        elif choice == 5:
            atm.view_transaction_history()
        elif choice == 6:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
