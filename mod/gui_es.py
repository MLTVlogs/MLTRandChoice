import random
import mod.oplist as opls
import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from tkinter import messagebox as mb

#GLOBAL CONSTANTS & VARIABLES--------------------
TITLESIZE = 24
SUBTITLESIZE = 18
TITLEWEIGHT = "normal"

#GUI MANAGEMENT--------------------
#Main Menu
def main():
    """MAIN

    Main menu gui for the program
    """
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
    mainpanel = ttk.Frame(window)
    mainpanel.grid(padx=10,pady=10)

    #Panel 1
    panel1 = ttk.Frame(mainpanel)
    panel1.grid(row=0)

    #Panel 2
    panel2 = ttk.Frame(mainpanel)
    panel2.grid(row=1)

    #Panel 3
    panel3 = ttk.Frame(mainpanel)
    panel3.grid(row=2)

    #Title
    title = ttk.Label(panel1,text="MLT RANDCHOICE",font=titlefont)
    title.grid(padx=10,pady=10)

    #Button1 (New List)
    button1 = ttk.Button(panel2,text="Nueva Lista",width=20,command=lambda:newlist(window))
    button1.grid(column=0,row=0,padx=4,pady=4)

    #Button2 (Open List)
    button2 = ttk.Button(panel2,text="Abrir Lista",width=20,command=lambda:openlist(window))
    button2.grid(column=1,row=0,padx=4,pady=4)

    #Button3 (Delete List)
    button3 = ttk.Button(panel3,text="Renombrar Lista",width=20,command=lambda:renamelist(window))
    button3.grid(column=0,row=0,padx=4,pady=4)

    #Button3 (Delete List)
    button4 = ttk.Button(panel3,text="Eliminar Lista",width=20,command=lambda:deletelist(window))
    button4.grid(column=1,row=0,padx=4,pady=4)

    #Stay Open the Window
    tk.mainloop()

#New List Menu
def newlist(mainmenu):
    """NEWLIST

    menu gui for creating a new list of options

    -Args-
    - mainmenu: the tkinter root"""

    #Delete The previous content of the window
    mainmenu.destroy()

    #Creating a Window
    window = tk.Tk()
    icon = tk.PhotoImage(file="artwork//favicon.png")

    #Title of the Window
    window.iconphoto(False,icon)
    window.title("MLT RandChoice")
    window.resizable(False,False)

    #Defining Fonts
    subtitlefont = Font(size=SUBTITLESIZE, 
                    weight=TITLEWEIGHT)
    
    #PANELS
    #Mainpanel
    mainpanel = ttk.Frame(window)
    mainpanel.grid(padx=10,pady=10)

    #Panel 1
    panel1 = ttk.Frame(mainpanel)
    panel1.grid(row=0)

    #Panel 2
    panel2 = ttk.Frame(mainpanel)
    panel2.grid(row=1)

    #Panel 3
    panel3 = ttk.Frame(mainpanel)
    panel3.grid(row=3)

    #Title
    title = ttk.Label(panel1,text="NUEVA LISTA",font=subtitlefont)
    title.grid()

    #Textbox
    textbox = ttk.Entry(panel2,width=40)
    textbox.grid(row=0,column=1,padx=4,pady=4)

    tbLabel = ttk.Label(panel2,text="Nombre:")
    tbLabel.grid(row=0,column=0,padx=4,pady=4)

    #Button1 (Create)
    button1 = ttk.Button(panel3,text="Crear",command=lambda:create(textbox.get(),window))
    button1.grid(row=0,column=0,padx=4,pady=4)

    #Button2 (Create)
    button2 = ttk.Button(panel3,text="Cancelar",command=lambda:backtomain(window))
    button2.grid(row=0,column=1,padx=4,pady=4)

    #Stay Open the Window
    tk.mainloop()

