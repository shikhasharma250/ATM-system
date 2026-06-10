#  ATM Management System

A simple console-based ATM simulation built with Python that replicates basic ATM operations using Object-Oriented Programming (OOP) concepts.

---

## Features

- **Create PIN** – Set a new 4-digit PIN for your account
- **Change PIN** – Update your PIN after verifying the old one
- **Check Balance** – View your current account balance (PIN protected)
- **Withdraw Money** – Withdraw funds with balance validation (PIN protected)

---

##  Tech Stack

- **Language:** Python 3
- **Concepts Used:** OOP, Encapsulation, Getters & Setters

---

##  Getting Started

### Prerequisites

- Python 3.x installed on your system

### Run the App

```bash
python atm.py
```

---

##  Sample Output

```
===== ATM MENU =====
1. Create PIN
2. Change PIN
3. Check Balance
4. Withdraw Money
5. Exit
Enter your choice:
```

---

## Code Explanation

### Class: `ATM`

The entire application is built inside a single class called `ATM` using **encapsulation** — the PIN and balance are kept private so they cannot be accessed or modified directly from outside the class.

---

### `__init__(self)`

```python
def __init__(self):
```

- Constructor method that runs automatically when the `ATM` object is created
- Initializes two **private variables**:
  - `self.__pin = ""` — stores the user's PIN (empty at start)
  - `self.__balance = 0` — sets the starting balance to 0

---

### `get_pin(self)` and `set_pin(self, new_pin)`

```python
def get_pin(self):
def set_pin(self, new_pin):
```

- `get_pin()` — returns the current stored PIN
- `set_pin()` — validates and updates the PIN:
  - Checks that the PIN is exactly **4 numeric digits** using `isdigit()` and `len()`
  - If valid: saves it to `self.__pin`
  - If invalid: prints an error message

---

### `get_balance(self)` and `set_balance(self, amount)`

```python
def get_balance(self):
def set_balance(self, amount):
```

- `get_balance()` — returns the current balance
- `set_balance()` — validates and updates the balance:
  - Checks that the amount is a **non-negative integer** using `isinstance()`
  - If valid: updates `self.__balance`
  - If invalid: prints an error message

---

### `create_pin(self)`

```python
def create_pin(self):
```

- Takes a PIN as input from the user
- Calls `set_pin()` to validate and save the PIN

---

### `change_pin(self)`

```python
def change_pin(self):
```

- Asks the user to enter their **old PIN**
- If the old PIN matches `self.__pin`:
  - Asks for a new PIN and calls `set_pin()` to update it
- If the old PIN is wrong, prints an error message

---

### `check_balance(self)`

```python
def check_balance(self):
```

- Asks for PIN verification
- If PIN is correct, prints the current value of `self.__balance`
- If PIN is wrong, prints an error message

---

### `withdraw_money(self)`

```python
def withdraw_money(self):
```

- Asks for PIN verification
- If PIN is correct, asks the user to enter the **withdrawal amount**
- Checks if the amount is less than or equal to `self.__balance`:
  - If yes: deducts the amount from `self.__balance` and prints the remaining balance
  - If no: prints **"Insufficient balance"**
- If PIN is wrong, prints an error message

---

### `menu(self)`

```python
def menu(self):
```

- The main driver method that runs a **loop** to keep the ATM running
- Displays a numbered menu with 5 options to the user
- Takes the user's choice as input and calls the corresponding method:
  - `1` → `create_pin()`
  - `2` → `change_pin()`
  - `3` → `check_balance()`
  - `4` → `withdraw_money()`
  - `5` → Prints exit message and **breaks** the loop
- If an invalid choice is entered, prints `"Invalid choice"`

---

### Object Creation & Execution

```python
obj = ATM()
obj.set_balance(1000)
obj.menu()
```

- An `ATM` object is created
- The initial balance is set to **₹1000** using the setter method
- `menu()` is called to start the ATM

---
