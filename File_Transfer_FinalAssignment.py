from tkinter import *
import tkinter as tk
from tkinter import filedialog

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #setting the frame configuration
        self.master = master
        self.master.title("Submit File Check")
        
        self.btn_browse1 = tk.Button(self.master,width=12,text="Outgoing File(s)",command = browseFiles)
        self.btn_browse1.grid(row=2,column=1,padx= 15,pady=10,stick=W)
        
##        self.txt_browse1 = tk.Entry(self.master,text='',width =50)
##        self.txt_browse1.grid(row=2, column=2,padx= 15, pady=5,columnspan=3)

        self.btn_browse2 = tk.Button(self.master,width=12,text="Main File",command = browseMainFile)
        self.btn_browse2.grid(row=3,column=1,padx= 15,pady=5,stick=SW)
        
##        self.txt_browse2 = tk.Entry(self.master,text='',width =50)
##        self.txt_browse2.grid(row=3, column=2,padx= 15, pady=0,columnspan=3)

        self.btn_close =tk.Button(self.master,width=12,height=2,text="Check Files")
        self.btn_close.grid(row=4,column=4,padx= 15,pady=5,stick=SE)

        # Create a File Explorer label for outgoing file
        label_file_explorer_Outgoing = Label(self.master, text = "Please, pick a file", width = 50) 
        label_file_explorer_Outgoing.grid(column = 2, row = 2)

        # Create a File Explorer label for main file
        label_file_explorer_Main = tk.Label(self.master, text = "Please, pick a file", width = 50) 
        label_file_explorer_Main.grid(row = 3, column = 2) 

        
def browseFiles():
	filename = filedialog.askopenfilename(initialdir = "C:/Users/Ryan/Desktop/DailyFiles/",title = "DailyFiles", filetypes = (("Text files", "*.txt*"),("all files", "*.*")))

                # Change label contents 
	label_file_explorer_Outgoing.configure(self.master,text="File Choice: " +filename)
	
                
def browseMainFile(): 
	filename = filedialog.askopenfilename(initialdir = "C:/Users/Ryan/Desktop/BatchCopy/",title = "BatchCopy", filetypes = (("Text files", "*.txt*"),("all files", "*.*")))

                # Change label contents 
	label_file_explorer_Main.configure(self.master,text="File Choice: " + filename)

##def checkfiles():
##    I WILL WRITE A FUNCTION HERE THAT WILL COMPARE BOTH AFTER
##    I FIGURE OUT HOW TO GET THE LABELS TO WORK

	
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    

