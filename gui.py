from downloader import download_sheet_music
from tkinter import *
import tkinter.font as font


def download():
  value = e1.get()
  download_sheet_music(value)

root = Tk()

myFont = font.Font(size=15)
 
root.title("MuseScore downloader")
# root window title and dimension

# Set geometry (widthxheight)
root.geometry('350x200')
 
Label(root, text="url").grid(row=0)

e1 = Entry(root, width=50)

e1.grid(row=0, column=1)

Button(root, text='Download', font=myFont, command=download).grid(row=3, column=1, sticky=W, pady=4)
# all widgets will be here
# Execute Tkinter
root.mainloop()