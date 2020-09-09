from tkinter import *
import tkinter as tk
from tkinter import filedialog
import os
import datetime
import shutil

class ParentWindow(Frame):              #create class window
    def __init__(self, master, *args, **kwargs):    #create object of parent window
        Frame.__init__(self, master, *args, **kwargs)

        #setting the frame configuration
        self.master = master
        self.master.title("Submit File Check")
        
        self.btn_browse1 = tk.Button(self.master,width=12,text="Outgoing File(s)",command = self.browseFiles)
        self.btn_browse1.grid(row=2,column=1,padx= 15,pady=10,stick=W)
        
        self.txt_browse1 = tk.Entry(self.master,text='',width =50)
        self.txt_browse1.grid(row=2, column=2,padx= 15, pady=5,columnspan=3)

        self.btn_browse2 = tk.Button(self.master,width=12,text="Main File",command = self.browseMainFile)
        self.btn_browse2.grid(row=3,column=1,padx= 15,pady=5,stick=SW)
        
        self.txt_browse2 = tk.Entry(self.master,text='',width =50)
        self.txt_browse2.grid(row=3, column=2,padx= 15, pady=0,columnspan=3)

        self.btn_check =tk.Button(self.master,width=12,height=2,text="Check Files",command = self.checkfiles)
        self.btn_check.grid(row=4,column=4,padx= 15,pady=5,stick=SE)

       

        
    def browseFiles(self):
        sourcedir = filedialog.askdirectory()
        self.txt_browse1.delete(0,END)                          #this deletes everything in the Entry field from start to finish(0 to End)
        self.txt_browse1.insert(0, sourcedir)                   # this inserts the file that the person picks into the entry field

                	
                
    def browseMainFile(self):
        destinationdir = filedialog.askdirectory()
        self.txt_browse2.delete(0,END)                          #this deletes everything in the Entry field from start to finish(0 to End)
        self.txt_browse2.insert(0, destinationdir)              # this inserts the file that the person picks into the entry field
                

    def checkfiles(self):
        sourcedir = self.txt_browse1.get()              # is the selected directory
        destinationdir = self.txt_browse2.get()       #is the destination directory
        listfiles = os.listdir(sourcedir)                    #list of files inside source
        for i in listfiles:                                         #Variable "i" is an element of listfile (elements in listfile are filenames inside the directory that was listed
            a_path = os.path.join(sourcedir, i)
            time = os.path.getmtime(a_path)
            last_hours = datetime.datetime.now() - datetime.timedelta(hours = 24)
            modtime = datetime.datetime.fromtimestamp(time)
            if last_hours <= modtime:
                shutil.move(a_path,destinationdir)
                print(i + " was moved")
	
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    

