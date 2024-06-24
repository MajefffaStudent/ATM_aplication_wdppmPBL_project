# ATM Application

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [File Structure](#file-structure)
6. [Data File Format](#data-file-format)
7. [Functionality](#functionality)
8. [Requirements](#requirements)
9. [Author](#author)

## Introduction

The ATM application is a graphical user interface (GUI) program that allows users to log in, check their balance, deposit funds, and withdraw funds. User data is stored in a text file (`file.txt`). The application is built using Python's Tkinter library.

## Features

- **Login**: Authenticate users based on username and password.
- **Balance Inquiry**: Display the user's current balance.
- **Deposit Funds**: Allow users to deposit a specified denomination.
- **Withdraw Funds**: Allow users to withdraw a specified amount.
- **Logout**: Log out and return to the login screen.
- **Exit**: Close the application.

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Clone or download the repository containing the application files.
3. Make sure the `file.txt` data file is in the same directory as the main script (`main.py`).

## Usage

### Running the Application

1. Open a terminal or command prompt.
2. Navigate to the directory containing `main.py`.
3. Run the application using the following command:

   ```sh
   python main.py
   ```

### Application Workflow

1. **Login Screen**:
   - Enter your username and password.
   - Click the "Login" button to authenticate.
   - Click "Exit" to close the application.

2. **Main Menu**:
   - After a successful login, you will see your balance and options to deposit, withdraw, or logout.
   - Click "Deposit" to deposit funds.
   - Click "Withdraw" to withdraw funds.
   - Click "Logout" to log out and return to the login screen.

3. **Deposit Funds**:
   - Select a denomination from the list.
   - Click "Confirm" to deposit the selected amount.
   - Click "Cancel" to return to the main menu without depositing.

4. **Withdraw Funds**:
   - Enter the amount you wish to withdraw.
   - Click "Confirm" to withdraw the specified amount.
   - Click "Cancel" to return to the main menu without withdrawing.

## File Structure

```
ATM-Application/
│
├── main.py          # Main application script
├── file.txt         # User data file
└── README.txt       # Application documentation
```

## Data File Format

The `file.txt` file should contain user data in the following format:

```
username password balance
```

### Example:

```
john_doe password123 500.0
jane_smith mypassword 1000.0
```

## Functionality

### Main Functions

- **setup_main_window()**: Sets up the main login window.
- **submit()**: Verifies login credentials and opens the main ATM interface if successful.
- **open_main_window(balance)**: Opens the main ATM interface with options for deposit, withdrawal, and logout.
- **deposit(widget1, widget2)**: Initiates the deposit process.
- **withdraw(widget1, widget2)**: Initiates the withdrawal process.
- **approve_deposit(amount, label, listbox, button, cancel_button)**: Processes the deposit and updates the balance.
- **approve_withdraw(amount, label, entry, button, cancel_button)**: Processes the withdrawal and updates the balance.
- **update_balance(username, new_balance)**: Updates the user's balance in the `file.txt` file.
- **cancel(button1, button2, label, entry)**: Cancels the current operation and returns to the main menu.
- **logout()**: Logs out the user and returns to the login screen.
- **exit_app()**: Exits the application.

## Requirements

- Python 3.x
- Tkinter library (usually included with Python)

## Author

Jakub Giądła, Mateusz Majewski, Paweł Wolny, Tomasz Piskozub
