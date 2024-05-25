from cProfile import label
from cgitb import text
from curses import newwin
from curses.panel import bottom_panel
from email import message
from hmac import new
from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD
from turtle import back

from distutils.command.clean import clean


def anuluj(button1,button2,label,entry):
    global newwindow
    button1.destroy()
    button2.destroy()
    label.destroy()
    entry.destroy()

    button1 = Button(newwindow, text="Wpłać",command=lambda:wplac(button2,button1))
    button2 = Button(newwindow, text="Wypłać",command=lambda:wyplac(button1,button2))
    button3 = Button(newwindow, text="Wyloguj", command=logout)
    button1.place(anchor='center', relx=0.4, rely=0.6)
    button2.place(anchor='center', relx=0.6, rely=0.6)
    button3.place(anchor='center', relx=0.5, rely=0.9)



def wyplac(widget1,widget2):
    global newwindow
    widget1.destroy()
    widget2.destroy()

    label = Label(newwindow,text="Podaj kwotę: ",font=("Arial",8,"bold"),bg='Black',fg='Green')
    label.place(anchor='center',relx=0.5,rely=0.5)
    entry = Entry(newwindow)
    entry.place(anchor='center',relx=0.5,rely=0.55)

    button = Button(newwindow,text="Zatwierdź")
    button.place(anchor='center',relx=0.4,rely=0.8)

    button1 = Button(newwindow,text="Anuluj",command=lambda:anuluj(button1,button,label,entry))
    button1.place(anchor='center',relx=0.6,rely=0.8)




def wplac(widget1,widget2):
    global newwindow

    widget1.destroy()
    widget2.destroy()

    button = Button(newwindow,text="Zatwierdź")
    button.place(anchor='center',relx=0.4,rely=0.8)

    button1 = Button(newwindow,text="Anuluj",command=lambda:anuluj(button,button1,label1,lista))
    button1.place(anchor='center',relx=0.6,rely=0.8)


    label1 = Label(newwindow,text="Wybierz nominał: ",font=("Arial",8,"bold"),bg='Black',fg='Green')
    label1.place(anchor='center',relx=0.5,rely=0.5)
    lista = Listbox(newwindow,height=3,selectmode=SINGLE)
    lista.insert(1,"10zł")
    lista.insert(2,"20zł")
    lista.insert(3,"50zł")
    lista.insert(4,"100zł")
    lista.insert(5,"200zł")
    lista.insert(6,"500zł")


    lista.place(anchor='center',relx=0.5,rely=0.6)


def exit():
    window.destroy()

def logout():
    global window, newwindow
    newwindow.destroy()
    window = Tk()
    setup_main_window()

def submit():
    username = entry.get()
    password = entry2.get()
    if username == "1" and password == "1" :
        messagebox.showinfo("Bankomat", "Zalogowano!")  
        OpenWindow1()
    else:
        messagebox.showerror("Bankomat", "Login Failed!\nInvalid username or password")

def OpenWindow1():
    global newwindow, window
    
    window.destroy()
    newwindow = Tk()
    newwindow.geometry("500x500")
    newwindow.title("Bankomat")
    newwindow.config(background="Black")
    newwindow.eval('tk::PlaceWindow . center')

    label = Label(newwindow,
                  text="Bankomat",
                  font=('Arial', 20, 'bold'),
                  bg='Black',
                  fg='Green',
                  relief=RAISED,
                  bd=10,
                  padx=20,
                  pady=20)
    label.pack()
    label.place(relx=0.5, rely=0.3, anchor="center")

    label2 = Label(newwindow,text="Saldo: 1 000 000$ ",
                   font=('Arial',12,'bold'),
                   bg='Black',
                   fg='Green')
    label2.place(anchor='center',relx=0.5,rely=0.45)


    button1 = Button(newwindow, text="Wpłać",command=lambda:wplac(button2,button1))
    button2 = Button(newwindow, text="Wypłać",command=lambda:wyplac(button1,button2))
    button3 = Button(newwindow, text="Wyloguj", command=logout)
    button1.place(anchor='center', relx=0.4, rely=0.6)
    button2.place(anchor='center', relx=0.6, rely=0.6)
    button3.place(anchor='center', relx=0.5, rely=0.9)

        

    newwindow.mainloop()


def setup_main_window():
    global entry
    global entry2
    window.geometry("500x500")
    window.title("Bankomat")
    window.eval('tk::PlaceWindow . center')

    
    window.config(background="Black")

    label = Label(window,
                  text="Bankomat",
                  font=('Arial', 20, 'bold'),
                  bg='Black',
                  fg='Green',
                  relief=RAISED,
                  bd=10,
                  padx=20,
                  pady=20)
    label.pack()
    label.place(relx=0.5, rely=0.3, anchor="center")

    label1 = Label(window, text="Login",
                   font=('Arial', 8, 'bold'),
                   bg='Black',
                   fg='Green',
                   compound='bottom')
    label1.place(anchor='center', relx=0.4, rely=0.45)

    label2 = Label(window, text="Hasło",
                   font=('Arial', 8, 'bold'),
                   bg='Black',
                   fg='Green',
                   compound='bottom')
    label2.place(anchor='center', relx=0.4, rely=0.55)


    entry2 = Entry(window,font=("Arial",10),show="*")
    entry2.place(anchor='center',relx=0.5,rely=0.6)    

    entry = Entry(window, font=("Arial", 10))
    entry.place(anchor='center', relx=0.5, rely=0.5)
    

    button2 = Button(window, text="Zaloguj się", command=submit)
    button2.place(anchor='center', relx=0.5, rely=0.7)
    button3 = Button(window,text="Wyjdź",command=exit)
    button3.place(relx=0.5,rely=0.9,anchor='center')

    window.mainloop()

window = Tk()
setup_main_window()



