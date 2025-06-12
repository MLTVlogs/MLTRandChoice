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

#write the range list in a file
def writerlist(oplist):
    """WRITERLIST
    
    Saves an range list name in a file with names of lists
    
    -ARGS-
    - oplist: name of the range list
    """
    try:
        #Create a file to save list names
        lists = io.open(f"files//rlists.dat","ab")
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
        for item in lists:
            if item.decode().rstrip("\n").capitalize() == oplist.capitalize():
                lists.close()
                return 1
        lists.close()
        return 0

#Search a range list
def searchrlist(oplist):
    """SEARCHRLIST
    
    Search an range list in the file with names of lists
    
    -ARGS-
    - oplist: name of the range list"""
    try:
        #Open the file with a list of option lists
        lists = io.open(f"files//rlists.dat","rb")
    except FileNotFoundError:
        return 0
    else:
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
    
#Create a list with range lists
def getrangelists():
    """GETRANGELISTS
    
    Create a list with all range list
    """
    try:
        #Open the file with a list of option lists
        lists = io.open(f"files//rlists.dat","rb")
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

#Rename a range list from the list
def changerlist(before,after):
    """CHANGERLIST
    
    Rename the range list from the file with
    name of lists
    
    -ARGS-
    - before: previous name of the range list
    - after: new name of the range list
    """
    #Get a list of range lists
    rlists = getrangelists()
    if after in rlists:
        return 0
    else:
        try:
            rlists[rlists.index(before)] = after
        except ValueError:
            return 0
        else:
            try:
                lists = io.open("files//rlists.dat","wb")
            except FileNotFoundError:
                return 0
            else:
                #Save all current option list names
                for rlist in rlists:
                    lists.write(f"{rlist}\n".encode())
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

#Delete a range list from the list
def eraserlist(name):
    """ERASERLIST
    
    Delete the name of the range list from the file with
    name of lists
    
    -ARGS-
    - name: name of the range list
    """
    #Get a list of range lists
    rlists = getrangelists()
    try:
        rlists.remove(name)
    except ValueError:
        return 0
    else:
        try:
            #Create and replace the file
            lists = io.open("files//rlists.dat","wb")
        except FileNotFoundError:
            return 0
        else:
            #Save all current range list names
            for rplist in rlists:
                lists.write(f"{rplist}\n".encode())
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
        optionlist = io.open(f"files//lists//{oplist}.dat","ab")
    except FileNotFoundError:
        return 0
    else:
        #Save a open in the option list file
        optionlist.write(f"{option}\n".encode())
        optionlist.close()
        return 1

# #Search an option in the list
# def searchop(option,oplist):
#     """SEARCHOP
    
#     Search an option in a option list file
    
#     -ARGS-
#     - option: name of an option
#     - oplist: name of the option list"""
#     try:
#         #Open the option list file
#         optionlist = io.open(f"files//lists//{oplist}.dat","rb")
#     except FileNotFoundError:
#         return 0
#     else:
#         for item in optionlist:
#             if item.decode().rstrip("\n").capitalize() == option.capitalize():
#                 optionlist.close()
#                 return 1
#         optionlist.close()
#         return 0

#Create a list with options from an option list
def getoptions(oplist):
    """GETOPTIONS
    
    Create a list with all options of an optionlist

    -ARGS-
    - oplist: name of the option list
    """
    try:
        #Open the option list file
        optionlist = io.open(f"files//lists//{oplist}.dat","rb")
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
            optionlist = io.open(f"files//lists//{oplist}.dat","wb")
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
            optionlist = io.open(f"files//lists//{oplist}.dat","wb")
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
        io.open(f"files//lists//{oplist}.dat","wb")
        return 1
    except FileNotFoundError:
        return 0

#RANGE LIST MANAGEMENT--------------------
#Write numbers in the range list
def writenums(min, max, rlist):
    """WRITERANGE
    
    Saves a range of numbers in a range list file
    
    -ARGS-
    - min: minimum number of the range
    - max: maximum number of the range
    - rlist: name of the range list"""
    try:
        #Open the range list file
        rangelist = io.open(f"files//rlists//{rlist}.dat","ab")
    except FileNotFoundError:
        return 0
    else:
        #Save all numbers in the range list file
        for num in range(min, max + 1):
            rangelist.write(f"{num}\n".encode())
        rangelist.close()
        return 1

#Create a list with options from a range list
def getnums(rlist):
    """GETNUMS
    
    Create a list with all numbers of a range list

    -ARGS-
    - rlist: name of the range list
    """
    try:
        #Open the option list file
        optionlist = io.open(f"files//rlists//{rlist}.dat","rb")
    except FileNotFoundError:
        return None
    else:
        options = []
        for op in optionlist:
            try:
                options.append(int(op.decode().rstrip("\n")))
            except ValueError:
                # If the line is not a number, skip it
                continue
        optionlist.close()
        return options
    
#Delete an number from a range list
def erasenum(num, rlist):
    """ERASENUM

    Delete a number from the range list file

    -ARGS-
    - num: number to delete
    - rlist: name of the range list
    """
    #Get a list of options
    numbers = getnums(rlist)
    try:
        if not isinstance(num, int):
            num = int(num)
        numbers.remove(num)
    except ValueError:
        return 0
    else:
        try:
            optionlist = io.open(f"files//rlists//{rlist}.dat","wb")
        except FileNotFoundError:
            return 0
        else:
            for op in numbers:
                optionlist.write(f"{op}\n".encode())
            optionlist.close()
            return 1

#Empty a range list
def emptyrlist(rlist):
    """EMPTYRLIST
    
    Delete all numbers from the range list file
    
    -ARGS-
    - oplist: name of the option list
    """
    try:
        io.open(f"files//rlists//{rlist}.dat","wb")
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
        oplist = io.open(f"files//lists//{name}.dat","wb")
    except FileNotFoundError:
        return 0
    else:
        oplist.close()
        return 1
    
def createrlist(name):
    """CREATERLIST
    
    Create a file with the range list information
    
    -ARGS-
    - name: name of the range list"""
    try:
        #Create a file to save list
        oplist = io.open(f"files//rlists//{name}.dat","wb")
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
       os.remove(f"files//lists//{name}.dat")
    except FileNotFoundError:
        return 0
    else:
        return 1

def deleterlist(name):
    """DELETERLIST
    
    Delete the file with the range list information
    
    -ARGS-
    - name: name of the range list""" 
    try:
       #Delete the file
       os.remove(f"files//rlists//{name}.dat")
    except FileNotFoundError:
        return 0
    else:
        return 1

#Rename a option list file
def renamelist(before,after):
    """RENAMELIST
    
    Rename the file with the option list information
    
    -ARGS-
    - before: previous name of the option list
    - after: new name of the option list
    """
    try:
        #Rename the file
        os.rename(f"files//lists//{before}.dat",f"files//lists//{after}.dat")
    except FileNotFoundError:
        return 0
    else:
        return 1

def renamerlist(before,after):
    """RENAMERLIST
    
    Rename the file with the range list information
    
    -ARGS-
    - before: previous name of the range list
    - after: new name of the range list
    """
    try:
        #Rename the file
        os.rename(f"files//rlists//{before}.dat",f"files//rlists//{after}.dat")
    except FileNotFoundError:
        return 0
    else:
        return 1

if __name__ == "__main__":
    pass