#Open List Menu
def openlist(mainmenu):
    """OPENLIST

    menu gui for open a list

    -Args-
    - mainmenu: the tkinter root"""
    #Delete The previous content of the window
    mainmenu.destroy()

    #Creating a Window
    window = tk.Tk()
    icon = tk.PhotoImage(file="artwork//favicon.png")

    #Title of the Window
    window.iconphoto(False,icon)
    window.title("MLT RandChoice")
    window.resizable(False,False)

    #Defining Fonts
    subtitlefont = Font(size=SUBTITLESIZE, 
                    weight=TITLEWEIGHT)
    
    #List of option lists
    oplists = opls.getoplists()
    oplists.sort()
    
    #PANELS
    #Mainframe
    mainframe = ttk.Frame(window)
    mainframe.grid(padx=10, pady=10)

    #Panel 1
    panel1 = ttk.Frame(mainframe)
    panel1.grid(row=0)

    #Panel 2
    panel2 = ttk.Frame(mainframe)
    panel2.grid(row=1)

    #Panel 3
    panel3 = ttk.Frame(mainframe)
    panel3.grid(row=2)

    #Title
    title = ttk.Label(panel1,text="ABRIR LISTA",font=subtitlefont)
    title.grid()

    #Combobox
    combobox = ttk.Combobox(panel2,width=40,values=oplists,state="readonly")
    combobox.grid(padx=4,pady=4)

    #Button Delete/OK
    button1 = ttk.Button(panel3,text="Abrir",width=20,command=lambda:open(combobox.get(),window))
    button1.grid(column=0,row=0,padx=4,pady=4)

    #Button Cancel
    button2 = ttk.Button(panel3,text="Cancelar",width=20,command=lambda:backtomain(window))
    button2.grid(column=1,row=0,padx=4,pady=4)

    #Stay Open the Window
    window.mainloop()

#Rename List Menu
def renamelist(mainmenu):
    """RENAMELIST

    menu gui for rename a list

    -Args-
    - mainmenu: the tkinter root"""

    #Delete The previous content of the window
    mainmenu.destroy()

    #Creating a Window
    window = tk.Tk()
    icon = tk.PhotoImage(file="artwork//favicon.png")

    #Title of the Window
    window.iconphoto(False,icon)
    window.title("MLT RandChoice")
    window.resizable(False,False)

    #Defining Fonts
    subtitlefont = Font(size=SUBTITLESIZE, 
                    weight=TITLEWEIGHT)
    
    #List of option lists
    oplists = opls.getoplists()
    oplists.sort()

    #PANELS
    #Mainframe
    mainframe = ttk.Frame(window)
    mainframe.grid(padx=10, pady=10)

    #Panel 1
    panel1 = ttk.Frame(mainframe)
    panel1.grid(row=0)

    #Panel 2
    panel2 = ttk.Frame(mainframe)
    panel2.grid(row=1)

    #Panel 3
    panel3 = ttk.Frame(mainframe)
    panel3.grid(row=2)

    #Panel 4
    panel4 = ttk.Frame(mainframe)
    panel4.grid(row=3)

    #Title
    title = ttk.Label(panel1,text="RENOMBRAR LISTA",font=subtitlefont)
    title.grid()

    #Combobox
    combobox = ttk.Combobox(panel2,width=40,values=oplists,state="readonly")
    combobox.grid(padx=4,pady=4)

    #Textbox
    textbox = ttk.Entry(panel3,width=35)
    textbox.grid(row=0,column=1,padx=4,pady=4)

    tbLabel = ttk.Label(panel3,text="Nombre:")
    tbLabel.grid(row=0,column=0,padx=4,pady=4)

    #Button Delete/OK
    button1 = ttk.Button(panel4,text="Renombrar",width=20,command=lambda:rename(combobox.get(),textbox.get(),window))
    button1.grid(column=0,row=0,padx=4,pady=4)

    #Button Cancel
    button2 = ttk.Button(panel4,text="Cancelar",width=20,command=lambda:backtomain(window))
    button2.grid(column=1,row=0,padx=4,pady=4)

    #Stay Open the Window
    window.mainloop() 

