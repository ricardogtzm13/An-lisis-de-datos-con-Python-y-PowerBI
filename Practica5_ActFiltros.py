from tkinter import END, messagebox,ttk
import tkinter as tk
import pandas as pd

root = tk.Tk()
root.config(width=600,height=800)
root.title("Filtros")

table = pd.read_csv(r'C:\Users\RICARDO\Downloads\MOCK_DATA.csv')
Tabla = []

ttk.Label(root,text = "Buscar por:").place(x = 50, y = 30)

Filtro = ttk.Combobox(root, state = "readonly",values=["Edad", "Ocupación"])
Filtro.place(x = 50, y = 50)

ttk.Label(root, text = "Valores a buscar:").place(x = 200, y = 30)
Entrada = ttk.Entry()
Entrada.place(x = 200, y = 50)

listbox = tk.Listbox(root, width=50, height=90) 
listbox.place(x = 50, y = 120)

def Buscar():
    filtro = Filtro.get()
    entrada = Entrada.get()
    listbox.delete(0, END)

    if filtro == "Edad":
        for x in range(0, table.count()[1]):
            Tabla = table.iloc[x]
            if entrada == str(Tabla[2]):
                listbox.insert(END, 'ID: '+ str(Tabla[0]))
                listbox.insert(END, 'NOMBRE: '+ str(Tabla[1]))
                listbox.insert(END, 'EDAD: '+ str(Tabla[2]))
                listbox.insert(END, 'OCUPACIÓN: '+ str(Tabla[3]))
                listbox.insert(END, '                            ')
                listbox.insert(END, '                            ')
    
    elif filtro == "Ocupación":
        for x in range(0,table.count()[1]):
            Tabla = table.iloc[x]
            if entrada == str(Tabla[3]):
                listbox.insert(END, 'ID: '+ str(Tabla[0]))
                listbox.insert(END, 'NOMBRE: '+ str(Tabla[1]))
                listbox.insert(END, 'EDAD: '+ str(Tabla[2]))
                listbox.insert(END, 'OCUPACIÓN: '+ str(Tabla[3]))
                listbox.insert(END, '                            ')
                listbox.insert(END, '                            ')
    
    else:
        messagebox.showinfo(message = "ERROR: No se ha seleccionado nada")

def Limpiar():
    listbox.delete(0,END)

mostrar = ttk.Button(root, text = "Buscar", command = Buscar)
mostrar.place(x = 50, y = 90)

limpiar = ttk.Button(root, text = "Limpiar", command = Limpiar)
limpiar.place(x = 140, y = 90)

root.mainloop()