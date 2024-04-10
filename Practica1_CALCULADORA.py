from logging import root
from tkinter import END,messagebox, ttk
import tkinter as tk

root=tk.Tk()
root.config(width = 400, height = 330)
root.title("Calculadora")
ttk.Label(root, text="Ingrese numero 1: ").place(x = 30, y = 10)
txtNumero1 = ttk.Entry()
txtNumero1.place(x = 130, y = 10)

ttk.Label(root, text="Ingrese numero 2: ").place(x = 30, y = 60)
txtNumero2 = ttk.Entry()
txtNumero2.place(x = 130, y = 60)

ttk.Label(root, text="Resultado: ").place(x = 30, y = 110)
txtResultado = ttk.Entry()
txtResultado.place(x = 100, y = 110)

def suma():
    resultado=0
    numero1=float(txtNumero1.get())
    numero2=float(txtNumero2.get())
    resultado=numero1+numero2
    txtResultado.delete(0,END)
    txtResultado.insert(0, resultado)

def resta():
    resultado=0
    numero1=float(txtNumero1.get())
    numero2=float(txtNumero2.get())
    resultado=numero1-numero2
    txtResultado.delete(0,END)
    txtResultado.insert(0, resultado)

def multiplicacion():
    resultado=0
    numero1=float(txtNumero1.get())
    numero2=float(txtNumero2.get())
    resultado=numero1*numero2
    txtResultado.delete(0,END)
    txtResultado.insert(0, resultado)

def division():
    resultado=0
    numero1=float(txtNumero1.get())
    numero2=float(txtNumero2.get())
    resultado=numero1/numero2
    txtResultado.delete(0,END)
    txtResultado.insert(0, resultado)

def porciento():
    resultado=0
    numero1=float(txtNumero1.get())
    numero2=float(txtNumero2.get())
    resultado=((numero1*numero2)/100)
    txtResultado.delete(0,END)
    txtResultado.insert(0, resultado)

def cuadrado():
    resultado=0
    numero1=int(txtNumero1.get())
    resultado=numero1*numero1
    txtResultado.delete(0,END)
    txtResultado.insert(0, resultado)

def cubo():
    resultado=0
    numero1=int(txtNumero1.get())
    resultado=resultado=numero1*numero1*numero1
    txtResultado.delete(0,END)
    txtResultado.insert(0, resultado)

btnSuma=ttk.Button(root, text="+", command=suma)
btnSuma.place(x=30, y=150)

btnResta=ttk.Button(root, text="-", command=resta)
btnResta.place(x=130, y=150)

btnMulti=ttk.Button(root, text="*", command=multiplicacion)
btnMulti.place(x=30, y=180)

btnDiv=ttk.Button(root, text="/", command=division)
btnDiv.place(x=130, y=180)

btnCuadrado=ttk.Button(root, text="^2", command=cuadrado)
btnCuadrado.place(x=30, y=210)

btnCubo=ttk.Button(root, text="^3", command=cubo)
btnCubo.place(x=85, y=240)

btnPorc=ttk.Button(root, text="%", command=porciento)
btnPorc.place(x=130, y=210)



ttk.Label(root, text="Para elevar al cubo y cuadrado, ingrese solo el primer numero").place(x = 3, y = 280)
ttk.Label(root, text="Para el porcentaje, el primer numero es el porcentaje a calcular").place(x = 3, y = 300)

root.mainloop()