#Delete List Menu
def deletelist(mainmenu):
    """DELETELIST

    menu gui for delete a list

    -Args-
    - mainmenu: the tkinter root"""

    #Delete The previous content of the window
    mainmenu.destroy()

    #Creating a Window
    window = tk.Tk()
    icon = tk.PhotoImage(file="artwork//favicon.png")

    #Title of the Window
    window.iconphoto(False,icon)
    window.title("MLT RandChoice")
    window.resizable(False,False)

    #Defining Fonts
    subtitlefont = Font(size=SUBTITLESIZE, 
                    weight=TITLEWEIGHT)
    
    #List of option lists
    oplists = opls.getoplists()
    oplists.sort()

    #PANELS
    #Mainframe
    mainframe = ttk.Frame(window)
    mainframe.grid(padx=10, pady=10)

    #Panel 1
    panel1 = ttk.Frame(mainframe)
    panel1.grid(row=0)

    #Panel 2
    panel2 = ttk.Frame(mainframe)
    panel2.grid(row=1)

    #Panel 3
    panel3 = ttk.Frame(mainframe)
    panel3.grid(row=2)

    #Title
    title = ttk.Label(panel1,text="ELIMINAR LISTA",font=subtitlefont)
    title.grid()

    #Combobox
    combobox = ttk.Combobox(panel2,width=40,values=oplists,state="readonly")
    combobox.grid(padx=4,pady=4)

    #Button Delete/OK
    button1 = ttk.Button(panel3,text="Eliminar",width=20,command=lambda:delete(combobox.get(),window))
    button1.grid(column=0,row=0,padx=4,pady=4)

    #Button Cancel
    button2 = ttk.Button(panel3,text="Cancelar",width=20,command=lambda:backtomain(window))
    button2.grid(column=1,row=0,padx=4,pady=4)

    #Stay Open the Window
    window.mainloop()

#(openlist) Main List Menu
def mainlist(mainmenu,oplist):
    """MAINLIST

    list main menu gui for the program

    -Args-
    - mainmenu: the tkinter root
    - oplist: the name of the option list
    """
    #Delete The previous content of the window
    mainmenu.destroy()

    #Creating a Window
    window = tk.Tk()
    icon = tk.PhotoImage(file="artwork//favicon.png")

    #Title of the Window
    window.iconphoto(False,icon)
    window.title("MLT RandChoice")
    window.resizable(False,False)

    #Defining Fonts
    subtitlefont = Font(size=SUBTITLESIZE, 
                    weight=TITLEWEIGHT)
    
    #PANELS
    #Mainpanel
    mainpanel = ttk.Frame(window)
    mainpanel.grid(padx=10,pady=10)

    #Panel 1
    panel1 = ttk.Frame(mainpanel)
    panel1.grid(row=1)

    #Panel 2
    panel2 = ttk.Frame(mainpanel)
    panel2.grid(row=2)

    #Panel 3
    panel3 = ttk.Frame(mainpanel)
    panel3.grid(row=3)

    #Title
    title = ttk.Label(mainpanel,text=oplist.upper(),font=subtitlefont)
    title.grid(row=0)

    #Button 1 (Select Option)
    button1 = ttk.Button(mainpanel,text="Seleccionar Opción",width=40,command=lambda:selectOp(window,oplist))
    button1.grid(row=1,padx=4,pady=4)
    if len(opls.getoptions(oplist)) == 0:
        button1.configure(state="disabled")

    #Button 2 (Add Option)
    button2 = ttk.Button(mainpanel,text="Añadir Opción",width=40,command=lambda:addOp(window,oplist))
    button2.grid(row=2,padx=4,pady=4)

    #Button 3 (Rename Option)
    button3 = ttk.Button(mainpanel,text="Renombrar Opción",width=40,command=lambda:renameOp(window,oplist))
    button3.grid(row=3,padx=4,pady=4)

    #Button 4 (Delete Option)
    button4 = ttk.Button(mainpanel,text="Eliminar Opción",width=40,command=lambda:deleteOp(window,oplist))
    button4.grid(row=4,padx=4,pady=4)

    #Button 5 (Delete Option)
    button5 = ttk.Button(mainpanel,text="Eliminar Todo",width=40,command=lambda:opempty(oplist,button1,button5))
    button5.grid(row=5,padx=4,pady=4)
    if len(opls.getoptions(oplist)) == 0:
        button5.configure(state="disabled")

    #Button 5 (Delete Option)
    button6 = ttk.Button(mainpanel,text="Cerrar Lista",width=40,command=lambda:backtomain(window))
    button6.grid(row=6,padx=4,pady=4)

    #Stay Open the Window
    tk.mainloop()

