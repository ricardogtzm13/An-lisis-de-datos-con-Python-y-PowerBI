from tkinter import END,messagebox, ttk
import tkinter as tk
import math

root=tk.Tk()
root.config(width = 300, height = 300)
root.title("Estadistica")
ttk.Label(root, text="Seleccione una opcion: ").place(x = 50, y = 30)
cbOpcion=ttk.Combobox(root, state="readonly", values=["Media", "Mediana", "Moda", "Desviacion Media"])
cbOpcion.place(x=50,y=50)

conjunto=[2,4,8,5,4,5,6,2,5,2,5,1,5,9,7]
ttk.Label(root, text="CONJUNTO: [2,4,8,5,4,5,6,2,5,2,5,1,5,9,7]").place(x = 30, y = 150)
ttk.Label(root, text="CONJUNTO ORDENADO: 122244555556789").place(x = 30, y = 170)
def media():
    prom=0
    x=0
    while x<15:
        prom+=conjunto[x]
        x+=1
    return prom/15

def moda():
    lista = {}
    mayor = 0
    for x in conjunto:
        if x in lista.keys():
            lista[x] += 1
        else:
            lista[x] = 1
    for x in conjunto:
        if lista[x] > mayor:
            moda = x
            mayor = lista[x]
    return moda

def mediana():
    conjunto.sort()
    mediana = conjunto[int(len(conjunto)/2)]
    return mediana

def desviacion():
    media = 0
    desv = 0
    for x in conjunto:
        media += x
        media /= len(conjunto)
    for x in conjunto:
        desv += (x - media)**2
        desv /= len(conjunto)
        desv = math.sqrt(desv) 
    return desv
    

def estadistica():
    opcion=cbOpcion.get()
    if opcion == "Media":
        messagebox.showinfo(message="El promedio es: " + str(media()))
    elif opcion == "Mediana":
        messagebox.showinfo(message="La mediana es: " + str(mediana()))
    elif opcion == "Moda":
        messagebox.showinfo(message="La moda es: " + str(moda()))
    elif opcion == "Desviacion Media":
        messagebox.showinfo(message="La desviacion media es: " + str(desviacion()))
    else:
        messagebox.showerror(message="No ha seleccionado nada")

btnCalcular=ttk.Button(root, text="Calcular", command=estadistica)
btnCalcular.place(x = 50, y = 80)

root.mainloop()