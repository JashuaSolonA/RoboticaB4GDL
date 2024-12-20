import tkinter as tk
from tkinter import messagebox,filedialog
import RPi.GPIO as GPIO
from time import sleep
from math import atan, sqrt, cos, pi, sin
import pandas as pd

#Servos

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

def set_servo_angle(angle,servo):
    duty_cycle = 2 + (angle / 18)  
    servo.ChangeDutyCycle(duty_cycle)
    sleep(0.1)
    servo.ChangeDutyCycle(0)  

def set_road(angle,servo):
    duty_cycle = 2 + (angle / 18)  
    servo.ChangeDutyCycle(duty_cycle)
    sleep(0.5)
    servo.ChangeDutyCycle(0) 

#Para q1

servo_1 = GPIO.PWM(11, 50) 
servo_1.start(0)

def update_servo1(val):
    angle = int(val)
    set_servo_angle(angle,servo_1)

def trayectoria_1(val):
    angle = int(val)
    set_road(angle,servo_1)

#Para q2

def funcion_q2(value):
    print("Bloqueado")

#Para q3

servo_2 = GPIO.PWM(13, 50) 
servo_2.start(0)

def update_servo2(val):
    angle = int(val)
    set_servo_angle(angle,servo_2)

def trayectoria_2(val):
    angle = int(val)
    set_road(angle,servo_2)

#Para q4

servo_3 = GPIO.PWM(15, 50) 
servo_3.start(0)

def update_servo3(val):
    angle = int(val)
    set_servo_angle(angle,servo_3)

def trayectoria_3(val):
    angle = int(val)
    set_road(angle,servo_3)

#Inversa

def angulos(X,Y,Z,c):
    L1=0.046; 
    L2=0.2; 
    L3=0.2; 
    L4=0.154;

    #q1
    q1 = atan(Y/X)

    M = sqrt(X**2+Y**2)
    Lx = L4 * cos(c*pi/180)
    Lz = L4 * sin(c*pi/180)
    X1=M-Lx
    Z1=Z-Lz-L1
    h = sqrt(X1**2+Z1**2)

    #q3
    cosq3 = (h**2 - L2**2 - L3 **2)/(2*L2*L3)
    #q3=atan(sqrt(1-cosq3.^2)/cosq3) ##Codo abajo
    q3 = atan(-sqrt(1-cosq3**2)/cosq3) #Codo arriba

    #Variable q2
    beta = atan(Z1/X1)
    cosphi = (h**2 + L2**2 - L3**2)/(2*h*L2)
    # #phi=atan(sqrt(1-cosphi.^2)/cosphi) #Codo abajo
    phi = atan(-sqrt(1-cosphi**2)/cosphi) #Codo arriba
    q2 = beta - phi
    
    #q4
    q4 = c*pi/180-q2-q3

    q1_deg = round(q1*180/pi)
    q2_deg = round(q2*180/pi)
    q3_deg = round(q3*180/pi)
    q4_deg = round(q4*180/pi)

    if q1_deg > 180 or q1_deg < 0:
        q1_deg = 0
        print("q1 fuera de rango, Singularidad")
    if q2_deg > 180 or q2_deg < 0:
        q2_deg = 0
        print("q2 fuera de rango, Singularidad")
    if q3_deg > 180 or q3_deg < 0:
        q3_deg = 0
        print("q3 fuera de rango, Singularidad")
    if q4_deg > 180 or q4_deg < 0:
        q4_deg = 0
        print("q4 fuera de rango, Singularidad")

    #Salida
    return q1_deg,q2_deg,q3_deg,q4_deg

# Extraer coodernadas de un archivo CSV

entries = []

def process_csv():
    filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if not filepath:
        return
    try:
        data = pd.read_csv(filepath, header=None)        
        coordinates = data.values.tolist()
        processed_coordinates = [row[:3] for row in coordinates if len(row) >= 3]
        entries = processed_coordinates
        messagebox.showinfo("Exitoso", f"Procesado {len(processed_coordinates)}!")
        # print("Coordenadas:", processed_coordinates)

    except Exception as e:
        messagebox.showerror("Error", f"Fallo al procesar el Archivo:\n{e}")


# Funcion de Cinematica Inversa

def cinematica_inversa():
    try:
        X = float(entry_px.get())
        Y = float(entry_py.get())
        Z = float(entry_pz.get())
    except ValueError:
        messagebox.showerror("Error", "Ingrese valores numericos")
        return
    
    c = 0
    q1, q2, q3, q4 = angulos(X, Y, Z, c)
    print(f"q1: {q1}, q2: {q2}, q3: {q3}, q4: {q4}")

    #Marcando Trayectoria

    trayectoria_1(q1)
    sleep(0.1)
    trayectoria_2(q3)
    sleep(0.1)
    trayectoria_3(q4)
    sleep(0.1)

def cinematica_inversa_modificada():

    #Iniciamos Variables
    X = []
    Y = []
    Z = []
    q1 = []
    q2 = []
    q3 = []
    q4 = []

    #Bucle para obtener Coordendas
    for i in range(len(entries)):
        X = entries[i][0]
        Y = entries[i][1]
        Z = entries[i][2]
    
    c = 0

    #Bucle para obtener movimiento

    for i in range(len(entries)):
        q1[i], q2[i], q3[i], q4[i] = angulos(X[i], Y[i], Z[i], c)


    for i in range(len(entries)):    
        trayectoria_1(q1[i])
        sleep(0.1)
        trayectoria_2(q3[i])
        sleep(0.1)
        trayectoria_3(q4[i])
        sleep(0.1)
        print(f'Paso{i+1}: q1: {q1[i]}, q2: {q2[i]}, q3: {q3[i]}, q4: {q4[i]}')
        sleep(1)


