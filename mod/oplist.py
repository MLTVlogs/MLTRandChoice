import io
import os

#LIST OF OPTION LISTS MANAGEMENT--------------------
#write the option list in a file
def writelist(oplist):
    """WRITELIST
    
    Saves an option list name in a file with names of lists
    
    -ARGS-
    - oplist: name of the option list
    """
    try:
        #Create a file to save list names
        lists = io.open(f"files//lists.dat","ab")
    except FileNotFoundError:
        return 0
    else:
        #Save a list name in a file
        lists.write(f"{oplist}\n".encode())
        lists.close()
        return 1

#Search an option list
def searchlist(oplist):
    """SEARCHLIST
    
    Search an option list in the file with names of lists
    
    -ARGS-
    - oplist: name of the option list"""
    try:
        #Open the file with a list of option lists
        lists = io.open(f"files//lists.dat","rb")
    except FileNotFoundError:
        return 0
    else:
        found = False
        for item in lists:
            if item.decode().rstrip("\n").capitalize() == oplist.capitalize():
                lists.close()
                return 1
        lists.close()
        return 0

#Create a list with option lists
def getoplists():
    """GETOPLISTS
    
    Create a list with all option list
    """
    try:
        #Open the file with a list of option lists
        lists = io.open(f"files//lists.dat","rb")
    except FileNotFoundError:
        return None
    else:
        oplists = []
        for op in lists:
            oplists.append(op.decode().rstrip("\n"))
        return oplists
        
#Rename an option list from the list
def changelist(before,after):
    """CHANGELIST
    
    Rename the option list from the file with
    name of lists
    
    -ARGS-
    - before: previous name of the option list
    - after: new name of the option list
    """
    #Get a list of option lists
    oplists = getoplists()
    if after in oplists:
        return 0
    else:
        try:
            oplists[oplists.index(before)] = after
        except ValueError:
            return 0
        else:
            try:
                lists = io.open("files//lists.dat","wb")
            except FileNotFoundError:
                return 0
            else:
                #Save all current option list names
                for oplist in oplists:
                    lists.write(f"{oplist}\n".encode())
                lists.close()
                return 1

#Delete an option list from the list
def eraselist(name):
    """ERASELIST
    
    Delete the name of the option list from the file with
    name of lists
    
    -ARGS-
    - name: name of the option list
    """
    #Get a list of option lists
    oplists = getoplists()
    try:
        oplists.remove(name)
    except ValueError:
        return 0
    else:
        try:
            #Create and replace the file
            lists = io.open("files//lists.dat","wb")
        except FileNotFoundError:
            return 0
        else:
            #Save all current option list names
            for oplist in oplists:
                lists.write(f"{oplist}\n".encode())
            lists.close()
            return 1

#OPTION LIST MANAGEMENT--------------------
#Write an option in the list
def writeop(option,oplist):
    """WRITEOP
    
    Saves an option in a option list file
    
    -ARGS-
    - option: name of an option
    - oplist: name of the option list"""
    try:
        #Open the option list file
        optionlist = io.open(f"files//{oplist}.dat","ab")
    except FileNotFoundError:
        return 0
    else:
        #Save a open in the option list file
        optionlist.write(f"{option}\n".encode())
        optionlist.close()
        return 1

#Search an option in the list
def searchop(option,oplist):
    """SEARCHOP
    
    Search an option in a option list file
    
    -ARGS-
    - option: name of an option
    - oplist: name of the option list"""
    try:
        #Open the option list file
        optionlist = io.open(f"files//{oplist}.dat","rb")
    except FileNotFoundError:
        return 0
    else:
        found = False
        for item in optionlist:
            if item.decode().rstrip("\n").capitalize() == option.capitalize():
                optionlist.close()
                return 1
        optionlist.close()
        return 0

#Create a list with options from an option list
def getoptions(oplist):
    """GETOPTIONS
    
    Create a list with all options of an optionlist

    -ARGS-
    - oplist: name of the option list
    """
    try:
        #Open the option list file
        optionlist = io.open(f"files//{oplist}.dat","rb")
    except FileNotFoundError:
        return None
    else:
        options = []
        for op in optionlist:
            options.append(op.decode().rstrip("\n"))
        return options

#Rename an option from an option list
def changeop(before, after, oplist):
    """CHANGEOP
    
    Rename an option from the option list file
    
    -ARGS-
    - before: previous name of the option
    - after: new name for the option
    - oplist: name of the option list"""

    #Get a list of options
    options = getoptions(oplist)
    try:
        options[options.index(before)] = after
    except ValueError:
        return 0
    else:
        try:
            optionlist = io.open(f"files//{oplist}.dat","wb")
        except FileNotFoundError:
            return 0
        else:
            for op in options:
                optionlist.write(f"{op}\n".encode())
            optionlist.close()
            return 1

#Delete an option from an option list
def eraseop(option, oplist):
    """ERASEOP
    
    Delete an option from the option list file
    
    -ARGS-
    - option: name of the option
    - oplist: name of the option list
    """
    #Get a list of options
    options = getoptions(oplist)
    try:
        options.remove(option)
    except ValueError:
        return 0
    else:
        try:
            optionlist = io.open(f"files//{oplist}.dat","wb")
        except FileNotFoundError:
            return 0
        else:
            for op in options:
                optionlist.write(f"{op}\n".encode())
            optionlist.close()
            return 1
        
#Empty an option list
def emptylist(oplist):
    """EMPTYLIST
    
    Delete all options from the option list file
    
    -ARGS-
    - oplist: name of the option list
    """
    try:
        optionlist = io.open(f"files//{oplist}.dat","wb")
        return 1
    except FileNotFoundError:
        return 0

#LIST FILES MANAGEMENT--------------------
#Create a file with the option list information
def createlist(name):
    """CREATELIST
    
    Create a file with the option list information
    
    -ARGS-
    - name: name of the option list"""
    try:
        #Create a file to save list
        oplist = io.open(f"files//{name}.dat","wb")
    except FileNotFoundError:
        return 0
    else:
        oplist.close()
        return 1
    
#Delete a option list file
def deletelist(name):
    """DELETELIST
    
    Delete the file with the option list information
    
    -ARGS-
    - name: name of the option list""" 
    try:
       #Delete the file
       os.remove(f"files//{name}.dat")
    except FileNotFoundError:
        return 0
    else:
        return 1

#Rename a option list file
def renamelist(before,after):
    """CHANGELIST
    
    Rename the file with the option list information
    
    -ARGS-
    - before: previous name of the option list
    - after: new name of the option list
    """
    try:
        #Rename the file
        os.rename(f"files//{before}.dat",f"files//{after}.dat")
    except FileNotFoundError:
        return 0
    else:
        return 1
