from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD

def cancel(button1: Button, button2: Button, label: Label, entry: Entry) -> None:
    """Quits the operation by destroying the provided widgets and returning to the main menu.

    Args:
        button1 (Button): The first button to destroy.
        button2 (Button): The second button to destroy.
        label (Label): The label to destroy.
        entry (Entry): The entry widget to destroy.
    """
    button1.destroy()
    button2.destroy()
    label.destroy()
    entry.destroy()
    back_to_menu()

def back_to_menu() -> None:
    """Returns to the main menu by recreating and placing the main buttons."""
    global newwindow
    # Recreate buttons
    button1 = Button(newwindow, text="Deposit", command=lambda: deposit(button2, button1))
    button2 = Button(newwindow, text="Withdraw", command=lambda: withdraw(button1, button2))
    button3 = Button(newwindow, text="Logout", command=logout)
    
    # Placement of buttons
    button1.place(anchor='center', relx=0.4, rely=0.6)
    button2.place(anchor='center', relx=0.6, rely=0.6)
    button3.place(anchor='center', relx=0.5, rely=0.9)

def withdraw(widget1: Widget, widget2: Widget) -> None:
    """Initiates the withdraw operation by destroying the provided widgets and setting up the withdraw interface.

    Args:
        widget1 (Widget): The first widget to destroy.
        widget2 (Widget): The second widget to destroy.
    """
    global newwindow
    
    # Destroy widgets
    widget1.destroy()
    widget2.destroy()
    
    # Creating and placing label
    label = Label(newwindow, text="Enter amount: ", font=("Arial", 8, BOLD), bg='Black', fg='Green')
    label.place(anchor='center', relx=0.5, rely=0.5)

    # Creating and placing Entry
    entry = Entry(newwindow)
    entry.place(anchor='center', relx=0.5, rely=0.55)

    # Creating and placing Buttons
    button = Button(newwindow, text="Confirm", command=lambda: approve_withdraw(entry.get(), label, entry, button, cancel_button))
    button.place(anchor='center', relx=0.4, rely=0.8)

    cancel_button = Button(newwindow, text="Cancel", command=lambda: cancel(button, cancel_button, label, entry))
    cancel_button.place(anchor='center', relx=0.6, rely=0.8)

def approve_withdraw(amount: str, label: Label, entry: Entry, button: Button, cancel_button: Button) -> None:
    """Approves the withdrawal, updates the balance, and handles potential errors.

    Args:
        amount (str): The amount to withdraw.
        label (Label): The label to destroy.
        entry (Entry): The entry widget to destroy.
        button (Button): The confirm button to destroy.
        cancel_button (Button): The cancel button to destroy.
    """
    global balance, username

    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        if amount > float(balance):
            messagebox.showerror("Error", "Insufficient funds.")
            return
        balance = str(float(balance) - amount)
        update_balance(username, balance)
        balance_label.config(text=f"Balance: {balance}")
        messagebox.showinfo("ATM", "Withdrawal successful!")
        button.destroy()
        cancel_button.destroy()
        label.destroy()
        entry.destroy()
        back_to_menu()
    except ValueError:
        messagebox.showerror("Error", "Enter a valid positive amount.")

def deposit(widget1: Widget, widget2: Widget) -> None:
    """Initiates the deposit operation by destroying the provided widgets and setting up the deposit interface.

    Args:
        widget1 (Widget): The first widget to destroy.
        widget2 (Widget): The second widget to destroy.
    """
    global newwindow

    widget1.destroy()
    widget2.destroy()

    label1 = Label(newwindow, text="Select denomination: ", font=("Arial", 8, BOLD), bg='Black', fg='Green')
    label1.place(anchor='center', relx=0.5, rely=0.5)
    
    list1 = Listbox(newwindow, height=3, selectmode=SINGLE)
    for value in ["10", "20", "50", "100", "200", "500"]:
        list1.insert(END, value)
    list1.place(anchor='center', relx=0.5, rely=0.6)

    approve_button = Button(newwindow, text="Confirm", command=lambda: approve_deposit(list1.get(ACTIVE), label1, list1, approve_button, cancel_button))
    approve_button.place(anchor='center', relx=0.4, rely=0.8)

    cancel_button = Button(newwindow, text="Cancel", command=lambda: cancel(approve_button, cancel_button, label1, list1))
    cancel_button.place(anchor='center', relx=0.6, rely=0.8)

