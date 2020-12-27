import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 12, "bold"))
my_label.grid(column=0, row=0)

# my_label["text"] = "Next Text"
my_label.config(text="New Text")


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = tkinter.Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

another_button = tkinter.Button(text="Click me", command=button_clicked)
another_button.grid(column=2, row=0)


input = tkinter.Entry(width=10)
input.grid(column=3, row=2)


window.mainloop()