# Ventana De Cinematica Directa

def abrir_control_directo():

    valores_grabados = []

    #GRabar los valores

    def grabar_valores():
        valores = [slider_q1.get(), slider_q2.get(), slider_q3.get(), slider_q4.get()]
        valores_grabados.append(valores)
        print(f"Valores grabados: {valores}")

    # Borra ultimo valor grabado

    def borrar_ultimo():
        if valores_grabados:
            valores_grabados.pop()
            print("Ultimo valor borrado")
        else:
            print("No hay valores para borrar")

    # Muestra valores

    def mostrar_valores():
        if valores_grabados:
            messagebox.showinfo("Valores Grabados", f"{valores_grabados}")
        else:
            messagebox.showinfo("Valores Grabados", "No hay valores grabados")

    # Borra todo

    def reset_valores():
        valores_grabados.clear()
        print("Todos los valores han sido reseteados")

    # Ejecuta la trayectoria

    def ejecutar_funciones():
        i = 0
        for valores in valores_grabados:
            trayectoria_1(valores[0])
            sleep(0.1)
            trayectoria_2(valores[2])
            sleep(0.1)
            trayectoria_3(valores[3])
            sleep(0.1)
            print(f'Paso{i+1}')
            i += 1
            sleep(0.5)


    # Crear nueva ventana
    control_window = tk.Toplevel(root)
    control_window.title("Control Directo de Manipulador")
    control_window.geometry("400x350")

    # Titulos
    title = tk.Label(
        control_window, 
        text="Control de Trayectoria", 
        font=("Helvica", 16, "bold")
    )
    title.pack(pady=5)

    subtitle = tk.Label(
        control_window, 
        text="Universidad Nacional de Trujillo", 
        font=("Helvica", 14))
    subtitle.pack(pady=5)

    # Crear los deslizadores y etiquetas
    frame_sliders = tk.Frame(control_window)
    frame_sliders.pack(pady=5)

    # Slider q1
    label_q1 = tk.Label(frame_sliders, text="q1")
    label_q1.grid(row=0, column=0, padx=5, pady=5)

    slider_q1 = tk.Scale(
        frame_sliders, 
        from_=0, to=180, 
        orient=tk.HORIZONTAL, 
        command=update_servo1
    )
    slider_q1.grid(row=0, column=1, padx=5, pady=5)
    value_q1 = tk.Label(frame_sliders, text="0Â°")
    value_q1.grid(row=0, column=2, padx=5, pady=5)

    # Slider q2
    label_q2 = tk.Label(frame_sliders, text="q2")
    label_q2.grid(row=1, column=0, padx=5, pady=5)
    slider_q2 = tk.Scale(frame_sliders, from_=0, to=0, orient=tk.HORIZONTAL, command=funcion_q2)
    slider_q2.grid(row=1, column=1, padx=5, pady=5)
    value_q2 = tk.Label(frame_sliders, text="0Â°")
    value_q2.grid(row=1, column=2, padx=5, pady=5)
    slider_q2.configure(command=lambda value: [funcion_q2(value), value_q2.config(text=f"{value}°")])

    # Slider q3
    label_q3 = tk.Label(frame_sliders, text="q3")
    label_q3.grid(row=2, column=0, padx=5, pady=5)
    slider_q3 = tk.Scale(
        frame_sliders, 
        from_=0, to=180, 
        orient=tk.HORIZONTAL, 
        command=update_servo2
    )
    slider_q3.grid(row=2, column=1, padx=5, pady=10)
    value_q3 = tk.Label(frame_sliders, text="0Â°")
    value_q3.grid(row=2, column=2, padx=5, pady=5)


    # Slider q4
    label_q4 = tk.Label(frame_sliders, text="q4")
    label_q4.grid(row=3, column=0, padx=5, pady=5)
    slider_q4 = tk.Scale(
        frame_sliders, 
        from_=0, to=180, 
        orient=tk.HORIZONTAL, 
        command=update_servo3
    )
    slider_q4.grid(row=3, column=1, padx=5, pady=5)
    value_q4 = tk.Label(frame_sliders, text="0Â°")
    value_q4.grid(row=3, column=2, padx=5, pady=5)

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


# Crear la ventana principal
root = tk.Tk()
root.title("Manipulacion de Posicion Final")
root.geometry("400x300")

# Titulo
title = tk.Label(root, text="Manipulacion de Posicion Final", font=("Helvica", 16, "bold"))
title.pack(pady=10)
subtitle = tk.Label(root, text="Universidad Nacional de Trujillo", font=("Helvica", 14))
subtitle.pack(pady=5)

# Frame para centrar los elementos
frame = tk.Frame(root)
frame.pack(pady=10)

# entries = []

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

# Boton OK
ok_button = tk.Button(
    button_frame, text="OK", 
    command=cinematica_inversa
)
ok_button.pack(side="left", padx=10)

# Boton para abrir Control Directo
control_directo_button = tk.Button(
    root, 
    text="Abrir Control Directo", 
    command=abrir_control_directo
)
control_directo_button.pack(pady=10)

# Boton para abrir Control por Trayectoria

road_frame = tk.Frame(root)
road_frame.pack(pady=10)

load_button = tk.Button(
    road_frame, 
    text="Cargar CSV para Trayecorias", 
    command=process_csv
)
load_button.pack(pady=10)

execute_button = tk.Button(
    road_frame, 
    text="Ejecutar Trayectorias", 
    command=cinematica_inversa_modificada
)

root.mainloop()
