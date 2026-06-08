class ATM:

    def __init__(self):
        self.__pin = ""
        self.__balance = 0

    # Getter for PIN
    def get_pin(self):
        return self.__pin

    # Setter for PIN
    def set_pin(self, new_pin):
        if new_pin.isdigit() and len(new_pin) == 4:
            self.__pin = new_pin
            print("PIN set successfully")
        else:
            print("Invalid PIN. Enter a 4-digit PIN.")

    # Getter for Balance
    def get_balance(self):
        return self.__balance

    # Setter for Balance
    def set_balance(self, amount):
        if isinstance(amount, int) and amount >= 0:
            self.__balance = amount
            print("Balance updated successfully")
        else:
            print("Invalid balance amount.")

    def create_pin(self):
        pin = input("Create a 4-digit PIN: ")
        self.set_pin(pin)

    def change_pin(self):
        old_pin = input("Enter old PIN: ")

        if old_pin == self.__pin:
            new_pin = input("Enter new PIN: ")
            self.set_pin(new_pin)
        else:
            print("Incorrect old PIN")

    def check_balance(self):
        pin = input("Enter your PIN: ")

        if pin == self.__pin:
            print("Your balance is:", self.__balance)
        else:
            print("Incorrect PIN")

    def withdraw_money(self):
        pin = input("Enter your PIN: ")

        if pin == self.__pin:
            amount = int(input("Enter amount to withdraw: "))

            if amount <= self.__balance:
                self.__balance -= amount
                print("Money withdrawn successfully")
                print("Remaining balance:", self.__balance)
            else:
                print("Insufficient balance")
        else:
            print("Incorrect PIN")

    def menu(self):
        while True:
            print("\n===== ATM MENU =====")
            print("1. Create PIN")
            print("2. Change PIN")
            print("3. Check Balance")
            print("4. Withdraw Money")
            print("5. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.create_pin()

            elif choice == 2:
                self.change_pin()

            elif choice == 3:
                self.check_balance()

            elif choice == 4:
                self.withdraw_money()

            elif choice == 5:
                print("Thank you for using ATM")
                break

            else:
                print("Invalid choice")


# Object Creation
obj = ATM()

# Set initial balance using setter
obj.set_balance(1000)

# Start ATM
obj.menu()
