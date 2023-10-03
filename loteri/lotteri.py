from tkinter import *
from tkinter import messagebox
import lotteri2


root = Tk()
root.title("lotteri")

Listbox = Listbox (root, height = 4,
                   width = 30,
                   bg = "white",
                   activestyle = "dotbox",
                   font = "Helvetica",
                   fg = "blue")

root.geometry("380x300")

lotteri2 = lotteri2.lotteri ()

Label_antal = Label (root, text = "Antal Lotter, max 3st :")
Label_antal.grid (row=0, column=0, sticky=E, padx=5, pady=5)

textbox_antal = Entry (root, width=2)
textbox_antal.grid (row=0, column=1, sticky=W, padx=5, pady=5)
textbox_antal.focus_set()

def update_listbox (antal_lotter):

    Listbox.delete (0, END)

    Listbox.insert (1, "Grattis du vann det här!")

    try:
        int_antal_lotter = int (antal_lotter)
        i = 0
        if (int_antal_lotter < 4) :
            while i < int_antal_lotter:
                vinst = lotteri2.get_vinst ()
                Listbox.insert ( (i+2), vinst )
                i += 1

        elif (int_antal_lotter > 3) :
            messagebox.showinfo ("Du har valt för många lotter!")

    except ValueError: messagebox.showinfo ("Endast sifror tillåtna!")

def clickSlumpaButton () : 
    antal_lott = textbox_antal.get ()
    textbox_antal.delete (0, END)
    textbox_antal.focus_set()
    update_listbox (antal_lott)

Button_slumpa = Button (text="Tur Knapp", command = clickSlumpaButton)
Button_slumpa.grid (row=2, column=0, sticky=E, padx=15, pady=15)

Listbox.grid (row=2, column=0, columnspan=2, padx=15, pady=15)


root.mainloop()