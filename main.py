import tkinter
window=tkinter.Tk()
window.title("Mile to Km converter")
window.config(padx=20,pady=20)
label=tkinter.Label(text="is equal to")
label.grid(column=0,row=1)
input=tkinter.Entry(width=10)
input.get()
input.grid(row=0,column=1)
label1=tkinter.Label(text=0)
label1.grid(column=1,row=1)
label2=tkinter.Label(text="Km")
label2.grid(column=2,row=1)
label3=tkinter.Label(text="Miles")
label3.grid(column=2,row=0)
def change():
    a=float(input.get())
    result=a*1.6909344
    label1.config(text=f"{round(result)}")
button=tkinter.Button(text="Calculate",command=change)
button.grid(column=1,row=2)


window.mainloop()
