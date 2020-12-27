import tkinter


def Calculate():
    miles = float(input_miles.get())
    reult = round(miles * 1.609)
    label_result.config(text=reult)


window = tkinter.Tk()
window.title("Milk to km calculate")
# window.minsize(width=300, height=300)

text_miles = tkinter.Label(text="Miles", font=("Arial", 12, "normal"))
text_miles.grid(column=2, row=0)

input_miles = tkinter.Entry(width=10)
input_miles.grid(column=1, row=0)

text_is_equal_to = tkinter.Label(text="is equal to", font=("Arial", 12, "normal"))
text_is_equal_to.grid(column=0, row=1)

text_km = tkinter.Label(text="km", font=("Arial", 12, "normal"))
text_km.grid(column=2, row=1)

label_result = tkinter.Label(text="0", font=("Arial", 12, "normal"))
label_result.grid(column=1, row=1)

button_Calculate = tkinter.Button(text="Calculate", command=Calculate)
button_Calculate.grid(column=1, row=2)

window.mainloop()

