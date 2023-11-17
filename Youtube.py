from pytube import YouTube
from tkinter import *
import tkinter as tk
import os
from tkinter.filedialog import askdirectory
from tkinter.font import Font

root = tk.Tk()
root.title("YouTube Downloader")
root.geometry("670x350")

# Label Fonts

headfont = Font(family="Helvetica", size=11, weight="bold")

labelfont = Font(family="Helvetica", size=11, weight="normal")

endfont = Font(family="Helvetica", size=8, weight="bold")


def endsession():
    root.destroy()


close = tk.Button(root, text="Close", command=endsession, fg="red", font=endfont)

close.place(x=605, y=2)


# ---------------------------------------

# destination path

def getpath():
    global path1
    global SAVE_PATH
    path = askdirectory()
    SAVE_PATH = path
    path1 = r'{}'.format(path)


# --------------------------------------

def Down():
    global Label1
    global Label2
    global Label3
    global fs
    global youtubeObject

    url = urlEntry.get()
    youtubeObject = YouTube(url)
    youtubeObject = youtubeObject.streams.get_highest_resolution()

    title = youtubeObject.title

    Label1 = Label(root, text=f"{title} ", fg="blue")
    Label1.place(x=200, y=150)

    fs = youtubeObject.filesize

    mgs1 = fs / 1048576  # 2^20
    mgs2 = fs / 1000000  # 10^3

    mgs3 = (mgs1 + mgs2) / 2  # Average
    mgs = round(mgs3, 1)





    try:
        youtubeObject.download(SAVE_PATH)

    except:

        Label(root, text="No Destination folder selected!").place(x=100, y=180)
    finally:


        Label3 = Label(root, text="Download Completed!")
        Label3.place(x=200, y=230)

        Label2 = Label(root, text=f"{mgs} mbs", fg="green")
        Label2.place(x=200, y=190)

# ---------------------------------------


Label4 = Label(root, text="Enter Video url", font=headfont)
Label4.place(x=110, y=5)

urlEntry = Entry(root, width=30, font=labelfont)
urlEntry.place(x=110, y=30)
urlEntry.focus_force()

buttondl = tk.Button(root, text="Download Video", command=Down)
buttondl.place(x=380, y=30)


# ---------------------------------------

def openf():
    os.startfile(path1, 'open')


button = Button(root, text="Open video location", bg="azure", command=openf)

button.place(x=390, y=80)


def clear():
    urlEntry.delete(0, END)
    Label1.destroy()
    Label2.destroy()
    Label3.destroy()


Button(root, text="Clear", command=clear, fg='blue', font=headfont).place(x=20, y=20)

Button(root, text="Select Destination", command=getpath, fg='green', font=headfont).place(x=20, y=100)

root.mainloop()
