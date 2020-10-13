from tkinter import *
from tkinter import Image, PhotoImage, Canvas

import random
import string
import tkinter.messagebox
import secrets
import uuid

window = Tk()

window.title("Password Generator")
window.geometry('370x500')

lbl = Label(window, text="Please choose the type of password you want to generate:")
lbl.grid()


# 6 character pw
lblsix = Label(window, text = "6 Character Passwords", relief=GROOVE)
lblsix.grid(column=0, row=1)

def simple_six_char_pass():
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(6))
    tkinter.messagebox.showinfo('Simple Password', result_str)


simpleSixCharPw = Button(window, text="Simple 6 character pw", fg="black", command=simple_six_char_pass)
simpleSixCharPw.grid(column=0, row=2)


def complex_six_char_pass():
    letters = string.ascii_letters + string.digits
    result_str = ''.join(random.choice(letters) for i in range(6))
    tkinter.messagebox.showinfo('Complex Password', result_str)


complexSixCharPw = Button(window, text="Complex 6 character pw", fg="black", command=complex_six_char_pass)
complexSixCharPw.grid(column=0, row=3)


def sophisticated_six_char_pass():
    letters = string.ascii_letters + string.digits + string.punctuation
    result_str = ''.join(random.choice(letters) for i in range(6))
    tkinter.messagebox.showinfo('Sophisticated Password', result_str)


sophisticatedSixCharPw = Button(window, text="Sophisticated 6 character pw", fg="black", command=sophisticated_six_char_pass)
sophisticatedSixCharPw.grid(column=0, row=4)

lblempty = Label(window)
lblempty.grid(column=0, row=5)


# 8 character pw
lbleight = Label(window, text = "8 Character Passwords", relief=GROOVE)
lbleight.grid(column=0, row=6)


def simple_eight_char_pass():
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(8))
    tkinter.messagebox.showinfo('Simple Password', result_str)


simpleEightCharPw = Button(window, text="Simple 8 character pw", fg="black", command=simple_eight_char_pass)
simpleEightCharPw.grid(column=0, row=7)


def complex_eight_char_pass():
    letters = string.ascii_letters + string.digits
    result_str = ''.join(random.choice(letters) for i in range(8))
    tkinter.messagebox.showinfo('Complex Password', result_str)


complexEightCharPw = Button(window, text="Complex 8 character pw", fg="black", command=complex_eight_char_pass)
complexEightCharPw.grid(column=0, row=8)


def sophisticated_eight_char_pass():
    letters = string.ascii_letters + string.digits + string.punctuation
    result_str = ''.join(random.choice(letters) for i in range(8))
    tkinter.messagebox.showinfo('Sophisticated Password', result_str)


sophisticatedEightCharPw = Button(window, text="Sophisticated 8 character pw", fg="black", command=sophisticated_eight_char_pass)
sophisticatedEightCharPw.grid(column=0, row=9)


lblempty2 = Label(window)
lblempty2.grid(column=0, row=10)

lblgtnsrs = Label(window, text="GETTING SERIOUS", fg="red", relief=GROOVE)
lblgtnsrs.grid(column=0, row=11)


def complex_twelve_char_pass():
    letters = string.ascii_letters + string.digits
    result_str = ''.join(random.choice(letters) for i in range(12))
    tkinter.messagebox.showinfo('Complex Password', result_str)


complexEightCharPw = Button(window, text="Complex 12 character pw", fg="black", command=complex_twelve_char_pass)
complexEightCharPw.grid(column=0, row=12)


def sophisticated_twelve_char_pass():
    letters = string.ascii_letters + string.digits + string.punctuation
    result_str = ''.join(random.choice(letters) for i in range(12))
    tkinter.messagebox.showinfo('Sophisticated Password', result_str)


sophisticatedEightCharPw = Button(window, text="Sophisticated 12 character pw", fg="black",
                                  command=sophisticated_twelve_char_pass)
sophisticatedEightCharPw.grid(column=0, row=13)


def absurdly_long_pw():
    letters = string.ascii_letters + string.digits + string.punctuation
    result_str = ''.join(random.choice(letters) for i in range(120))
    tkinter.messagebox.showinfo('Absurdly Long Password', result_str)


absurdpw = Button(window, text="ABSURDLY LONG COMPLICATED PASSWORD", fg="red", command=absurdly_long_pw)
absurdpw.grid(column=0, row=14)


lblempty3 = Label(window)
lblempty3.grid(column=0, row=15)


# EXTRAS
lblgtnsrs = Label(window, text="Extras", fg="green", relief=GROOVE)
lblgtnsrs.grid(column=0, row=16)


def secure_hexadecimal_token():
    scrhex = secrets.token_hex(32)
    tkinter.messagebox.showinfo('Secure hexadecimal token', scrhex)


scrhexpw = Button(window, text="Secure hexadecimal token", fg="black", command=secure_hexadecimal_token)
scrhexpw.grid(column=0, row=17)


def universally_u_id():
    idstring = uuid.uuid4()
    tkinter.messagebox.showinfo('UUID', idstring)


uuidpw = Button(window, text="UUID", fg="black", command=universally_u_id)
uuidpw.grid(column=0, row=18)


lblempty4 = Label(window)
lblempty4.grid(column=0, row=19)


lblmadeby = Label(window, text="Made by Pelvis Fresley")
lblmadeby.grid(column=0, row=20)


window.mainloop()