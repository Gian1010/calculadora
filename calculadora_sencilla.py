import tkinter as tk
from tkinter import messagebox

def sumar():
    try: 
        num1 = float(num1_user.get())
        num2 = float(num2_user.get())
        resultado = num1 + num2 
        label_resultado.config(text = f'Resultado:  {resultado}')
    except ValueError:
        messagebox.showerror('Error','Ingrese numeros validos')

def restar():
    try:
        num1 = float(num1_user.get())
        num2 = float(num2_user.get())
        resultado = num1 - num2 
        label_resultado.config(text = f'Resultado:  {resultado}')
    except ValueError:
        messagebox.showerror('Error','Ingrese numeros validos')

def multiplicar():
    try:
        num1 = float(num1_user.get())
        num2 = float(num2_user.get())
        resultado = num1 * num2 
        label_resultado.config(text = f'Resultado:  {resultado}')
    except ValueError:
        messagebox.showerror('Error','Ingrese numeros validos')

def dividir():
    try:
        num1 = float(num1_user.get())
        num2 = float(num2_user.get())
        if num2 == 0:
            messagebox.showerror('Error','Ingrese numeros validos, no se puede dividir por 0')
        else:
            resultado = num1 / num2 
            label_resultado.config(text = f'Resultado:  {resultado}')
    except ValueError:
        messagebox.showerror('Error','Ingrese numeros validos')

def conversion_dolar():
    try:
        num1 = float(num1_user.get())
        resultado = num1 / valor_dolar
        label_resultado.config(text = f'Resultado:  {resultado} : Dolares')
    except ValueError:
        messagebox.showerror('Error','Ingrese un valor valido')

def conversion_euro():
    try:
        num1 = float(num1_user.get())
        resultado = num1 / valor_euro
        label_resultado.config(text = f'Resultado:  {resultado} : Euros')
    except ValueError:
        messagebox.showerror('Error','Ingrese un valor valido')   

valor_dolar = 949
valor_euro = 1054

root = tk.Tk()
root.title('Calculadora')
root.geometry('300x150')
root.configure(bg='black')

label_num1 = tk.Label(root, text = 'Numero 1', bg='black', fg='cyan', font=('Arial', 12, 'bold'))
label_num1.grid(row=0, column=0)
num1_user = tk.Entry(root)
num1_user.grid(row=0, column=1)

label_num2 = tk.Label(root, text = 'Numero 2', bg='black', fg='cyan', font=('Arial', 12, 'bold'))
label_num2.grid(row=1, column=0)
num2_user = tk.Entry(root)
num2_user.grid(row=1, column=1)

label_resultado = tk.Label(root, text= 'Resultado', bg='black', fg='cyan', font=('Arial', 12, 'bold'))
label_resultado.grid(row=4, column= 0, columnspan=2)

boton_sumar = tk.Button(root, text='sumar', command= sumar, bg='black', fg='cyan', font=('Arial', 12, 'bold'))
boton_sumar.grid(row= 2, column=0)

boton_restar = tk.Button(root, text='restar', command= restar, bg='black', fg='cyan', font=('Arial', 12, 'bold'))
boton_restar.grid(row= 2, column=1)

boton_multiplicar = tk.Button(root, text='multiplicar', command= multiplicar, bg='black', fg='cyan', font=('Arial', 12, 'bold'))
boton_multiplicar.grid(row= 3, column=0)

boton_dividir = tk.Button(root, text='dividir', command= dividir, bg='black', fg='cyan', font=('Arial', 12, 'bold'))
boton_dividir.grid(row= 3, column=1)

boton_dolar = tk.Button(root, text='dolar', command= conversion_dolar, bg='black', fg='cyan', font=('Arial', 12, 'bold'))
boton_dolar.grid(row= 2, column=2)

boton_euro = tk.Button(root, text='euro', command= conversion_euro, bg='black', fg='cyan', font=('Arial', 12, 'bold'))
boton_euro.grid(row= 3, column=2)

root.mainloop()