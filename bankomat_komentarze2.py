from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD

# Funkcja do anulowania operacji i powrotu do menu głównego
# Usuwa przyciski i pola wprowadzenia danych z ekranu, a następnie przywraca menu główne
def anuluj(button1, button2, label, entry):
    button1.destroy()
    button2.destroy()
    label.destroy()
    entry.destroy()
    wroc_do_menu()

# Funkcja do wyświetlenia menu głównego
# Tworzy i umieszcza przyciski dla opcji "Wpłać", "Wypłać" oraz "Wyloguj"
def wroc_do_menu():
    global newwindow
    button1 = Button(newwindow, text="Wpłać", command=lambda: wplac(button2, button1))
    button2 = Button(newwindow, text="Wypłać", command=lambda: wyplac(button1, button2))
    button3 = Button(newwindow, text="Wyloguj", command=logout)
    button1.place(anchor='center', relx=0.4, rely=0.6)
    button2.place(anchor='center', relx=0.6, rely=0.6)
    button3.place(anchor='center', relx=0.5, rely=0.9)

# Funkcja do obsługi wypłaty
# Usuwa przyciski menu i wyświetla pola do wprowadzenia kwoty oraz przyciski do zatwierdzenia lub anulowania operacji
def wyplac(widget1, widget2):
    global newwindow
    widget1.destroy()
    widget2.destroy()
    label = Label(newwindow, text="Podaj kwotę: ", font=("Arial", 8, "bold"), bg='Black', fg='Green')
    label.place(anchor='center', relx=0.5, rely=0.5)
    entry = Entry(newwindow)
    entry.place(anchor='center', relx=0.5, rely=0.55)
    button = Button(newwindow, text="Zatwierdź", command=lambda: zatwierdz_wyplate(entry.get(), label, entry, button, anuluj_button))
    button.place(anchor='center', relx=0.4, rely=0.8)
    anuluj_button = Button(newwindow, text="Anuluj", command=lambda: anuluj(button, anuluj_button, label, entry))
    anuluj_button.place(anchor='center', relx=0.6, rely=0.8)

# Funkcja do zatwierdzenia wypłaty
# Sprawdza dostępność środków, aktualizuje saldo użytkownika i informuje o sukcesie lub błędzie
def zatwierdz_wyplate(kwota, label, entry, button, anuluj_button):
    global saldo, username
    try:
        kwota = float(kwota)
        if kwota > float(saldo):
            messagebox.showerror("Błąd", "Nie masz wystarczających środków.")
            return
        saldo = str(float(saldo) - kwota)
        update_saldo(username, saldo)
        saldo_label.config(text=f"Saldo: {saldo} ")
        messagebox.showinfo("Bankomat", "Wypłata zakończona sukcesem!")
        button.destroy()
        anuluj_button.destroy()
        label.destroy()
        entry.destroy()
        wroc_do_menu()
    except ValueError:
        messagebox.showerror("Błąd", "Podaj poprawną kwotę.")

# Funkcja do obsługi wpłaty
# Usuwa przyciski menu i wyświetla pola do wyboru nominału oraz przyciski do zatwierdzenia lub anulowania operacji
def wplac(widget1, widget2):
    global newwindow
    widget1.destroy()
    widget2.destroy()
    label1 = Label(newwindow, text="Wybierz nominał: ", font=("Arial", 8, "bold"), bg='Black', fg='Green')
    label1.place(anchor='center', relx=0.5, rely=0.5)
    lista = Listbox(newwindow, height=3, selectmode=SINGLE)
    lista.insert(1, "10")
    lista.insert(2, "20")
    lista.insert(3, "50")
    lista.insert(4, "100")
    lista.insert(5, "200")
    lista.insert(6, "500")
    lista.place(anchor='center', relx=0.5, relx=0.6)
    zatwierdz_button = Button(newwindow, text="Zatwierdź", command=lambda: zatwierdz_wplate(lista.get(ACTIVE), label1, lista, zatwierdz_button, anuluj_button))
    zatwierdz_button.place(anchor='center', relx=0.4, rely=0.8)
    anuluj_button = Button(newwindow, text="Anuluj", command=lambda: anuluj(zatwierdz_button, anuluj_button, label1, lista))
    anuluj_button.place(anchor='center', relx=0.6, rely=0.8)

