import tkinter as tk

def match():
    username = ingreso.get()
    password = ingreso2.get()
    if username == password:
        print("Ingreso Exitoso")
    else:
        print("Acceso denegado")

ventana = tk.Tk() #lo convierte en objeto
ventana.title("Mi App")
ventana.geometry("850x500+500+200") #ancho,largo,+100+50(posicion)
etiqueta = tk.Label(ventana,text= "Bienvenido al Videoclub",bg="green",fg = "white",font= ("arial black",10))
etiqueta.pack()
etiqueta1 = tk.Label(ventana,text= "Login", font =("arial black",10))
etiqueta1.pack()
etiqueta2 = tk.Label(ventana,text= "Username")
etiqueta2.place(x = 50 , y = 80)
etiqueta3 = tk.Label(ventana,text= "Password")
etiqueta3.place(x = 50, y = 140 )
ingreso = tk.Entry(width= 40) #usernamae
ingreso.place(x = 150 , y = 80)
ingreso2 = tk.Entry(width= 40) #password
ingreso2.place(x = 150 , y = 140)
button = tk.Button(text= "Ingresar",command= match)
button.place(x = 400, y= 200 )



ventana.mainloop()



