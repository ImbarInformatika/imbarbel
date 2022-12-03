import tkinter
from tkinter import *

jar = Tk()
jar.title("LOGIN")
jar.geometry('400x300')

judul = Label(judulk, text="Please enter details below", bg="black",fg="white")
judul.place(x=150, y=10)
judulk = Frame(jar, width = 200, height = 20, bg="black")
judulk.place(x=1, y=10)

username = Label(jar, text="Username * ")
username.place(x=70, y=50)

username = Entry(jar, width=25)
username.place(x=150, y=50)

password = Label(jar, text="Password * ")
password.place(x=70, y=100)

password = Entry(jar, width=25)
password.place(x=150, y=100)

teks = Label(jar, text="fill the empty field!!!!")
teks.place(x=160, y=120)

login = Button(text="Login", bg="black", fg="white", width=15)
login.place(x=160, y=160)
jar.mainloop()
