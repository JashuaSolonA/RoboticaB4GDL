import tkinter as tk

def reset_fields():
    for entry in entries:
        entry.delete(0, tk.END)
        entry.insert(0, "0")

def cinematica_inversa():
    print("Función cinemática inversa ejecutada")

def abrir_control_directo():
    def actualizar_label(value, label):
        label.config(text=f"{int(float(value))}°")
        cinematica_directa()

    def cinematica_directa():
        print("Función cinemática directa ejecutada")

    # Crear nueva ventana
    control_window = tk.Toplevel(root)
    control_window.title("Control Directo de Manipulador")
    control_window.geometry("400x350")

    # Título principal
    title = tk.Label(control_window, text="Control Directo de Manipulador", font=("Helvica", 16, "bold"))
    title.pack(pady=10)

    # Subtítulo
    subtitle = tk.Label(control_window, text="Universidad Nacional de Trujillo", font=("Helvica", 14))
    subtitle.pack(pady=5)

    # Frame para deslizadores
    slider_frame = tk.Frame(control_window)
    slider_frame.pack(pady=15)

    sliders = []
    for i in range(4):
        tk.Label(slider_frame, text=f"Ángulo {i + 1}:").grid(row=i, column=0, padx=5, pady=5)
        slider = tk.Scale(slider_frame, from_=0, to=180, orient=tk.HORIZONTAL, command=lambda value, i=i: actualizar_label(value, labels[i]))
        slider.grid(row=i, column=1, padx=5, pady=5)
        sliders.append(slider)
        label = tk.Label(slider_frame, text="0°")
        label.grid(row=i, column=2, padx=5, pady=5)
        labels.append(label)

# Crear la ventana principal
root = tk.Tk()
root.title("Manipulación de Posición Final")
root.geometry("400x300")

# Título principal
title = tk.Label(root, text="Manipulación de Posición Final", font=("Helvica", 16, "bold"))
title.pack(pady=10)

# Subtítulo
subtitle = tk.Label(root, text="Universidad Nacional de Trujillo", font=("Helvica", 14))
subtitle.pack(pady=5)

# Frame para centrar los elementos
frame = tk.Frame(root)
frame.pack(pady=10)

entries = []

# Crear etiquetas y entradas

label_px = tk.Label(frame, text="Px:")
label_px.grid(row=1, column=1, padx=5, pady=5)

entry_px = tk.Entry(frame)
entry_px.grid(row=1, column=2, padx=5, pady=5)

label_py = tk.Label(frame, text="Py:")
label_py.grid(row=2, column=1, padx=5, pady=5)

entry_py = tk.Entry(frame)
entry_py.grid(row=2, column=2, padx=5, pady=5)

label_pz = tk.Label(frame, text="Pz:")
label_pz.grid(row=3, column=1, padx=5, pady=5)

entry_pz = tk.Entry(frame)
entry_pz.grid(row=3, column=2, padx=5, pady=5)

# Frame para los botones
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Botón OK
ok_button = tk.Button(button_frame, text="OK", command=cinematica_inversa)
ok_button.pack(side="left", padx=10)

# Botón Reset
reset_button = tk.Button(button_frame, text="Reset", command=reset_fields)
reset_button.pack(side="right", padx=10)

# Botón para abrir Control Directo
control_directo_button = tk.Button(root, text="Abrir Control Directo", command=abrir_control_directo)
control_directo_button.pack(pady=10)

# Lista de etiquetas para sliders
labels = []

# Ejecutar la aplicación
root.mainloop()
