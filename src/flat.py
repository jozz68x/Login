# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="admin"
__date__ ="$28/01/2015 01:39:15 AM$"


from tkinter import *
from tkinter import messagebox
from tkinter import ttk


class GenerarAcceso:
    def __init__(self):
        self.interfaz_generar_acceso()
        self.interfaz_widgets_generar_acceso()
             
    def interfaz_generar_acceso(self):
        self.master = Tk()
        self.master.title("Login")
        self.master.geometry("410x180+480+230")
        self.master.focus_set()
        self.master["background"] = "#37474f"
        self.master.overrideredirect(True) # desabilita el borde de la ventana
        #self.master.maxsize(430,190)              #este codigo establece el tamanio maximo de la ventana sin posibilidada a crecer mas
        #self.master.minsize(430,190)              #este codigo establece el tamanio minimo de la ventana
        #self.master.resizable(width=False, height=False) #este codigo evita o controla el posicionamiento de la ventana, desabilita el boton de maximizado y restaurado de la ventana
        self.master.grab_set()        #este codigo hace que desabilita todas las ventanas hasta que sea destruida esta ventana
        
        self.master.bind('<Escape>', lambda e: self.master.destroy()) #Presionando la tecla esc sale del programa
        
    def interfaz_widgets_generar_acceso(self):
        f1 = Frame(self.master, bg=self.master['bg'], relief=FLAT)
        f1.pack(fill=X, pady=30)
        f2 = Frame(self.master, bg=self.master['bg'], relief=FLAT)
        f2.pack(fill=X, pady=10)
        Label(f1,text="Usuario: ",bg=self.master['bg'],fg="white",font=("Adobe Fan Heiti Std B",11)).pack(side=LEFT, anchor='w', padx=10)  
        self.entryUsuarioGenerar = ttk.Entry(f1, width=25,font=("Franklin Gothic Book",12))
        self.entryUsuarioGenerar.focus()
        self.entryUsuarioGenerar.pack(side=RIGHT, anchor='e', padx=10)
        Label(f2,text="Password: ",bg=self.master['bg'],fg="white",font=("Adobe Fan Heiti Std B",11)).pack(side=LEFT, anchor='w', padx=10)
        self.entryPasswordGenerar = ttk.Entry(f2,show='*', width=25,font=("Franklin Gothic Book",12))
        self.entryPasswordGenerar.pack(side=RIGHT, anchor='e', padx=10)
        
        buttonGenerarAcceso = Button(self.master, relief=FLAT, command=self.acceso, cursor="hand2",width=13,bd=1,font=("Franklin Gothic Book",10), compound=CENTER,bg="#00887a",fg="white",text="Ingresar",activebackground="#333333",activeforeground="#ffffff")
        buttonGenerarAcceso.pack(side=BOTTOM, anchor='e', padx=10, pady=10)
        
        self.master.mainloop()

    def acceso(self):
        messagebox.showinfo(title="Bienvenido", message="LOGEO CORRECTO jajajaj")



if __name__ == "__main__":
        GenerarAcceso()