import tkinter as tk
from tkinter import text
import os
import main

root = tk.Tk()

hastag = ""
count = 0

canvas = tk.Canvas(root, height=700, width=700, bg="#4287f5")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

inputHastag = tk.Entry(root, width=50)
inputHastag.pack()
inputHastag.insert(0, "Input hastag ...")

inputCount = tk.Entry(root, width=50)
inputCount.pack()
inputCount.insert(0, "Input loop count ...")

setHastagButton = tk.Button(root, text="Set Hastag", padx=10, pady=5, fg="white", bg="#4287f5", command=setHastag)
setHastagButton.pack()

startButton = tk.Button(root, text="Start", padx=10, pady=5, fg="white", bg="#4287f5", command=initiateGetData(hastag,count))
startButton.pack()

def setHastag():
    hastag = inputHastag.get()
    count = int(inputCount.get())
    label = tk.Label(root, text=f"Hastag : {hastag}. Count : {count}")

def initiateGetData(tag, count):
    main.Youtube(tag, count)

root.mainloop()