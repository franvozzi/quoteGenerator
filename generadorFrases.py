import requests
import tkinter as tk

def obtener_cita_aleatoria():
    url = "https://api.quotable.io/random"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            cita = data["content"]
            autor = data["author"]
            return f'"{cita}"\n- {autor}'
        else:
            return "No se pudo obtener una cita en este momento."
    except Exception as e:
        return str(e)

def mostrar_cita():
    cita = obtener_cita_aleatoria()
    label_cita.config(text=cita)

# Crear la ventana de la aplicación
ventana = tk.Tk()
ventana.title("Generador de Citas")

# Crear un botón para obtener una cita
boton_obtener_cita = tk.Button(ventana, text="Obtener Cita Aleatoria", command=mostrar_cita)
boton_obtener_cita.pack(pady=10)

# Crear una etiqueta para mostrar la cita
label_cita = tk.Label(ventana, text="", wraplength=300)
label_cita.pack()

# Inicializar la ventana de la aplicación
ventana.mainloop()
