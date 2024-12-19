import tkinter as tk
from tkinter import messagebox
import time

# Lista global para almacenar los valores grabados
valores_grabados = []

def funcion_q1(value):
    print(f"función q1 ejecutada con valor: {value}")

def funcion_q2(value):
    print(f"función q2 ejecutada con valor: {value}")

def funcion_q3(value):
    print(f"función q3 ejecutada con valor: {value}")

def funcion_q4(value):
    print(f"función q4 ejecutada con valor: {value}")

def grabar_valores():
    valores = [slider_q1.get(), slider_q2.get(), slider_q3.get(), slider_q4.get()]
    valores_grabados.append(valores)
    print(f"Valores grabados: {valores}")

def borrar_ultimo():
    if valores_grabados:
        valores_grabados.pop()
        print("Último valor borrado")
    else:
        print("No hay valores para borrar")

def mostrar_valores():
    if valores_grabados:
        messagebox.showinfo("Valores Grabados", f"{valores_grabados}")
    else:
        messagebox.showinfo("Valores Grabados", "No hay valores grabados")

def reset_valores():
    valores_grabados.clear()
    print("Todos los valores han sido reseteados")

def ejecutar_funciones():
    for valores in valores_grabados:
        funcion_q1(valores[0])
        funcion_q2(valores[1])
        funcion_q3(valores[2])
        funcion_q4(valores[3])
        time.sleep(1)

# Crear la ventana principal
root = tk.Tk()
root.title("Control de Trayectoria")
root.geometry("400x400")

# Títulos
title = tk.Label(root, text="Control de Trayectoria", font=("Arial", 16, "bold"))
title.pack(pady=5)

# Crear los deslizadores y etiquetas
frame_sliders = tk.Frame(root)
frame_sliders.pack(pady=5)

# Slider q1
label_q1 = tk.Label(frame_sliders, text="q1")
label_q1.grid(row=0, column=0, padx=5, pady=5)
slider_q1 = tk.Scale(frame_sliders, from_=0, to=180, orient=tk.HORIZONTAL, command=funcion_q1)
slider_q1.grid(row=0, column=1, padx=5, pady=5)
value_q1 = tk.Label(frame_sliders, text="0°")
value_q1.grid(row=0, column=2, padx=5, pady=5)
slider_q1.configure(command=lambda value: [funcion_q1(value), value_q1.config(text=f"{value}°")])

# Slider q2
label_q2 = tk.Label(frame_sliders, text="q2")
label_q2.grid(row=1, column=0, padx=5, pady=5)
slider_q2 = tk.Scale(frame_sliders, from_=0, to=180, orient=tk.HORIZONTAL, command=funcion_q2)
slider_q2.grid(row=1, column=1, padx=5, pady=5)
value_q2 = tk.Label(frame_sliders, text="0°")
value_q2.grid(row=1, column=2, padx=5, pady=5)
slider_q2.configure(command=lambda value: [funcion_q2(value), value_q2.config(text=f"{value}°")])

# Slider q3
label_q3 = tk.Label(frame_sliders, text="q3")
label_q3.grid(row=2, column=0, padx=5, pady=5)
slider_q3 = tk.Scale(frame_sliders, from_=0, to=180, orient=tk.HORIZONTAL, command=funcion_q3)
slider_q3.grid(row=2, column=1, padx=5, pady=5)
value_q3 = tk.Label(frame_sliders, text="0°")
value_q3.grid(row=2, column=2, padx=5, pady=5)
slider_q3.configure(command=lambda value: [funcion_q3(value), value_q3.config(text=f"{value}°")])

# Slider q4
label_q4 = tk.Label(frame_sliders, text="q4")
label_q4.grid(row=3, column=0, padx=5, pady=5)
slider_q4 = tk.Scale(frame_sliders, from_=0, to=180, orient=tk.HORIZONTAL, command=funcion_q4)
slider_q4.grid(row=3, column=1, padx=5, pady=5)
value_q4 = tk.Label(frame_sliders, text="0°")
value_q4.grid(row=3, column=2, padx=5, pady=5)
slider_q4.configure(command=lambda value: [funcion_q4(value), value_q4.config(text=f"{value}°")])

# Frame para los botones
frame_buttons1 = tk.Frame(root)
frame_buttons1.pack(pady=5)

# Primera fila de botones
grab_button = tk.Button(frame_buttons1, text="Grabar", command=grabar_valores)
grab_button.grid(row=0, column=0, padx=5, pady=5)

delete_button = tk.Button(frame_buttons1, text="Borrar", command=borrar_ultimo)
delete_button.grid(row=0, column=1, padx=5, pady=5)

show_button = tk.Button(frame_buttons1, text="Mostrar", command=mostrar_valores)
show_button.grid(row=0, column=2, padx=5, pady=5)

frame_buttons2 = tk.Frame(root)
frame_buttons2.pack(pady=5)

# Segunda fila de botones
ok_button = tk.Button(frame_buttons2, text="OK", command=ejecutar_funciones)
ok_button.grid(row=1, column=0, padx=5, pady=5)

reset_button = tk.Button(frame_buttons2, text="Reset", command=reset_valores)
reset_button.grid(row=1, column=1, padx=5, pady=5)

# Ejecutar la aplicación
root.mainloop()