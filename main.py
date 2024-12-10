import json
import tkinter as tk
from tkinter import END
from tkinter import messagebox
import random
from jsonHandling import update_json_file
import pyperclip

window = tk.Tk()


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    pass_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    pass_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = pass_numbers + pass_symbols + pass_letters

    random.shuffle(password_list)

    password_generated = "".join(password_list)

    password.delete(0, END)
    password.insert(0, password_generated)
    pyperclip.copy(f"{password_generated}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    data = {
        website_input.get(): {
            "username": username.get(),
            "password": password.get()
        }
    }

    if website_input.get() == "" and password.get() == "":
        messagebox.showinfo(message="Please fill the required fields")
    elif username.get() == "":
        messagebox.showinfo(message="Please fill the username field")
    elif password.get() == "":
        messagebox.showinfo(message="Please fill the password field")
    elif website_input.get() == "":
        messagebox.showinfo(message="Please fill the website field")
    else:
        proceed = messagebox.askokcancel(title=website_input.get(), message=f"Username: {username.get()}\n" "Password: "
                                                                            f"{password.get()} \n Do you want to "
                                                                            f"proceed ?")
        if proceed:
            update_json_file("data.json", data)
            # try:
            #     with open("data.json", "r") as file:
            #         root_data = json.load(file)
            # except FileNotFoundError:
            #     with open("data.json", "w") as file:
            #         json.dump(data, file, indent=4)
            # else:
            #     with open("data.json", "w") as file:
            #         root_data.update(data)
            #         json.dump(root_data, file, indent=4)

        website_input.delete(0, END)
        username.delete(0, END)
        password.delete(0, END)


# ---------------------------SEARCH-------------------------------------- #
def find_credentials():
    try:
        with open("data.json", "r") as file:
            search_data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Data File", message="Credential Database is missing")
    else:
        for i, j in search_data.items():
            if website_input.get().lower() == i.lower():
                copy_credentials = messagebox.askquestion(title=i, message=f"Username: {j["username"]}\n"
                                                                           "\n"  # f"Password: {j["password"]}\n"
                                                                           f"Do you want to copy the password ?\n")
                if copy_credentials == "yes":
                    pyperclip.copy(j["password"])
                break
        else:
            messagebox.showinfo(title=website_input.get(), message=f"Credentials for {website_input.get()} is "
                                                                   f"missing")


# ---------------------------- UI SETUP ------------------------------- #
window.title("Password Manager")
window.minsize(width=350, height=600)
window.configure(background="#ADD8E6")
window.config(padx=30, pady=22)

# Image Canvas
canvas = tk.Canvas(width=150, height=150, background="#ADD8E6", highlightthickness=0)
logo_img = tk.PhotoImage(file="pass-logo.png")
canvas.create_image(75, 75, image=logo_img)
canvas.grid(row=0, column=1, padx=15, pady=12)

# Website display text
website_name = tk.Label(text="Website: ", background="#ADD8E6")
website_name.grid(row=1, column=0, pady=10)

# Website Text Box
website_input = tk.Entry(width=36)
website_input.grid(row=1, column=1, sticky='w', pady=10)
website_input.focus()

# Search button
search_button = tk.Button(text="Search", command=find_credentials)
search_button.grid(row=1, column=2)

# Username display text
username_text = tk.Label(text="Username or Mail", background="#ADD8E6")
username_text.grid(row=2, column=0, pady=10)

# Username text box
username = tk.Entry(width=36)
username.grid(row=2, column=1, columnspan=2, sticky='w', pady=10)
username.insert(0, string="yourmail@mail.com")

# Password display text
password_text = tk.Label(text="Password: ", background="#ADD8E6")
password_text.grid(row=3, column=0, pady=10)

# Password text box
password = tk.Entry(width=30)
password.grid(row=3, column=1, sticky='w', pady=10)  # Stick to west (left)

# Password generator button
generate_password_button = tk.Button(text="Generate", command=pass_gen)
generate_password_button.grid(row=3, column=2)

# Add button
add_credentials = tk.Button(text="Add", width=30, command=save)
add_credentials.grid(row=4, column=1, sticky='w', columnspan=2, pady=20)

window.mainloop()
