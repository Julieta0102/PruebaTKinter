import tkinter
import time

def funcion():
    root.state(newstate='withdraw')
    time.sleep(5)
    root.state(newstate='normal')

root = tkinter.Tk()
boton = tkinter.Button(root, text="Probando el metodo state", command=funcion)
boton.pack()
root.mainloop()