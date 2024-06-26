import tkinter as tk

"""def Inicio ():
    ventMenu.mainloop()
    if button_iniciar == True:
        match()
    else:
        None
"""

def login ():
    ventLogin = tk.Tk()
    ventLogin.geometry("580x400+500+200")
    etiqueta_Login = tk.Label(ventLogin,text = "Login", bg = "violet" , fg = "black" , font = ("calibri",15))
    etiqueta_Login.place(x = 280 , y = 50)
    etiqueta_user = tk.Label(ventLogin,text= "username")
    etiqueta_user.place(x =150 , y = 150 )
    user_entry = tk.Entry(ventLogin,width= 30)
    user_entry.place(x =250 , y =150 )
    etiqueta_pass = tk.Label(ventLogin,text="password")
    etiqueta_pass.place(x= 150 , y = 200)
    pass_entry = tk.Entry(ventLogin,width= 30)
    pass_entry.place(x=250 , y = 200)
    button_ingresar = tk.Button(ventLogin,text= "Ingresar")




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
