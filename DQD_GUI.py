from tkinter import *
from tkinter import ttk


def get_que(event):

    # Get the value stored in the entries
    q1 = First_que.get()
    q2 = Second_que.get()

    # Delete the value in the entry
    First_que.delete(0, "end")
    Second_que.delete(0, "end")

    # Insert the sum into the entry
    First_que.insert(0, q2)
    Second_que.insert(0, q1)


root = Tk()
root.title("Duplicate Question Detection")
root.minsize(width=800, height=150)
root.maxsize(width=800, height=150)

# rows start at 0, 1, ...
# columns start at 0, 1, ...
# sticky defines how the widget expands (N, NE, E, SE,
# S, SW, W, NW)
# padx and pady provide padding around the widget above
# and below it
Label(root, text="First Question").grid(row=0, sticky=W, padx=10)
First_que = Entry(root, width=100)
First_que.grid(row=0, column=1, sticky=E, pady=10)

Label(root, text="Second Question").grid(row=1, sticky=W, padx=10)
Second_que = Entry(root, width=100)
Second_que.grid(row=1, column=1, sticky=E, pady=10)

equalButton = Button(root, text="Submit")
equalButton.grid(row=3)
equalButton.bind("<Button-1>", get_que)


root.mainloop()
