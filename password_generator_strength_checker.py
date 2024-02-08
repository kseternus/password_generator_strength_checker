import tkinter as tk
import webbrowser
import random
import string
import pyperclip
from tkinter import ttk


def password_gen(*args):
    password_length = int(slider.get())
    chars = ((string.ascii_lowercase if checkbox_lower_var.get() else '')
             + (string.ascii_uppercase if checkbox_upper_var.get() else '')
             + (string.digits if checkbox_digit_var.get() else '')
             + (string.punctuation if checkbox_special_var.get() else ''))
    if chars == '':
        proposal_password_label.config(text=' ')
    else:
        generated_password = ''.join(random.choice(chars) for _ in range(password_length))
        proposal_password_label.config(text=generated_password)


def check_password_strength():
    password = password_entry.get()
    letters_lower = sum(1 for char in password if char in string.ascii_lowercase)
    letters_upper = sum(1 for char in password if char in string.ascii_uppercase)
    digits = sum(1 for char in password if char in string.digits)
    special_char = sum(1 for char in password if char in string.punctuation)
    sum_strength = (1 if letters_lower > 0 else 0) + (1 if letters_upper > 0 else 0) + (1 if digits > 0 else 0) + (
        1 if special_char > 0 else 0)
    sum_characters = letters_lower + letters_upper + digits + special_char
    is_lowercase.config(foreground='#baff99') if letters_lower >= 1 else is_lowercase.config(foreground='#ffffff')
    is_uppercase.config(foreground='#baff99') if letters_upper >= 1 else is_uppercase.config(foreground='#ffffff')
    is_digit.config(foreground='#baff99') if digits >= 1 else is_digit.config(foreground='#ffffff')
    is_special.config(foreground='#baff99') if special_char >= 1 else is_special.config(foreground='#ffffff')
    if sum_strength == 1:
        strength_bar['value'] = 5
        info_text.config(text='very weak', foreground='#ffb3ba')
        if sum_characters > 8:
            strength_bar['value'] = 10
            info_text.config(text='very weak', foreground='#ffb3ba')
        elif sum_characters > 16:
            strength_bar['value'] = 20
            info_text.config(text='very weak', foreground='#ffb3ba')

    elif sum_strength == 2:
        strength_bar['value'] = 15
        info_text.config(text='very weak', foreground='#ffb3ba')
        if sum_characters > 16:
            strength_bar['value'] = 55
            info_text.config(text='medium', foreground='#baff99')
        elif sum_characters > 8:
            strength_bar['value'] = 35
            info_text.config(text='weak', foreground='#ffdfba')
        elif sum_characters > 12:
            strength_bar['value'] = 45
            info_text.config(text='medium', foreground='#baffc9')

    elif sum_strength == 3:
        strength_bar['value'] = 20
        info_text.config(text='weak', foreground='#ffdfba')
        if sum_characters > 16:
            strength_bar['value'] = 55
            info_text.config(text='very good', foreground='#baff99')
        elif sum_characters > 8:
            strength_bar['value'] = 35
            info_text.config(text='medium', foreground='#baffc9')
        elif sum_characters > 12:
            strength_bar['value'] = 45
            info_text.config(text='good', foreground='#baffc9')

    elif sum_strength == 4:
        strength_bar['value'] = 25
        info_text.config(text='weak', foreground='#ffdfba')
        if sum_characters > 20:
            strength_bar['value'] = 100
            info_text.config(text='ultimate password', foreground='#4dff00')
        elif sum_characters > 12:
            strength_bar['value'] = 65
            info_text.config(text='good', foreground='#baff99')
        elif sum_characters > 16:
            strength_bar['value'] = 75
            info_text.config(text='very good', foreground='#baff99')


def callback(url):
    webbrowser.open_new(url)


def copy_password():
    pyperclip.copy(proposal_password_label['text'])


def read_more():
    read_more_window = tk.Tk()
    read_more_window.geometry('800x250')
    read_more_window.resizable(False, False)
    read_more_window.config(background='#383f40')
    read_more_window.title('Info')
    read_more_window_text = tk.Label(read_more_window, font='Futura 12', foreground='#ffffff', background='#383f40')
    read_more_window_text['text'] ="""
    Password security starts with creating a strong password. A strong password is:
    •At least 12 characters long but 14 or more is better.
    •A combination of uppercase letters, lowercase letters, numbers, and symbols.
    •Not a word that can be found in a dictionary or the name of a person, character, product, or organization.
    •Significantly different from your previous passwords.
    •Easy for you to remember but difficult for others to guess.
    Consider using a memorable phrase like "6MonkeysRLooking^"."""
    read_more_window_text.pack()
    source_label = tk.Label(read_more_window, text='Source', font='Futura 12', foreground='#ffffff',
                            background='#383f40')
    source_label.bind("<Button-1>", lambda e: callback(
        "https://support.microsoft.com/en-us/windows/create-and-use-strong-passwords-c5cebb49-8c53-4f5e-2bc4-fe357ca048eb"))
    source_label.pack(pady=15)
    read_more_window_text = tk.Button(read_more_window, text='Close', foreground='#ffffff', background='#718f9c',
                                      command=read_more_window.destroy)
    read_more_window_text.pack()


# configure main window
root = tk.Tk()
root.title('Password strength checker')
root.geometry('600x760')
root.resizable(False, False)
root.config(background='#383f40')

