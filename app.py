import tkinter as tk
from tkinter import filedialog
import os
from main import Youtube

hastag = ""
count = 0

def setHastag():
    hastag = inputHastag.get()
    count = int(inputCount.get())
    label = tk.Label(frame, text=f"Hastag : {hastag}. Count : {count}")
    label.pack()
    print("A")

def initiateGetData():
    print("Initiating...")
    Youtube(hastag, count)

root = tk.Tk()

canvas = tk.Canvas(root, height=700, width=700, bg="#4287f5")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.05, rely=0.05)

inputHastag = tk.Entry(frame, width=50)
inputHastag.pack()
inputHastag.insert(0, "Input hastag ...")

inputCount = tk.Entry(frame, width=50)
inputCount.pack()
inputCount.insert(0, "Input loop count ...")

setHastagButton = tk.Button(frame, text="Set Hastag", padx=10, pady=5, fg="white", bg="#4287f5", command=setHastag)
setHastagButton.pack()

startButton = tk.Button(frame, text="Start", padx=10, pady=5, fg="white", bg="#4287f5", command=initiateGetData)
# startButton = tk.Button(frame, text="Start", padx=10, pady=5, fg="white", bg="#4287f5")
startButton.pack()

root.mainloop()