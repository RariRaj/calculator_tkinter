from tkinter import *
from tkinter.messagebox import *
import math as m

window = Tk()
window.title("calculator")
window.geometry("420x495")

# for picture label
pic = PhotoImage(file='img/calculator.png')
picLabel = Label(window, image=pic)
picLabel.pack(side=TOP)
# picLabel.grid(sticky="w", row=0, column=2)

# for heading label
headingLabel = Label(window, text="MY CALCULATOR", font=("Arial", 20, 'bold'))
headingLabel.pack(side=TOP)


# headingLabel .grid(row=0, column=2, columnspan=4)


# method for Delete
def delete():
    entryText.set(entryText.get()[:-1])


# method for clear all inputs
def clear():
    entryText.set("")


# method for adding inputs while button click
def add(text):
    oldtextvalue = entryText.get()
    if oldtextvalue == "Error":
        entryText.set(text)

    else:
        entryText.set(oldtextvalue + text)


# method for equal button
def calc():
    try:
        entryText.set(eval(entryText.get()))

    except:
        entryText.set("Error")
        showinfo("Error", "Please enter a valid operation")


# for Entry field(getting input from user and display result)
entryText = StringVar()
entry_field = Entry(window, relief=RIDGE, textvariable=entryText, justify='right', bd=26, bg='powder blue',
                    font=("Times", "24"))
# entry_field.grid(sticky="WE", row=2, column=2, columnspan=4)
entry_field.pack(side=TOP, ipadx=20)

# Place a frame to include all buttons
frame = Frame(window)
frame.config(bg="powder blue")
frame.pack(side=TOP)

# for Button widgets
btn7 = Button(frame, text="7", command=lambda: add("7"), bg='light blue', activebackground='orange', font="Times 18",
              width=6, height=2)

btn7.grid(row=3, column=2)

btn8 = Button(frame, text="8", command=lambda: add("8"), bg='light blue', activebackground='orange', font="Times 18",
              width=6,
              height=2)
btn8.grid(row=3, column=3)

btn9 = Button(frame, text="9", command=lambda: add("9"), bg='light blue', activebackground='orange', font="Times 18",
              width=6,
              height=2)
btn9.grid(row=3, column=4)

btn4 = Button(frame, text="4", command=lambda: add("4"), bg='light blue', activebackground='orange', font="Times 18",
              width=6,
              height=2)
btn4.grid(row=4, column=2)

btn5 = Button(frame, text="5", command=lambda: add("5"), bg='light blue', activebackground='orange', font="Times 18",
              width=6,
              height=2)
btn5.grid(row=4, column=3)

btn6 = Button(frame, text="6", command=lambda: add("6"), bg='light blue', activebackground='orange', font="Times 18",
              width=6,
              height=2)
btn6.grid(row=4, column=4)

btn1 = Button(frame, text="1", command=lambda: add("1"), bg='light blue', activebackground='orange', font="Times 18",
              width=6,
              height=2)
btn1.grid(row=5, column=2)

btn2 = Button(frame, text="2", command=lambda: add("2"), bg='light blue', activebackground='orange', font="Times 18",
              width=6,
              height=2)
btn2.grid(row=5, column=3)

btn3 = Button(frame, text="3", command=lambda: add("3"), bg='light blue', activebackground='orange', font="Times 18",
              width=6,
              height=2)
btn3.grid(row=5, column=4)

btn0 = Button(frame, text="0", command=lambda: add("0"), bg='light blue', activebackground='orange', font="Times 18",
              width=6,
              height=2)
btn0.grid(row=6, column=2)

btn_dot = Button(frame, text=".", command=lambda: add("."), bg='light blue', activebackground='orange',
                 font="Times 18", width=6,
                 height=2)
btn_dot.grid(row=6, column=3)

btn_del = Button(frame, text="DEL", command=delete, bg='light blue', activebackground='orange', font="Times 18",
                 width=6,
                 height=2)
btn_del.grid(row=6, column=4)

btn_div = Button(frame, text="/", command=lambda: add("/"), bg='light blue', activebackground='orange',
                 font="Times 18", width=6,
                 height=2)
btn_div.grid(row=3, column=5)

btn_mul = Button(frame, text="x", command=lambda: add("*"), bg='light blue', activebackground='orange',
                 font="Times 18", width=6,
                 height=2)
btn_mul.grid(row=4, column=5)

btn_sub = Button(frame, text="-", command=lambda: add("-"), bg='light blue', activebackground='orange',
                 font="Times 18", width=6,
                 height=2)
btn_sub.grid(row=5, column=5)

btn_add = Button(frame, text="+", command=lambda: add("+"), bg='light blue', activebackground='orange',
                 font="Times 18", width=6,
                 height=2)
btn_add.grid(row=6, column=5)

btn_clear = Button(frame, text="Clear", command=clear, bg='light blue', activebackground='orange', font="Times 18",
                   width=15,
                   height=2)
btn_clear.grid(row=7, column=2, columnspan=2)

btn_equal = Button(frame, text="=", command=calc, bg='light blue', activebackground='red', font="Times 18", width=15,
                   height=2)
btn_equal.grid(row=7, column=4, columnspan=2)

# /////////////////////////////////////////////////////////////////////////////////////////////

# code for Scientific Mode
# PLEASE NOTE THAT i have designed scientific mode which first accept numbers and then the operation


normal_clicked = True


