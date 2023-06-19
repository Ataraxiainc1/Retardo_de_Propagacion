# -*- coding: latin-1 -*-
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import matplotlib.pyplot as plt

def generar_imagen_formula():
    # Definir la fórmula en TEX
    formula_tex = r"$T_d = \frac{d}{v}$"

    # Configurar Matplotlib para renderizar texto en TEX
    plt.rcParams["text.usetex"] = True

    # Crear la figura y el eje
    fig, ax = plt.subplots(figsize=(4, 2.5))

    # Renderizar la fórmula en el eje
    ax.text(0.5, 0.35, formula_tex, fontsize=18, ha="center", va="center")

    # Eliminar los ejes
    ax.axis("off")

    # Guardar la figura como imagen
    fig.savefig("formula_temp.png", dpi=300, bbox_inches="tight", pad_inches=0)

    # Cerrar la figura
    plt.close(fig)

    # Abrir la imagen guardada
    image = Image.open("formula_temp.png")

    # Recortar la imagen con un margen adicional
    left = 300
    top = 320
    right = image.width - 300
    bottom = image.height - 150
    cropped_image = image.crop((left, top, right, bottom))

    # Guardar la imagen recortada
    cropped_image.save("formula.png")


# Crear la ventana principal
window = tk.Tk()
window.title("Calculadora de Retardo de Propagación")
window.configure(bg='black')

# Configurar estilo temático para el modo oscuro
style = ttk.Style()
style.theme_use('clam')
style.configure('.', foreground='light green', background='black', font=('Arial', 14, 'bold'), fieldbackground='black')
style.configure('Resultado.TLabel', foreground='orange')

# Agregar un resumen de la fórmula
resumen_formula = "El retardo de propagación (Td) se calcula mediante la fórmula: \n\nTd = d / v\n\nDonde:\n- d es la distancia\n- v es la velocidad de propagación\n\nEl retardo de propagación es una medida del tiempo que tarda una señal en propagarse a través de un medio de transmisión."
label_resumen = ttk.Label(window, text=resumen_formula, justify="left", font=('Arial', 16, 'bold'))
label_resumen.grid(row=0, column=0, padx=10, pady=5)

# Generar la imagen de la fórmula
generar_imagen_formula()

# Cargar la imagen de la fórmula recortada
formula_image = Image.open("formula.png")
formula_photo = ImageTk.PhotoImage(formula_image)

# Mostrar la imagen de la fórmula en la interfaz gráfica
label_formula = ttk.Label(window, image=formula_photo)
label_formula.grid(row=1, column=0, padx=10, pady=5)

def calcular_retardo():
    distancia = float(entry_distancia.get())  # Get the distance value from the entry field
    velocidad = float(entry_velocidad.get())  # Get the velocity value from the entry field
    
    retardo = distancia / velocidad  # Calculate the propagation delay
    
    label_resultado.configure(text="Retardo de Propagación: {:.2f}".format(retardo))


# Crear los elementos de la interfaz
label_distancia = ttk.Label(window, text="Distancia (d):", font=('Arial', 16, 'bold'))
entry_distancia = ttk.Entry(window, font=('Arial', 16))
label_unidad_distancia = ttk.Label(window, text="(metros)", font=('Arial', 12))
label_velocidad = ttk.Label(window, text="Velocidad de Propagación (v):", font=('Arial', 16, 'bold'))
entry_velocidad = ttk.Entry(window, font=('Arial', 16))
label_unidad_velocidad = ttk.Label(window, text="(m/s)", font=('Arial', 12))
btn_calcular = tk.Button(window, text="Calcular", command=calcular_retardo, font=('Arial', 16, 'bold'))
label_resultado = ttk.Label(window, text="Retardo de Propagación: ", font=('Arial', 16, 'italic'), style='Resultado.TLabel')
label_unidad_resultado = ttk.Label(window, text="(segundos)", font=('Arial', 12))

# Posicionar los elementos en la ventana
label_distancia.grid(row=2, column=0, padx=16, pady=5)
entry_distancia.grid(row=2, column=1, padx=10, pady=5)
label_unidad_distancia.grid(row=2, column=2, padx=5)
label_velocidad.grid(row=3, column=0, padx=10, pady=5)
entry_velocidad.grid(row=3, column=1, padx=10, pady=5)
label_unidad_velocidad.grid(row=3, column=2, padx=5)
btn_calcular.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
label_resultado.grid(row=5, column=0, columnspan=2, padx=10, pady=5)
label_unidad_resultado.grid(row=5, column=2, padx=5)

# Ejecutar la ventana
window.mainloop()