#(openlist) Select Option Menu
def selectOp(mainmenu,oplist):
    """SELECTOP

    Menu that selects randomly an option of a list

    -ARGS-
    - window: the tkinter root
    """

    #Delete The previous content of the window
    mainmenu.destroy()

    #Creating a Window
    window = tk.Tk()
    icon = tk.PhotoImage(file="artwork//favicon.png")

    #Title of the Window
    window.iconphoto(False,icon)
    window.title("MLT RandChoice")
    window.resizable(False,False)

    #Defining Fonts
    subtitlefont = Font(size=SUBTITLESIZE, 
                    weight=TITLEWEIGHT)
    
    #PANELS
    #Mainpanel
    mainpanel = ttk.Frame(window)
    mainpanel.grid(padx=10,pady=10)

    #Panel 1
    panel1 = ttk.Frame(mainpanel)
    panel1.grid(row=1)

    #Panel 2
    panel2 = ttk.Frame(mainpanel)
    panel2.grid(row=2)

    #Panel 3
    panel3 = ttk.Frame(mainpanel)
    panel3.grid(row=3)

    #Title
    title = ttk.Label(panel1, text="SELECCIONAR OPCIÓN", font=subtitlefont)
    title.grid(padx=10,pady=10)

    #Option Text
    optext = ttk.Label(panel1, text="Haz Click para Seleccionar")
    optext.grid(padx=10,pady=10)

    #Button1 (Create)
    button1 = ttk.Button(panel3,text="Seleccionar",command=lambda:opselect(oplist,optext,button1))
    button1.grid(row=0,column=0,padx=4,pady=4)

    #Button2 (Create)
    button2 = ttk.Button(panel3,text="Cerrar",command=lambda:mainlist(window,oplist))
    button2.grid(row=0,column=1,padx=4,pady=4)

    #Stay Open a Windos
    tk.mainloop()

#(openlist) Add Option Menu
def addOp(mainmenu,oplist):
    """ADDOP

    menu gui for add an option to the list

    -Args-
    - window: the tkinter root"""
    #Delete The previous content of the window
    mainmenu.destroy()

    #Creating a Window
    window = tk.Tk()
    icon = tk.PhotoImage(file="artwork//favicon.png")

    #Title of the Window
    window.iconphoto(False,icon)
    window.title("MLT RandChoice")
    window.resizable(False,False)

    #Defining Fonts
    subtitlefont = Font(size=SUBTITLESIZE, 
                    weight=TITLEWEIGHT)
    
    #PANELS
    #Mainframe
    mainframe = ttk.Frame(window)
    mainframe.grid(padx=10, pady=10)

    #Panel 1
    panel1 = ttk.Frame(mainframe)
    panel1.grid(row=0)

    #Panel 2
    panel2 = ttk.Frame(mainframe)
    panel2.grid(row=1)

    #Panel 3
    panel3 = ttk.Frame(mainframe)
    panel3.grid(row=2)

    #Title
    title = ttk.Label(panel1,text="AÑADIR OPCIÓN",font=subtitlefont)
    title.grid()

    #Textbox
    textbox = ttk.Entry(panel2,width=44)
    textbox.grid(row=0,column=1,padx=4,pady=4)

    #Button Delete/OK
    button1 = ttk.Button(panel3,text="Crear",width=20,command=lambda:opadd(textbox.get(),oplist,window))
    button1.grid(column=0,row=0,padx=4,pady=4)

    #Button Cancel
    button2 = ttk.Button(panel3,text="Cancelar",width=20,command=lambda:mainlist(window,oplist))
    button2.grid(column=1,row=0,padx=4,pady=4)

    #Stay Open the Window
    window.mainloop()    

