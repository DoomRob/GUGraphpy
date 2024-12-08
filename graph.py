from tkinter import *
from PIL import ImageTk,Image
import numpy as np
import matplotlib.pyplot as mplt

root = Tk()
root.title("My Code")
root.iconbitmap('Python/GUI')
root.geometry("400x400")

def graph():
    housesPrices = np.random.normal(20000, 25000, 5000)
    mplt.hist(housesPrices, 50)
    mplt.show()

myButton = Button(root, text="House Graphs", command=graph)
myButton.pack()


# Execution
root.mainloop()
