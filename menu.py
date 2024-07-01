import tkinter as tk
import mysql.connector

conexion = mysql.connector.connect(host="localhost",user="root",password="" , database = "videoclub")
cursor = conexion.cursor()

"""def Inicio ():
    ventMenu.mainloop()
    if button_iniciar == True:
        match()
    else:
        None
"""
def ingresar ():
    vent_emergente = tk.Tk()
    vent_emergente.geometry("300x200+450+120")
    username = user_entry.get()
    password = pass_entry.get()
    cursor.execute(f"select * from usuarios where nombre ='{username}' and contrasenia = '{password}'")
    resultado = cursor.fetchall()
    if len(resultado) > 0:
        cartel = tk.Label(vent_emergente,text= "Ingreso exitoso")
        cartel.pack()
    else:
        cartel = tk.Label(vent_emergente,text= "Ingreso denegado")
        cartel.pack()
    

def login ():
    ventLogin = tk.Tk()
    ventLogin.geometry("580x400+500+200")
    
    etiqueta_Login = tk.Label(ventLogin,text = "Login", bg = "violet" , fg = "black" , font = ("calibri",15))
    etiqueta_Login.place(x = 280 , y = 50)
    
    etiqueta_user = tk.Label(ventLogin,text= "username")
    etiqueta_user.place(x =150 , y = 150 )
    
    global user_entry
    user_entry = tk.Entry(ventLogin,width= 30)
    user_entry.place(x =250 , y =150 )
    
    
    etiqueta_pass = tk.Label(ventLogin,text="password")
    etiqueta_pass.place(x= 150 , y = 200)
    
    global pass_entry
    pass_entry = tk.Entry(ventLogin,width= 30)
    pass_entry.place(x=250 , y = 200)
    
    button_ingresar = tk.Button(ventLogin,text= "Ingresar",command= ingresar)
    button_ingresar.place(x = 280 , y =280)




ventMenu = tk.Tk()
ventMenu.title = ("Mi App")
ventMenu.geometry("580x400+500+200")

Etiqueta_bienve = tk.Label(ventMenu,text= "Bienvenido a la App",bg="violet",fg = "black",font= ("calibri",20))
Etiqueta_bienve.pack()

button_iniciar = tk.Button(ventMenu,text = "Iniciar Sesion",command= login)
button_iniciar.place(x = 240 , y = 100)

button_registar = tk.Button(ventMenu, text = "Registrarse")
button_registar.place (x = 240 ,y = 150)

ventMenu.mainloop()