#(openlist) Rename Option Menu
def renameOp(mainmenu,oplist):
    """RENAMEOP

    menu gui for rename a option of the list

    -Args-
    - window: the tkinter root"""

    #Delete The previous content of the window
    mainmenu.destroy()

    #Creating a Window
    window = tk.Tk()
    icon = tk.PhotoImage(file="artwork//favicon.png")

    #Title of the Window
    window.iconphoto(False,icon)
    window.title("MLT RandChoice")
    window.resizable(False,False)

    #Defining Fonts
    subtitlefont = Font(size=SUBTITLESIZE, 
                    weight=TITLEWEIGHT)
    
    #List of option lists
    options = opls.getoptions(oplist)
    options.sort()
    
    #PANELS
    #Mainframe
    mainframe = ttk.Frame(window)
    mainframe.grid(padx=10, pady=10)

    #Panel 1
    panel1 = ttk.Frame(mainframe)
    panel1.grid(row=0)

    #Panel 2
    panel2 = ttk.Frame(mainframe)
    panel2.grid(row=1)

    #Panel 3
    panel3 = ttk.Frame(mainframe)
    panel3.grid(row=2)

    #Panel 4
    panel4 = ttk.Frame(mainframe)
    panel4.grid(row=3)

    #Title
    title = ttk.Label(panel1,text="RENOMBRAR OPCIÓN",font=subtitlefont)
    title.grid()

    #Combobox
    combobox = ttk.Combobox(panel2,width=40,values=options,state="readonly")
    combobox.grid(padx=4,pady=4)

    #Textbox
    textbox = ttk.Entry(panel3,width=35)
    textbox.grid(row=0,column=1,padx=4,pady=4)

    tbLabel = ttk.Label(panel3,text="Nombre:")
    tbLabel.grid(row=0,column=0,padx=4,pady=4)

    #Button Delete/OK
    button1 = ttk.Button(panel4,text="Renombrar",width=20,command=lambda:oprename(combobox.get(),textbox.get(),oplist,window))
    button1.grid(column=0,row=0,padx=4,pady=4)

    #Button Cancel
    button2 = ttk.Button(panel4,text="Cancelar",width=20,command=lambda:mainlist(window,oplist))
    button2.grid(column=1,row=0,padx=4,pady=4)

    #Stay Open the Window
    window.mainloop()     

#(openlist) Delete Option Menu
def deleteOp(mainmenu,oplist):
    """DELETEOP

    menu gui for delete a option of the list

    -Args-
    - window: the tkinter root"""

    #Delete The previous content of the window
    mainmenu.destroy()

    #Creating a Window
    window = tk.Tk()
    icon = tk.PhotoImage(file="artwork//favicon.png")

    #Title of the Window
    window.iconphoto(False,icon)
    window.title("MLT RandChoice")
    window.resizable(False,False)

    #Defining Fonts
    subtitlefont = Font(size=SUBTITLESIZE, 
                    weight=TITLEWEIGHT)
    
    #List of option lists
    options = opls.getoptions(oplist)
    options.sort()
    
    #PANELS
    #Mainframe
    mainframe = ttk.Frame(window)
    mainframe.grid(padx=10, pady=10)

    #Panel 1
    panel1 = ttk.Frame(mainframe)
    panel1.grid(row=0)

    #Panel 2
    panel2 = ttk.Frame(mainframe)
    panel2.grid(row=1)

    #Panel 3
    panel3 = ttk.Frame(mainframe)
    panel3.grid(row=2)

    #Title
    title = ttk.Label(panel1,text="ELIMINAR OPCIÓN",font=subtitlefont)
    title.grid()

    #Combobox
    combobox = ttk.Combobox(panel2,width=40,values=options,state="readonly")
    combobox.grid(padx=4,pady=4)

    #Button Delete/OK
    button1 = ttk.Button(panel3,text="Eliminar",width=20,command=lambda:opdelete(combobox.get(),oplist,window))
    button1.grid(column=0,row=0,padx=4,pady=4)

    #Button Cancel
    button2 = ttk.Button(panel3,text="Cancelar",width=20,command=lambda:mainlist(window,oplist))
    button2.grid(column=1,row=0,padx=4,pady=4)

    #Stay Open the Window
    window.mainloop()  

#GUI COMMANDS--------------------
#Go Back to the Main Menu
def backtomain(window):
    """BACKTOMAIN

    procedure that bring back to the main menu

    -ARGS-

    - window: the tkinter root for exit"""
    try:
        window.destroy()
    except AttributeError:
        pass
    main()

