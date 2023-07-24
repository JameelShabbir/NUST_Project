import tkinter as tk
from tkinter import messagebox


def submit():
    username = username_entry.get()
    password = password_entry.get()

    # Perform form validation
    if not username and not password:
        messagebox.showerror(
            "Error", "Please enter both username and password.")
        return
    elif not username:
        messagebox.showerror(
            "Error", "Please enter username")
        return
    elif not password:
        messagebox.showerror(
            "Error", "Please enter your password.")
        return

    # Perform validation or authentication logic here

    messagebox.showinfo(
        "Login", "Username: {}\nPassword: {}".format(username, password))

    # Clear the form
    clear_form()

    # Show welcome page
    welcome_page(username)


def forget():
    signup_window = tk.Toplevel(window)
    signup_window.title("Sign Up")
    signup_window.geometry("800x600")

    # Center the sign-up window on the screen
    window_width = signup_window.winfo_width()
    window_height = signup_window.winfo_height()
    screen_width = signup_window.winfo_screenwidth()
    screen_height = signup_window.winfo_screenheight()
    x = int((screen_width/2) - (window_width/2))
    y = int((screen_height/2) - (window_height/2))
    signup_window.geometry(f"+{x}+{y}")

    # Create labels and entries for sign-up form
    signup_title_label = tk.Label(
        signup_window, text="Sign Up", font=("Helvetica", 16, "bold"))
    signup_title_label.pack(pady=10)

    signup_username_label = tk.Label(signup_window, text="Username:")
    signup_username_label.pack()
    signup_username_entry = tk.Entry(signup_window)
    signup_username_entry.pack()

    signup_password_label = tk.Label(signup_window, text="Password:")
    signup_password_label.pack()
    signup_password_entry = tk.Entry(signup_window, show="*")
    signup_password_entry.pack()

    signup_name_label = tk.Label(signup_window, text="Name:")
    signup_name_label.pack()
    signup_name_entry = tk.Entry(signup_window)
    signup_name_entry.pack()

    signup_email_label = tk.Label(signup_window, text="Email:")
    signup_email_label.pack()
    signup_email_entry = tk.Entry(signup_window)
    signup_email_entry.pack()

    signup_button = tk.Button(
        signup_window, text="Sign Up", command=signup_submit)
    signup_button.pack()


def signup_submit():
    username = signup_username_entry.get()
    password = signup_password_entry.get()
    name = signup_name_entry.get()
    email = signup_email_entry.get()

    # Perform form validation
    if not username or not password or not name or not email:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    # Store the user information or perform any other required logic

    messagebox.showinfo("Sign Up", "Username: {}\nPassword: {}\nName: {}\nEmail: {}".format(
        username, password, name, email))

    # Clear the form
    signup_username_entry.delete(0, tk.END)
    signup_password_entry.delete(0, tk.END)
    signup_name_entry.delete(0, tk.END)
    signup_email_entry.delete(0, tk.END)


def clear_form():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    check_button.deselect()


def welcome_page(username):
    welcome_window = tk.Toplevel(window)
    welcome_window.title("Welcome")
    welcome_window.geometry("800x600")

    # Center the welcome window on the screen
    window_width = welcome_window.winfo_width()
    window_height = welcome_window.winfo_height()
    screen_width = welcome_window.winfo_screenwidth()
    screen_height = welcome_window.winfo_screenheight()
    x = int((screen_width/2) - (window_width/2))
    y = int((screen_height/2) - (window_height/2))
    welcome_window.geometry(f"+{x}+{y}")

    welcome_label = tk.Label(welcome_window, text="Welcome, {}!".format(
        username), font=("Helvetica", 16, "bold"), background="green")
    welcome_label.pack(pady=50)
    welcome_label = tk.Label(
        welcome_window, text="We hope you are well and injoying, {}!".format(username))
    welcome_label.pack(pady=50)

    logout_button = tk.Button(
        welcome_window, text="Logout", command=welcome_window.destroy)
    logout_button.pack()


# Create the main window
window = tk.Tk()
window.title("Login System")
window.geometry("800x450")
window.resizable(True, True)

# Set the window title
title_label = tk.Label(window, text="Login System",
                       font=("Helvetica", 26, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Create labels and entries
username_label = tk.Label(window, text="Username:")
username_label.grid(row=1, column=0, pady=5)
username_entry = tk.Entry(window)
username_entry.grid(row=1, column=1, pady=5)

password_label = tk.Label(window, text="Password:")
password_label.grid(row=2, column=0, pady=5)
password_entry = tk.Entry(window, show="*")
password_entry.grid(row=2, column=1, pady=5)

# Create buttons
check_button = tk.Checkbutton(window, text="Remember me")
check_button.grid(row=3, column=0, columnspan=2, pady=5)

submit_button = tk.Button(window, text="Submit", command=submit)
submit_button.grid(row=4, column=0, columnspan=2, pady=5)

forget_button = tk.Button(window, text="Forgot Password?", command=forget)
forget_button.grid(row=5, column=0, columnspan=2, pady=5)

clear_button = tk.Button(window, text="Clear Form", command=clear_form)
clear_button.grid(row=6, column=0, columnspan=2, pady=5)

# Run the event loop
window.mainloop()
