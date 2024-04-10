from tkinter import END, messagebox,ttk
import tkinter as tk
import sys
import pandas as pd
import matplotlib.pyplot as plt

root = tk.Tk()
root.config(width=300,height=200)
root.title("Gráficas")

table = pd.read_csv(r'C:\Users\RICARDO\Downloads\datos.csv')

ttk.Label(root,text = "Buscar por:").place(x = 50, y = 30)

Filtro = ttk.Combobox(root, state = "readonly",values=["Ciudad", "Fecha", "Venta", "CostoEnvio", "TotalVenta"])
Filtro.place(x = 50, y = 50)

def Buscar():
    filtro = Filtro.get()

    if filtro == "Ciudad":
        df=dict(table.groupby('Ciudad')['NombreCliente'].size())
        plt.bar(df.keys(), df.values())
        plt.xlabel("Ciudad")
        plt.ylabel("Clientes")
        plt.title("Gráfica Ciudad")
        plt.show()
    
    elif filtro == "Fecha":
        df=dict(table.groupby('Fecha')['NombreCliente'].size())
        plt.bar(df.keys(), df.values())
        plt.xlabel("Fecha")
        plt.ylabel("Clientes")
        plt.title("Gráfica Fecha")
        plt.show()

    elif filtro == "Venta":
        df=dict(table.groupby('NombreCliente')['Venta'].size())
        plt.bar(df.keys(), df.values())
        plt.xlabel("Clientes")
        plt.ylabel("Ventas similares")
        plt.title("Gráfica Ventas Similares")
        plt.show()
    
    elif filtro == "CostoEnvio":
        df=dict(table.groupby('NombreCliente')['CostoEnvio'].size())
        plt.bar(df.keys(), df.values())
        plt.xlabel("Clientes")
        plt.ylabel("CostoEnvio")
        plt.title("Gráfica Costo de Envío")
        plt.show()

    elif filtro == "TotalVenta":
        df=dict(table.groupby('NombreCliente')['TotalVenta'].size())
        df2=dict(table.groupby('Ciudad')['TotalVenta'].size())
        DF = {**df, **df2}
        plt.bar(DF.keys(), DF.values())
        plt.xlabel("TotalVenta")
        plt.ylabel("Clientes y ciudades")
        plt.title("Gráfica Total Ventas")
        plt.show()

    else:
        messagebox.showinfo(message = "ERROR: No se ha seleccionado nada")


mostrar = ttk.Button(root, text = "Buscar", command = Buscar)
mostrar.place(x = 50, y = 90)


root.mainloop()