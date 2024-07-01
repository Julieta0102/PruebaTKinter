import tkinter as tk
from tkinter import messagebox as mb 
from conexion import conexionbbdd,cursor

ventana = tk.Tk()
ventana.geometry("850x500+500+200")
marco = tk.Frame(ventana)
user_entry = tk.Entry(ventana,width= 30)
passw_entry = tk.Entry(ventana,width=30)

def inicio():
    marco.pack()
    boton_IS = tk.Button(marco,text= "Iniciar sesion",command=login)
    boton_R = tk.Button(marco,text = "Registrarse",command= Registrarse)
    boton_IS.pack()
    boton_R.pack()

def match():
    user_entry
    passw_entry
    cursor.execute(f"select * from usuarios where nombre = '{user_entry.get()}' and contrasenia = '{passw_entry.get()}'")
    resultado = cursor.fetchall()
    if len(resultado) >0:
        menu()
    else:
        mb.showerror("Error")

def refresh():
    for i in ventana.pack_slaves():
        i.destroy()

def login ():
    marco.destroy()
    username_eti = tk.Label(ventana,text="Username")
    username_eti.place (x = 150 , y = 50)
    # global user_entry
    # user_entry = tk.Entry(ventana,width= 30)
    user_entry.place(x = 250 , y = 50)

    password_eti = tk.Label(ventana,text="Password")
    password_eti.place(x = 150 ,  y = 150)
    # global passw_entry
    # passw_entry = tk.Entry(ventana,width=30)
    passw_entry.place(x = 250 , y =150)

    ingresar_button = tk.Button(ventana,text="Ingresar",command= match)
    ingresar_button.place(x = 300 , y = 200)

def Insert_Into_Regis():
    sql = "Insert into usuarios (dni,nombre,telefono,direccion,situacion,contrasenia) VALUES (%s ,%s ,%s ,%s ,%s ,%s)"
    val = (int(dni_entry.get()),nombre_entry.get(),int(tel_entry.get()),dir_entry.get(),'L',contra_entry.get())
    cursor.execute(sql,val)
    conexionbbdd.commit()
    

def Registrarse ():
    refresh()
    #marco.destroy()

    global dni_entry
    dni_eti = tk.Label(ventana,text= "DNI")
    dni_eti.place(x = 50, y = 50)
    dni_entry = tk.Entry(ventana,width= 30)
    dni_entry.place(x = 150 , y =50)

    global nombre_entry
    nombre_eti = tk.Label(ventana,text="Nombre")
    nombre_eti.place(x = 50 , y = 100)
    nombre_entry = tk.Entry(ventana,width= 30)
    nombre_entry.place(x = 150 , y = 100)

    global tel_entry
    tel_eti = tk.Label(ventana,text = "Teléfono")
    tel_eti.place(x = 50 , y = 150)
    tel_entry = tk.Entry(ventana,width=30)
    tel_entry.place(x = 150 , y = 150)

    global dir_entry
    dir_eti = tk.Label(ventana,text= "Dirección")
    dir_eti.place(x = 50 , y = 200)
    dir_entry = tk.Entry(ventana,width=30)
    dir_entry.place(x = 150, y =200)

    global contra_entry
    contra_eti = tk.Label(ventana,text= "Contraseña")
    contra_eti.place(x = 50 , y =250)
    contra_entry = tk.Entry(ventana,width=30)
    contra_entry.place(x = 150 , y =250)

    boton_R = tk.Button(ventana,text = "Registrarse",command= Insert_Into_Regis)    
    boton_R.place(x = 500 , y = 150)

def menu ():
    refresh()
    menu_encabezado = tk.Label(ventana,text = "Menu Principal",font=("Calibri",15))
    menu_encabezado.pack()





inicio()
ventana.mainloop()
