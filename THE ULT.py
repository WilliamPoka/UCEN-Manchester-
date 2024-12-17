import tkinter as tk
from tkinter import messagebox
import random

# This is to make sure no one is entering strings in the integer box!
def validate_input(new_char, current_text):
    final_text = current_text + new_char
    if new_char.isdigit() and len(current_text) < 8:
        return True
    elif new_char == "":  
        return True
    else:
        return False

# The GUI main frame (HACKING INTO THE MAIN FRAME!)
root = tk.Tk()
root.geometry("650x650")
root.title("Poka ATM Machine")

# Just a quality of life title
Label = tk.Label(root, text="Your Trusty ATM", font=('Verdana', 16))
Label.pack(pady=20)

# Code label box
number_Label = tk.Label(root, text="Input your 8 digit code: ", font=('Verdana', 16))
number_Label.pack(pady=10)

# This makes the validation function valid if that makes sense.
validate_cmd = root.register(validate_input)

# Code input box
number_entry = tk.Entry(root, font=('Verdana', 16), width=20, validate="key", validatecommand=(validate_cmd, '%P', '%S'))
number_entry.pack(pady=5)

# Create a dictionary to hold user profiles with their balance, 
user_profiles = {}

# Function to generate a random 8-digit number
def generate_random_code():
    return random.randint(10000000, 99999999)

# Function to open the signup page
def open_signup():
    # Create a new window for the signup page because i dont know how to make it just change pages so your getting a whole new page.
    signup_window = tk.Toplevel(root)
    signup_window.geometry("400x300")
    signup_window.title("Sign Up")

    # Create labels and entry field for the username only, passwords would be pointless and make this way too confusing.
    username_label = tk.Label(signup_window, text="Username:", font=('Verdana', 12))
    username_label.pack(pady=5)
    username_entry = tk.Entry(signup_window, font=('Verdana', 12), width=20)
    username_entry.pack(pady=5)

    #the famous signup page
    def submit_signup():
        username = username_entry.get()
        
        if username:
            #if asked nicely it will generate the user a nice 8 didgit code
            user_code = generate_random_code()
            
            # Save the profile (username, code, and initial balance)
            user_profiles[username] = {'code': user_code, 'balance': 0}
            
            messagebox.showinfo("Sign Up", f"Signup Successful! Your code is: {user_code}")
            signup_window.destroy()  # Close signup window after success
        else:
            messagebox.showerror("Error", "Please enter a username.")

    # Signup button (if you couldnt tell by the vbariable names)
    signup_button = tk.Button(signup_window, text="Sign Up", font=('Verdana', 12), bg='blue', fg='white', command=submit_signup)
    signup_button.pack(pady=20)

# Confirm action function for code entry
def confirm_action():
    entered_code = number_entry.get()
    
    # makes sure your not a clone and are truly the original owner of the bank account
    found_user = None
    for username, profile in user_profiles.items():
        if profile['code'] == int(entered_code):
            found_user = username
            break
    
    if found_user:
        messagebox.showinfo("Confirmation", f"Welcome, {found_user}! Code verified.")
        open_account_page(found_user)  # THE VAULT IS OPENED FOR THE ORIGINAL USER MUHAHAHAH
    else:
        messagebox.showerror("Error", "Invalid code. Please sign up first or enter a valid code.")

# Function to open the account page
def open_account_page(username):
    # Create a new window for the account page
    account_window = tk.Toplevel(root)
    account_window.geometry("400x400")
    account_window.title(f"{username}'s Account")

    # Show the current balance of the user
    balance_label = tk.Label(account_window, text=f"Balance: ${user_profiles[username]['balance']}", font=('Verdana', 16))
    balance_label.pack(pady=20)

    # Function to add money to the balance
    def add_money():
        amount = add_entry.get()
        if amount.isdigit():
            user_profiles[username]['balance'] += int(amount)
            balance_label.config(text=f"Balance: ${user_profiles[username]['balance']}")
        else:
            messagebox.showerror("Error", "Please enter a valid amount.")

    # Function to remove money from the balance
    def remove_money():
        amount = remove_entry.get()
        if amount.isdigit():
            amount = int(amount)
            if amount <= user_profiles[username]['balance']:
                user_profiles[username]['balance'] -= amount
                balance_label.config(text=f"Balance: ${user_profiles[username]['balance']}")
            else:
                messagebox.showerror("Error", "Insufficient funds.")
        else:
            messagebox.showerror("Error", "Please enter a valid amount.")
    
    # Entry to add money (im goinhg to turn this into real life)
    add_label = tk.Label(account_window, text="Add Money:", font=('Verdana', 12))
    add_label.pack(pady=5)
    add_entry = tk.Entry(account_window, font=('Verdana', 12), width=20)
    add_entry.pack(pady=5)
    
    # Entry to remove money (I dont do this because i am the money man (i lied))
    remove_label = tk.Label(account_window, text="Remove Money:", font=('Verdana', 12))
    remove_label.pack(pady=5)
    remove_entry = tk.Entry(account_window, font=('Verdana', 12), width=20)
    remove_entry.pack(pady=5)

    add_button = tk.Button(account_window, text="Add Money", font=('Verdana', 12), bg='green', fg='white', command=add_money)
    add_button.pack(pady=10)

    remove_button = tk.Button(account_window, text="Remove Money", font=('Verdana', 12), bg='red', fg='white', command=remove_money)
    remove_button.pack(pady=10)

# Confirm button
confirm_button = tk.Button(root, text="Confirm", font=('Verdana', 12), bg='green', fg='white', command=confirm_action)
confirm_button.pack(pady=10)

# Sign Up button under the confirm box
signup_button = tk.Button(root, text="Sign Up", font=('Verdana', 12), bg='blue', fg='white', command=open_signup)
signup_button.pack(pady=10)

root.mainloop()
