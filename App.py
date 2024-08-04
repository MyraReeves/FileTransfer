import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil


class GUI (Frame):
    def __init__(self, master):
        Frame.__init__(self)
        self.master.title("Transfer All Files To New Folder")

        # "Select Source" button:
        self.sourceDirectoryButton = Button(text="Source Folder", width=20, bg="papayawhip", command=self.sourceDir)
        self.sourceDirectoryButton.grid(row=0, column=0, padx=(20, 10), pady=(30,0))

        # Display area for the chosen source:
        self.sourceDirectoryEntry = Entry(width=75, bg="papayawhip")
        self.sourceDirectoryEntry.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30, 0))   # padx and pady are the same as the button to ensure they will line up.

        # "Select Destination" button:
        self.destinationDirectoryButton = Button(text="Destination Folder", width=20, bg="lavender", command=self.destiDir)
        self.destinationDirectoryButton.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))

        # Display area for the chosen destination:
        self.destinationDirectoryEntry = Entry(width=75, bg="lavender")
        self.destinationDirectoryEntry.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15, 10)) # padx and pady are the same as the button to ensure they will line up.

        # File Transfer button:
        self.transferButton = Button(text="Transfer All Files", width = 20, height=2, bg="palegreen", command=self.transferFiles)
        self.transferButton.grid(row=2, column=1, pady=(10, 25))



if __name__ == "__main__":
    root = tk.Tk()
    App = GUI(root)
    root.mainloop