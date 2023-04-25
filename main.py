import random
import string
import tkinter

# basic settings
bg_color = "#878787"
main_font = "Arial", "10"


# generator function
def password_generator():
    password_lenght = characters_entry.get()
    password = []

    # items of password
    letters = string.ascii_lowercase
    capital_letters = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation

    lists = [letters]

    # user choices
    if check_capital_letters.get() == 1:
        lists.append(capital_letters)
    if check_numbers.get() == 1:
        lists.append(numbers)
    if check_special_characters.get() == 1:
        lists.append(special_characters)

    # password generator
    for one_character in range(password_lenght):
        one_list = random.choice(lists)
        one_letter = random.choice(one_list)
        password.append(one_letter)

    # print password
    password_string = "".join(password)

    result_label = tkinter.Label(text="Your password: ", background=bg_color, font=main_font)
    result_label.grid(row=6, column=0, columnspan=2, padx=(15, 0), pady=(10, 0), sticky="w")

    password_entry = tkinter.StringVar()
    password_entry.set(password_string)
    password_entry_label = tkinter.Entry(readonlybackground=bg_color, font=main_font, bd=0,
                                         state="readonly", textvariable=password_entry, width=35)
    password_entry_label.grid(row=7, column=0, columnspan=2, padx=15, pady=(5, 15), sticky="we")


# window
screen = tkinter.Tk()
screen.title("Password Generator")
screen.iconbitmap("icon.ico")
screen.geometry("300x320+200+200")
screen.resizable(False, False)
screen.configure(background=bg_color)

screen_text = tkinter.Label(text="Customize your password: ", background=bg_color, font=main_font)
screen_text.grid(row=0, column=0, columnspan=2, padx=15, pady=15, sticky="w")

# password lenght
characters_label = tkinter.Label(text="Minimum lenght: ", background=bg_color, font=main_font)
characters_label.grid(row=1, column=0, padx=15, pady=5, sticky="n")

characters_entry = tkinter.Scale(from_=4, to=30, orient="horizontal", background=bg_color)
characters_entry.grid(row=1, column=1, pady=5, sticky="we")

# user choices
check_capital_letters = tkinter.IntVar()
capital_letters_choice = tkinter.Checkbutton(screen, text="capital letters", variable=check_capital_letters,
                                             background=bg_color, activebackground=bg_color, font=main_font)
capital_letters_choice.grid(row=2, column=0, sticky="w", padx=15)

check_numbers = tkinter.IntVar()
numbers_choice = tkinter.Checkbutton(text="numbers", variable=check_numbers,
                                     background=bg_color, activebackground=bg_color, font=main_font)
numbers_choice.grid(row=3, column=0, sticky="w", padx=15)

check_special_characters = tkinter.IntVar()
special_characters_choice = tkinter.Checkbutton(text="special characters", variable=check_special_characters,
                                                background=bg_color, activebackground=bg_color, font=main_font)
special_characters_choice.grid(row=4, column=0, sticky="w", padx=15)

# confirm button
confirm_button = tkinter.Button(text="Confirm", background=bg_color, activebackground="#CACACA", command=password_generator)
confirm_button.grid(row=5, column=1, pady=15, sticky="e")

# mainloop
screen.mainloop()
