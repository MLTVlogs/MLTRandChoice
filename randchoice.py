import mod.gui_en as en
import mod.gui_es as es
import tkinter as tk
from tkinter.font import Font
from tkinter import ttk

#GLOBAL CONSTANTS--------------------
TITLESIZE = 24
TITLEWEIGHT = "normal"

#COMMANDS--------------------
def gotolang(window,op):
    """
    Destroys the current window and calls the main function of the specified language module.

    Parameters:
    window: The window instance to be destroyed.
    op (int): An integer representing the language option. 
            If op is 1, the English module's main function is called.
            If op is 2, the Spanish module's main function is called.
    """
    window.destroy()
    if op == 1:
        en.main()
    if op == 2:
        es.main()

#MAIN--------------------
#Creating a Window
window = tk.Tk()
icon = tk.PhotoImage(file="artwork//favicon.png")

#Title of the Window
window.iconphoto(False,icon)
window.title("MLT RandChoice")
window.resizable(False,False)

#Defining Fonts
titlefont = Font(size=TITLESIZE, 
                weight=TITLEWEIGHT)

#PANELS
#Mainpanel
mainframe = ttk.Frame(window)
mainframe.grid(padx=10,pady=10)

#Title
title = ttk.Label(mainframe, text="MLT RANDCHOICE", font=titlefont)
title.grid(padx=10,pady=10)

#Message
message = ttk.Label(mainframe, text="Select a language")
message.grid(padx=10)

#RADIOBUTTONS
#Radio Button Buttons
op = tk.IntVar()

#Radio Button English
eng = ttk.Radiobutton(mainframe, text="English", variable=op, value=1)
eng.grid(padx=10)

#Radio Button Spanish
esp = ttk.Radiobutton(mainframe, text="Spanish", variable=op, value=2)
esp.grid(padx=10)

#Button 1
button = ttk.Button(mainframe, text="OK", width=20, command=lambda:gotolang(window, op.get()))
button.grid(padx=10,pady=10)

#Stay Open the Window
tk.mainloop()