from tkinter import END, messagebox,ttk
import tkinter as tk
import pandas as pd

root = tk.Tk()  
root.config(width=800,height=800)
root.title("Frecuencias")

table = pd.read_csv(r'C:\Users\RICARDO\Downloads\MOCK_DATA.csv')
  
ttk.Label(root, text = "Categoría").place(x=50,y=30)
ttk.Label(root, text = "Dato --- (Frecuencia)").place(x = 50, y = 110)

Filtro = ttk.Combobox(root, state="readonly", values = ["Edad", "Ocupación"])
Filtro.place(x=50,y=50)

def Buscar():
    indice = 0
    filtro = Filtro.get()
    listbox.delete(0,END)

    if filtro == "Edad":
        frec = table["edad"].value_counts().to_dict()
        for i in frec.keys():
            indice +=  1
            listbox.insert(indice, "%s --- (%s)" % (i, frec[i]))
       
    elif filtro == "Ocupación":
        frec = table["ocupacion"].value_counts().to_dict()
        for i in frec.keys():
            indice +=  1
            listbox.insert(indice, "%s --- (%s)" % (i, frec[i]))
    else:
        messagebox.showinfo(message = "ERROR: No se ha seleccionado nada")  

listbox = tk.Listbox(root, width = 50, height=90)
listbox.place(x = 50,y = 130)

botonMostrar = ttk.Button(root, text = "Buscar", command = Buscar).place(x=200, y=48)

root.mainloop()