#Create a list event
def create(oplist,window):
    """CREATE

    Event to create a option list and save it in a file with name of all lists.
    If a list is called "lists" and if a list exists, it shows a message box with
    its respective message.

    -ARGS-

    oplist: name of an option list.
    window: the tkinter root for exit.
    """
    #If a list exists
    if(opls.searchlist(oplist) == 1):
        mb.showinfo(title="Lista Existente",message=f"La lista de opciones \"{oplist}\" ya existe")
    #Create a new option
    elif(opls.searchlist(oplist) == 0):
        #If a list has as name "lists"
        if(oplist == "lists"):
            mb.showwarning(title="Nombre Reservado",message=f"\"lists\" es un nombre reservado")
        #If a list hasn't name
        elif(oplist == ""):
            backtomain(window)
        else:
            #Error Prevention
            if opls.writelist(oplist) == 0 or opls.createlist(oplist) == 0:
                mb.showerror(title="Error",message="Hay un error al crear la lista de opciones")
            backtomain(window)

#Event to Open a option list
def open(oplist,window):
    """OPEN

    Event to open a option list and bring a menu of the option list

    -ARGS-

    oplist: name of an option list to open.
    window: the tkinter root for exit.
    """
    if oplist != "":
        mainlist(window,oplist)

#Event to Delete a option list
def delete(oplist,window):
    """DELETE

    Event to delete a option list

    -ARGS-

    oplist: name of an option list to delete.
    window: the tkinter root for exit.
    """
    if oplist != "":
        if opls.eraselist(oplist) == 0 or opls.deletelist(oplist) == 0:
            mb.showerror(title="Error",message="Hay un error al eliminar la lista de opciones.")
        backtomain(window)

#Event to Rename a option list
def rename(oplist,newname,window):
    """RENAME

    Event to rename a option list

    -ARGS-

    oplist: name of an option list to rename.
    newname: the new name for the option list
    window: the tkinter root for exit.
    """
    if oplist != "" and newname != "":
        if newname in opls.getoplists() or newname == oplist:
            mb.showinfo(title="Lista Existente",message=f"La lista de opciones \"{newname}\" ya existe")
        else:
            if opls.changelist(oplist,newname) == 0 or opls.renamelist(oplist,newname) == 0:
                mb.showerror(title="Error",message="Hay un error al renombrar la lista de opciones.")
            backtomain(window)

#Select randomly an option of the option list
def opselect(oplist,label,button):
    """OPSELECT

    Event to select randomly an option of the list

    -ARGS-

    oplist: name of an option list to select from.
    label: the label to display the selected option.
    button: the button to disable after selection.
    """
    options = opls.getoptions(oplist)
    maxnum = len(options)
    randnum = random.randint(0,maxnum-1)
    try:
        label.configure(text=options[randnum])
        button.configure(state="disabled")
    except AttributeError:
        pass

#Event to Add an option in the list
def opadd(option,oplist,window):
    """OPADD

    Event to add an option in the list

    -ARGS-

    option: name of the option to add in oplist
    oplist: name of the option list.
    window: the tkinter root to exit
    """ 
    if option != "":
        if opls.writeop(option,oplist) == 0:
            mb.showerror(title="Error",message="Hay un error al crear la opción")
        mainlist(window,oplist) 

#Event to Rename an option from the list
def oprename(option, newname, oplist, window):
    """OPRENAME

    Event to rename an option of the list

    -ARGS-

    option: name of the option to rename
    newname: new name for the option
    oplist: name of the option list.
    window: the tkinter root to exit
    """ 
    if option != "" and newname != "":
        if opls.changeop(option,newname,oplist) == 0:
            mb.showerror(title="Error",message="Hay un error al renombrar la opción")
        mainlist(window,oplist)

#Event to Delete an option from the list
def opdelete(option, oplist, window):
    """OPRENAME

    Event to delete an option from the list

    -ARGS-

    option: name of the option to delete
    oplist: name of the option list.
    window: the tkinter root to exit
    """ 
    if option != "":
        if opls.eraseop(option,oplist) == 0:
            mb.showerror(title="Error",message="Hay un error al eliminar la opción")
        mainlist(window,oplist)

#Event to Delete all options from the list
def opempty(oplist, button1, button2):
    """OPEMPTY

    Event to delete all options from the list

    -ARGS-

    oplist: name of the option list.
    button1: select option button to disable
    button2: delete all button to disable
    """ 
    if opls.emptylist(oplist) == 0:
        mb.showerror(title="Error",message="Hay un error al vaciar la lista de opciones")
    else:
        mb.showinfo(title="Lista Vacía", message="La lista ya está vacía")
        try:
            button1.configure(state="disabled")
            button2.configure(state="disabled")
        except AttributeError:
            pass