# Funkcja do zatwierdzenia wpłaty
# Aktualizuje saldo użytkownika i informuje o sukcesie lub błędzie
def zatwierdz_wplate(kwota, label, lista, button, anuluj_button):
    global saldo, username
    try:
        kwota = float(kwota)
        saldo = str(float(saldo) + kwota)
        update_saldo(username, saldo)
        saldo_label.config(text=f"Saldo: {saldo} ")
        messagebox.showinfo("Bankomat", "Wpłata zakończona sukcesem!")
        button.destroy()
        anuluj_button.destroy()
        label.destroy()
        lista.destroy()
        wroc_do_menu()
    except ValueError:
        messagebox.showerror("Błąd", "Podaj poprawną kwotę.")

# Funkcja do aktualizacji salda użytkownika w pliku
# Przeszukuje plik z danymi użytkowników i aktualizuje saldo dla zalogowanego użytkownika
def update_saldo(username, new_saldo):
    with open("plik.txt", 'r') as file:
        lines = file.readlines()
    with open("plik.txt", 'w') as file:
        for line in lines:
            dane = line.strip().split()
            if len(dane) == 3 and dane[0] == username:
                file.write(f"{dane[0]} {dane[1]} {new_saldo}\n")
            else:
                file.write(line)

# Funkcja do zamykania głównego okna
def exit():
    window.destroy()

# Funkcja do wylogowania użytkownika
# Zamyka obecne okno i przywraca okno logowania
def logout():
    global window, newwindow
    newwindow.destroy()
    window = Tk()
    setup_main_window()

# Funkcja do zalogowania użytkownika
# Sprawdza poprawność danych logowania i otwiera okno bankomatu w przypadku sukcesu
def submit():
    global username, saldo
    username = entry.get()
    password = entry2.get()
    try:
        with open("plik.txt", 'r') as file:
            zawartosc = file.readlines()
    except FileNotFoundError:
        print("File not found")
        return
    logged_in = False
    for linia in zawartosc:
        linia = linia.strip()
        dane = linia.split()
        if len(dane) == 3 and dane[0] == username and dane[1] == password:
            saldo = dane[2]
            messagebox.showinfo("Bankomat", "Zalogowano!")  
            OpenWindow1(saldo)
            logged_in = True
            break
    if not logged_in:
        messagebox.showerror("Bankomat", "Login Failed!\nInvalid username or password")

# Funkcja do otwarcia okna bankomatu po zalogowaniu
# Tworzy nowe okno bankomatu i wyświetla saldo oraz przyciski do wpłaty, wypłaty i wylogowania
def OpenWindow1(saldo):
    global newwindow, window, saldo_label
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
    saldo_label = Label(newwindow, text=f"Saldo: {saldo} ", font=('Arial', 12, 'bold'), bg='Black', fg='Green')
    saldo_label.place(anchor='center', relx=0.5, rely=0.45)
    button1 = Button(newwindow, text="Wpłać", command=lambda: wplac(button2, button1))
    button2 = Button(newwindow, text="Wypłać", command=lambda: wyplac(button1, button2))
    button3 = Button(newwindow, text="Wyloguj", command=logout)
    button1.place(anchor='center', relx=0.4, rely=0.6)
    button2.place(anchor='center', relx=0.6, rely=0.6)
    button3.place(anchor='center', relx=0.5, rely=0.9)
    newwindow.mainloop()

# Funkcja do konfiguracji głównego okna logowania
# Tworzy pola do wprowadzenia nazwy użytkownika i hasła oraz przycisk do zalogowania się
def setup_main_window():
    global entry, entry2
    window.geometry("500x500")
    # Kontynuacja konfiguracji okna logowania...