def show_btn():
    global normal_clicked
    if normal_clicked:

        frame.pack_forget()
        window.geometry("420x680")
        sc_frame.pack()
        frame.pack()
        normal_clicked = False

    else:
        normal_clicked = True
        sc_frame.pack_forget()
        window.geometry("420x495")
        # frame.pack()
        entryText.set("")


def sc_calc(event):
    sc_val = ""
    sb = event.widget
    sc_text = sb['text']
    exp = entryText.get()
    if sc_text == "sinθ":
        sc_val = str(m.sin(m.radians(int(exp))))
        entryText.set(sc_val)

    elif sc_text == "cosθ":
        sc_val = str(m.cos(m.radians(int(exp))))
        entryText.set(sc_val)

    elif sc_text == "tanθ":
        sc_val = str(m.tan(m.radians(int(exp))))
        entryText.set(sc_val)

    elif sc_text == "x!":
        sc_val = str(m.factorial(int(exp)))
        entryText.set(sc_val)

    elif sc_text == "^":
        base, power = exp.split(",")
        sc_val = str(m.pow(int(base), int(power)))
        entryText.set(sc_val)

    elif sc_text == "ToDeg":
        sc_val = str(m.degrees(float(exp)))
        entryText.set(sc_val)

    elif sc_text == "ToRad":
        sc_val = str(m.radians(float(exp)))
        entryText.set(sc_val)

    elif sc_text == "√":
        sc_val = str(m.sqrt(int(exp)))
        entryText.set(sc_val)

    elif sc_text == ",":
        entryText.set(exp + sc_text)

    elif sc_text == "log":
        x, base = exp.split(",")
        sc_val = str(m.log(int(x), int(base)))
        entryText.set(sc_val)

    elif sc_text == "∏":
        sc_val = str(m.pi * (int(exp)))
        entryText.set(sc_val)

    elif sc_text == "└ Floor┘":
        sc_val = str(m.floor(float(exp)))
        entryText.set(sc_val)


# menu bar to show scientific mode
menuBar = Menu(window, activebackground='orange', foreground="red", font="Times 12 ")
mode = Menu(menuBar, tearoff=0)
mode.add_checkbutton(label="Scientific Calculator", command=show_btn)
menuBar.add_cascade(label="Menu", menu=mode)
window.config(menu=menuBar)

# create a frame for scientific mode buttons
sc_frame = Frame(window)
sc_frame.config(bg="powder blue")

# scientific mode buttons (action performed without using lambda function)


sin_btn = Button(sc_frame, text="sinθ", bg='light blue', activebackground='orange', font="Times 12", width=4, height=2)
sin_btn.grid(row=0, column=0, padx=4)
cos_btn = Button(sc_frame, text="cosθ", bg='light blue', activebackground='orange', font="Times 12", width=4, height=2)
cos_btn.grid(row=0, column=1, padx=4)
tan_btn = Button(sc_frame, text="tanθ", bg='light blue', activebackground='orange', font="Times 12", width=4, height=2)
tan_btn.grid(row=0, column=2, padx=4)
fact_btn = Button(sc_frame, text="x!", bg='light blue', activebackground='orange', font="Times 12", width=4, height=2)
fact_btn.grid(row=0, column=3, padx=4)

pow_btn = Button(sc_frame, text="^", bg='light blue', activebackground='orange', font="Times 12", width=4, height=2)
pow_btn.grid(row=0, column=4, padx=4)
deg_btn = Button(sc_frame, text="ToDeg", bg='light blue', activebackground='orange', font="Times 12", width=4, height=2)
deg_btn.grid(row=0, column=5, padx=4)
rad_btn = Button(sc_frame, text="ToRad", bg='light blue', activebackground='orange', font="Times 12", width=4, height=2)
rad_btn.grid(row=1, column=0, padx=4)
sqr_btn = Button(sc_frame, text="√", bg='light blue', activebackground='orange', font="Times 12", width=4, height=2)
sqr_btn.grid(row=1, column=1, padx=4)

coma_btn = Button(sc_frame, text=",", bg='light blue', activebackground='orange', font="Times 12", width=4, height=2)
coma_btn.grid(row=1, column=2, padx=4)
log_btn = Button(sc_frame, text="log", bg='light blue', activebackground='orange', font="Times 12", width=4, height=2)
log_btn.grid(row=1, column=3, padx=4)
pi_btn = Button(sc_frame, text="∏", bg='light blue', activebackground='orange', font="Times 12", width=4, height=2)
pi_btn.grid(row=1, column=4, padx=4)
flr_btn = Button(sc_frame, text="└ Floor┘", bg='light blue', activebackground='orange', font="Times 12", width=4,
                 height=2)
flr_btn.grid(row=1, column=5, padx=4)

# binding all scientific buttons
sin_btn.bind("<Button-1>", sc_calc)
cos_btn.bind("<Button-1>", sc_calc)
tan_btn.bind("<Button-1>", sc_calc)
fact_btn.bind("<Button-1>", sc_calc)
pow_btn.bind("<Button-1>", sc_calc)
deg_btn.bind("<Button-1>", sc_calc)
rad_btn.bind("<Button-1>", sc_calc)
sqr_btn.bind("<Button-1>", sc_calc)
coma_btn.bind("<Button-1>", sc_calc)
log_btn.bind("<Button-1>", sc_calc)
pi_btn.bind("<Button-1>", sc_calc)
flr_btn.bind("<Button-1>", sc_calc)

window.mainloop()
