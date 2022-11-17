import tkinter as tk
from tkinter import filedialog
import main

hastag = ""
count = 0
dir = ""

def setHastag():
    global hastag
    global count
    global dir
    hastag = inputHastag.get()
    count = int(inputCount.get())
    dir = inputDir.cget("text")
    label = tk.Label(frame, text=f"Hastag : {hastag}. Count : {count}. Dir : {dir}")
    label.grid(row=10,column=1)
    print(label)

def initiateYoutube():
    print("Initiating youtube...", hastag, count)
    main.Controller(hastag, count, dir, "Youtube")

def initiateTiktok():
    print("Initiating Tiktok...", hastag, count)
    main.Controller(hastag, count, dir, "Tiktok")

def initiateInstagram():
    print("Initiating Instagram...", hastag, count)
    main.Controller(hastag, count, dir, "Instagram")

def getDir():
    print("Getting Dir")
    path = filedialog.askdirectory()
    inputDir.config(text=path)

root = tk.Tk()
root.title("Data Extraction App")

canvas = tk.Canvas(root, height=700, width=700, bg="#4287f5")
# canvas.pack()

frame = tk.Frame(root, bg="white")
tk.Label(frame, text="Data Extraction Apps", font=('Arial Bold', 16)).grid(row=0,column=0, columnspan=2, pady=(0,20))

hastagLabel = tk.Label(frame,text="Input Hastag : ").grid(row=1,column=0,pady=(0,5))
inputHastag = tk.Entry(frame, width=50)
inputHastag.grid(row=1,column=1)

countLabel = tk.Label(frame, text="Jumlah Data : ").grid(row=2,column=0,pady=(0,5))
inputCount = tk.Entry(frame, width=50)
inputCount.grid(row=2,column=1)

askDirLabel = tk.Label(frame, text="Set directory : ").grid(row=3,column=0,pady=(0,5))
inputDir = tk.Label(frame, width=50)
inputDir.grid(row=3,column=1)

buttonDir = tk.Button(frame, text="Set directory", fg="white", bg="#4287f5", command=getDir)
buttonDir.grid(row=4,column=0, columnspan=2, pady=(0,10))

setHastagButton = tk.Button(frame, text="Set Config", padx=10, pady=5, fg="white", bg="#4287f5", command=setHastag).grid(row=5,column=0,columnspan=2, pady=(0,10))
# setHastagButton.pack()

startYoutube = tk.Button(frame, text="Start Youtube", padx=10, pady=5, fg="white", bg="#4287f5", command=initiateYoutube).grid(row=6,column=0,columnspan=2, pady=(0,10))
startTiktok = tk.Button(frame, text="Start Tiktok", padx=10, pady=5, fg="white", bg="#4287f5", command=initiateTiktok).grid(row=7,column=0,columnspan=2, pady=(0,10))
startInstagram = tk.Button(frame, text="Start Instagram", padx=10, pady=5, fg="white", bg="#4287f5", command=initiateInstagram).grid(row=8,column=0,columnspan=2, pady=(0,20))

frame.place(relwidth=0.8, relheight=0.8, relx=0.5, rely=0.5, anchor="center")
frame.pack()

root.mainloop()