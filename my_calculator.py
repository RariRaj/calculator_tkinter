from tkinter import *

window = Tk()
window.title("calculator")
window.geometry("450x500")

# for Entry field(getting input from user and display result)
entryText = StringVar()
Entry(window, relief=RIDGE, textvariable=entryText, justify='right', bd=26, fg="white", bg="gray",
      font=("Times", "24")).grid(sticky="WE", row=1, column=1, columnspan=4)

# for Button widgets
Button(window, text="7", font="Times 18", width=6, height=2).grid(row=2, column=1)
Button(window, text="8", font="Times 18", width=6, height=2).grid(row=2, column=2)
Button(window, text="9", font="Times 18", width=6, height=2).grid(row=2, column=3)
Button(window, text="4", font="Times 18", width=6, height=2).grid(row=3, column=1)
Button(window, text="5", font="Times 18", width=6, height=2).grid(row=3, column=2)
Button(window, text="6", font="Times 18", width=6, height=2).grid(row=3, column=3)
Button(window, text="1", font="Times 18", width=6, height=2).grid(row=4, column=1)
Button(window, text="2", font="Times 18", width=6, height=2).grid(row=4, column=2)
Button(window, text="3", font="Times 18", width=6, height=2).grid(row=4, column=3)
Button(window, text="0", font="Times 18", width=6, height=2).grid(row=5, column=1)
Button(window, text=".", font="Times 18", width=6, height=2).grid(row=5, column=2)
Button(window, text="DEL", font="Times 18", width=6, height=2).grid(row=5, column=3)
Button(window, text="/", font="Times 18", width=6, height=2).grid(row=2, column=4)
Button(window, text="x", font="Times 18", width=6, height=2).grid(row=3, column=4)
Button(window, text="-", font="Times 18", width=6, height=2).grid(row=4, column=4)
Button(window, text="+", font="Times 18", width=6, height=2).grid(row=5, column=4)
Button(window, text="Clear", font="Times 18", width=15,height=2).grid(sticky="W",row=6, column=1,columnspan=2)
Button(window, text="=", font="Times 18", width=15, height=2).grid(row=6, column=3,columnspan=2)


window.mainloop()