def approve_deposit(amount: str, label: Label, listbox: Listbox, button: Button, cancel_button: Button) -> None:
    """Approves the deposit, updates the balance, and handles potential errors.

    Args:
        amount (str): The amount to deposit.
        label (Label): The label to destroy.
        listbox (Listbox): The listbox to destroy.
        button (Button): The confirm button to destroy.
        cancel_button (Button): The cancel button to destroy.
    """
    global balance, username

    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        balance = str(float(balance) + amount)
        update_balance(username, balance)
        balance_label.config(text=f"Balance: {balance}")
        messagebox.showinfo("ATM", "Deposit successful!")
        button.destroy()
        cancel_button.destroy()
        label.destroy()
        listbox.destroy()
        back_to_menu()
    except ValueError:
        messagebox.showerror("Error", "Enter a valid positive amount.")

def update_balance(username: str, new_balance: str) -> None:
    """Updates the user's balance in the data file.

    Args:
        username (str): The username of the account.
        new_balance (str): The new balance to update.
    """
    with open("file.txt", 'r') as file:
        lines = file.readlines()

    with open("file.txt", 'w') as file:
        for line in lines:
            data = line.strip().split()
            if len(data) == 3 and data[0] == username:
                file.write(f"{data[0]} {data[1]} {new_balance}\n")
            else:
                file.write(line)

def exit_app() -> None:
    """Exits the application by destroying the main window."""
    window.destroy()

def logout() -> None:
    """Logs out the user and returns to the login screen."""
    global window, newwindow
    newwindow.destroy()
    window = Tk()
    setup_main_window()

def submit() -> None:
    """Submits the login information, verifies it, and opens the main interface if successful."""
    global username, balance
    username = entry.get()
    password = entry2.get()

    try:
        with open("file.txt", 'r') as file:
            content = file.readlines()
    except FileNotFoundError:
        print("File not found")
        return

    logged_in = False
    for line in content:
        data = line.strip().split()
        if len(data) == 3 and data[0] == username and data[1] == password:
            balance = data[2]
            messagebox.showinfo("ATM", "Logged in successfully!")
            open_main_window(balance)
            logged_in = True
            break

    if not logged_in:
        messagebox.showerror("ATM", "Login Failed!\nInvalid username or password")

def open_main_window(balance: str) -> None:
    """Opens the main ATM interface window with the user's balance.

    Args:
        balance (str): The user's current balance.
    """
    global newwindow, window, balance_label

    window.destroy()
    newwindow = Tk()
    newwindow.geometry("500x500")
    newwindow.title("ATM")
    newwindow.config(background="Black")
    newwindow.eval('tk::PlaceWindow . center')

    label = Label(newwindow, text="ATM", font=('Arial', 20, BOLD), bg='Black', fg='Green', relief=RAISED, bd=10, padx=20, pady=20)
    label.pack()
    label.place(relx=0.5, rely=0.3, anchor="center")

    balance_label = Label(newwindow, text=f"Balance: {balance}", font=('Arial', 12, BOLD), bg='Black', fg='Green')
    balance_label.place(anchor='center', relx=0.5, rely=0.45)

    button1 = Button(newwindow, text="Deposit", command=lambda: deposit(button2, button1))
    button2 = Button(newwindow, text="Withdraw", command=lambda: withdraw(button1, button2))
    button3 = Button(newwindow, text="Logout", command=logout)
    button1.place(anchor='center', relx=0.4, rely=0.6)
    button2.place(anchor='center', relx=0.6, rely=0.6)
    button3.place(anchor='center', relx=0.5, rely=0.9)

    newwindow.mainloop()

def setup_main_window() -> None:
    """Sets up the main login window."""
    global entry
    global entry2
    window.geometry("500x500")
    window.title("ATM")
    window.eval('tk::PlaceWindow . center')
    window.config(background="Black")

    label = Label(window, text="ATM", font=('Arial', 20, BOLD), bg='Black', fg='Green', relief=RAISED, bd=10, padx=20, pady=20)
    label.pack()
    label.place(relx=0.5, rely=0.3, anchor="center")

    label1 = Label(window, text="Username", font=('Arial', 8, BOLD), bg='Black', fg='Green')
    label1.place(anchor='center', relx=0.4, rely=0.45)

    label2 = Label(window, text="Password", font=('Arial', 8, BOLD), bg='Black', fg='Green')
    label2.place(anchor='center', relx=0.4, rely=0.55)

    entry2 = Entry(window, font=("Arial", 10), show="*")
    entry2.place(anchor='center', relx=0.5, rely=0.6)

    entry = Entry(window, font=("Arial", 10))
    entry.place(anchor='center', relx=0.5, rely=0.5)

    button2 = Button(window, text="Login", command=submit)
    button2.place(anchor='center', relx=0.5, rely=0.7)
    button3 = Button(window, text="Exit", command=exit_app)
    button3.place(relx=0.5, rely=0.9, anchor='center')

    window.mainloop()

window = Tk()
setup_main_window()  # Start the application