# create title and entry box for password
title_label = tk.Label(root, text='Password strength checker', font='Futura 28', foreground='#ffffff',
                       background='#383f40')
title_label.pack(pady=15)

password_entry = tk.Entry(root, width=30, font='Futura 20', foreground='#ffffff', background='#718f9c')
password_entry.pack(pady=15)

# create label frame with info about containing certain characters in password
char_info_label = tk.LabelFrame(root, background='#383f40', borderwidth=0)
char_info_label.pack()

is_lowercase = tk.Label(char_info_label, text='lowercase', font='Futura 12', foreground='#ffffff', background='#383f40')
is_lowercase.grid(row=0, column=0, padx=10)

is_uppercase = tk.Label(char_info_label, text='uppercase', font='Futura 12', foreground='#ffffff', background='#383f40')
is_uppercase.grid(row=0, column=1, padx=10)

is_digit = tk.Label(char_info_label, text='digits', font='Futura 12', foreground='#ffffff', background='#383f40')
is_digit.grid(row=0, column=2, padx=10)

is_special = tk.Label(char_info_label, text='special characters', font='Futura 12', foreground='#ffffff',
                      background='#383f40')
is_special.grid(row=0, column=3, padx=10)

# button to check password and strength bar showing how secure is password with text info - very weak, weak etc.
check_button = tk.Button(root, text='Check password', font='Futura 12', foreground='#ffffff', background='#718f9c',
                         command=check_password_strength)
check_button.pack(pady=15)

strength_bar = ttk.Progressbar(root, length=450)
strength_bar.pack(pady=15)

info_text = tk.Label(root, text='', font='Futura 20', foreground='#ffffff', background='#383f40')
info_text.pack()

# create label with info about weak password and button to another window with info about how create strong password
read_more_label = tk.LabelFrame(root, borderwidth=0, background='#383f40')
read_more_label.pack()

info_password_label = tk.Label(read_more_label, text='Password too weak?', font='Futura 12', foreground='#ffffff',
                               background='#383f40')
info_password_label.grid(row=0, column=0, pady=(15, 0), padx=(0, 15))

read_more_button = tk.Button(read_more_label, text='Read more', font='Futura 8', foreground='#ffffff',
                             background='#718f9c', command=read_more)
read_more_button.grid(row=0, column=1,  pady=(15, 0))

# place where you can create own strong (or weak ;P) password
proposal_password_info = tk.Label(root, text='Password generator', font='Futura 20', foreground='#ffffff',
                                  background='#383f40')
proposal_password_info.pack(pady=(30, 15))

proposal_password_label = tk.Label(root, text='', font='Futura 20', foreground='#ffffff', background='#383f40')
proposal_password_label.pack(pady=15)

# label frame with generate password and copy password buttons
copy_generate_label = tk.LabelFrame(root, borderwidth=0, background='#383f40')
copy_generate_label.pack()

generate_password = tk.Button(copy_generate_label, text='Generate password', font='Futura 12', foreground='#ffffff',
                              background='#718f9c', command=password_gen)
generate_password.grid(row=0, column=0, padx=(0, 15), pady=15)

copy_password_button = tk.Button(copy_generate_label, text='Copy', font='Futura 12', foreground='#ffffff',
                                 background='#718f9c', command=copy_password)
copy_password_button.grid(row=0, column=1, pady=15)

checkbox_frame = tk.LabelFrame(root, borderwidth=0, background='#383f40')
checkbox_frame.pack(pady=(15, 30))

checkbox_lower_var = tk.IntVar()
checkbox_lower = tk.Checkbutton(checkbox_frame, text='lowercase', font='Futura 12', foreground='#ffffff',
                                background='#383f40', activebackground='#383f40', activeforeground='#baff99',
                                selectcolor='#718f9c', onvalue=True, offvalue=False, command=password_gen,
                                variable=checkbox_lower_var)
checkbox_lower.grid(row=0, column=0, padx=10)

checkbox_upper_var = tk.IntVar()
checkbox_upper = tk.Checkbutton(checkbox_frame, text='uppercase', font='Futura 12', foreground='#ffffff',
                                background='#383f40', activebackground='#383f40', activeforeground='#baff99',
                                selectcolor='#718f9c', onvalue=True, offvalue=False, command=password_gen,
                                variable=checkbox_upper_var)
checkbox_upper.grid(row=0, column=1, padx=10)

checkbox_digit_var = tk.IntVar()
checkbox_digit = tk.Checkbutton(checkbox_frame, text='digits', font='Futura 12', foreground='#ffffff',
                                background='#383f40', activebackground='#383f40', activeforeground='#baff99',
                                selectcolor='#718f9c', onvalue=True, offvalue=False, command=password_gen,
                                variable=checkbox_digit_var)
checkbox_digit.grid(row=0, column=2, padx=10)

checkbox_special_var = tk.IntVar()
checkbox_special = tk.Checkbutton(checkbox_frame, text='special characters', font='Futura 12', foreground='#ffffff',
                                  background='#383f40', activebackground='#383f40', activeforeground='#baff99',
                                  selectcolor='#718f9c', onvalue=True, offvalue=False, command=password_gen,
                                  variable=checkbox_special_var)
checkbox_special.grid(row=0, column=3, padx=10)

slider = tk.Scale(master=root, from_=12, to=44, length=450, command=password_gen,
                  orient='horizontal', resolution=1, borderwidth=0, foreground='#ffffff', background='#718f9c')
slider.pack()

root.mainloop()
