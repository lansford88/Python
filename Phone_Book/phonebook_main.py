#Author:            Ryan Lansford

#Purpose:           Phonebook Demo. Demonstrating OOP, Tkinter GUI Module,
#                    using Tkinter Parent and Child relationships.
#
#Tested OS:          This code was written and tested to work with Windows 10.



from tkinter import *
import tkinter as tk



#Be sure to import our other modules
#so we can have access to them
import phonebook_gui
import phonebook_func


#Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):                                              #FRAME is the primary Tkinter object, we will inherit from it
    def __init__(self, master, *args, **kwargs):                        #this intializes, refrence the class(ParentWindow) with self, and then master is what were calling the FRAME
        Frame.__init__(self, master, *args, **kwargs)                   

        #define our master frame configuration
        self.master = master                                            #in order to access the tkinter object, we have to do self, self.master is the parentwindow frame.
        self.master.minsize(500,300)                                   #(Height, Width)Sets size- By setting min/max size, we make it to where they cannot adjust the window.
        self.master.maxsize(500,300)
        # This CenterWindow method will center our app on the user's screen
        phonebook_func.center_window(self,500,300)                      #This will always center the window in the middle of the screen             
        self.master.title("The Tkinter Phonebook Demo")                 #This Creates the Title of the window.
        self.master.configure(bg="#F0F0F0")                             #Background Color 
        #This protocol method is a tkinter built-in method to catch if
        #the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))         
        

        # load in the GUI widgets from a seperate module,
        # keeping your code comparmentalized and clutter free
        phonebook_gui.load_gui(self)



if __name__ == "__main__":                  
    root = tk.Tk()                               
    App = ParentWindow(root)                    
    root.mainloop()
                              
