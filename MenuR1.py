import tkinter as tk
from tkinter import messagebox as mb 
from conexion import conexionbbdd,cursor


def inicio():
    refresh()
    boton_IS = tk.Button(ventana,text= "Iniciar sesion",command=login)
    boton_R = tk.Button(ventana,text = "Registrarse",command= Registrarse)
    boton_IS.pack()
    boton_R.pack()

def match():
    cursor.execute(f"select * from usuarios where nombre = '{user_entry.get()}' and contrasenia = '{passw_entry.get()}'")
    resultado = cursor.fetchall()
    if len(resultado) >0:
        menu(resultado[0])
    else:
        mb.showerror("Error")
    

def refresh():
    for i in ventana.pack_slaves():
        i.destroy()
    for i in ventana.place_slaves():
        i.destroy()


def login ():
    refresh()
    login_encabezado = tk.Label(ventana,text = "Login",bg= "green",font=("Calibri",14))
    login_encabezado.pack()
    username_eti = tk.Label(ventana,text="Username")
    username_eti.place (x = 320 , y = 100)
    user_entry.place(x = 400 , y = 100)

    password_eti = tk.Label(ventana,text="Password")
    password_eti.place(x = 320 ,  y = 150)
    passw_entry.place(x = 400 , y =150)

    ingresar_button = tk.Button(ventana,text="Ingresar",command= match)
    ingresar_button.place(x = 340 , y = 200)

    boton_c = tk.Button(ventana,text= "Cancelar",command=inicio)
    boton_c.place(x= 450 , y =200)

def Insert_Into_Regis():
    sql = "Insert into usuarios (dni,nombre,telefono,direccion,situacion,contrasenia) VALUES (%s ,%s ,%s ,%s ,%s ,%s)"
    val = (int(dni_entry.get()),nombre_entry.get(),int(tel_entry.get()),dir_entry.get(),'L',contra_entry.get())
    cursor.execute(sql,val)
    conexionbbdd.commit()
    login()
    

def Registrarse ():
    refresh()
    dni_eti = tk.Label(ventana,text= "DNI")
    dni_eti.place(x = 50, y = 50)
    dni_entry.place(x = 150 , y =50)

    nombre_eti = tk.Label(ventana,text="Nombre")
    nombre_eti.place(x = 50 , y = 100)
    nombre_entry.place(x = 150 , y = 100)

    tel_eti = tk.Label(ventana,text = "Teléfono")
    tel_eti.place(x = 50 , y = 150)
    tel_entry.place(x = 150 , y = 150)

    dir_eti = tk.Label(ventana,text= "Dirección")
    dir_eti.place(x = 50 , y = 200)
    dir_entry.place(x = 150, y =200)

    contra_eti = tk.Label(ventana,text= "Contraseña")
    contra_eti.place(x = 50 , y =250)
    contra_entry.place(x = 150 , y =250)

    boton_R = tk.Button(ventana,text = "Registrarse",command= Insert_Into_Regis)    
    boton_R.place(x = 500 , y = 150)

    boton_c = tk.Button(ventana,text= "Cancelar",command=inicio)
    boton_c.place(x = 500 , y = 250)
    

def menu (x): #parametro result[0] - tupla login
    refresh()
    menu_encabezado = tk.Label(ventana,text = "Menu Principal",bg= "yellow",font=("Calibri",15))
    menu_encabezado.pack()

    marco_datos = tk.Frame(ventana, width=700, height=150, bd=2, relief="solid")
    marco_datos.pack()
    
    nombre_eti = tk.Label(marco_datos,text= "Nombre :")
    nombre_eti.place(x = 0 , y = 0)
    nombre_user = tk.Label(marco_datos,text= f"{x[2]}")
    nombre_user.place(x = 60 , y = 0)

    dni_eti = tk.Label(marco_datos,text= "DNI : ")
    dni_eti.place(x = 0 , y = 20)
    dni_user = tk.Label(marco_datos,text= f"{x[1]}")
    dni_user.place(x = 60 , y = 20)

    tel_eti = tk.Label(marco_datos,text= "Teléfono: ")
    tel_eti.place(x = 0 , y = 40)
    tel_user = tk.Label(marco_datos,text= f"{x[3]}")
    tel_user.place(x = 60 , y = 40)

    direccion_eti = tk.Label(marco_datos,text= "Dirección : ")
    direccion_eti.place(x = 0 , y = 60)
    direccion_user = tk.Label(marco_datos,text= f"{x[4]}")
    direccion_user.place(x = 60 , y = 60)

    situacion_eti = tk.Label(marco_datos,text= "Situación : ")
    situacion_eti.place(x = 0 , y = 80)
    situacion_user = tk.Label(marco_datos,text= f"{x[5]}")
    situacion_user.place(x = 60 , y = 80)

    contrasenia_eti = tk.Label(marco_datos,text= "Contraseña : ")
    contrasenia_eti.place(x = 0 , y = 100)
    contrasenia_user = tk.Label(marco_datos,text= f"{x[6]}")
    contrasenia_user.place(x = 60 , y = 100) 

    #Hacer 2 botones para actualizar telefono y dreccion


def datos_perso():
    cursor.execute(f"select * from usuarios where nombre = '{user_entry.get()}' and contrasenia = '{passw_entry.get()}'")



ventana = tk.Tk()
ventana.geometry("850x500+500+200")
user_entry = tk.Entry(ventana,width= 30)
passw_entry = tk.Entry(ventana,width=30)

dni_entry = tk.Entry(ventana,width= 30)
nombre_entry = tk.Entry(ventana,width= 30)
tel_entry = tk.Entry(ventana,width=30)
dir_entry = tk.Entry(ventana,width=30)
contra_entry = tk.Entry(ventana,width=30)

inicio()
ventana.mainloop()
