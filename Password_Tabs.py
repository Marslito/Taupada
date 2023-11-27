import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
import password_Generator as PG
import datetime as dt

def current_date():
    current_date = dt.date.today()
    # Extract the year and month from the current date
    year = current_date.year
    month = current_date.strftime('%m')
    # Create the formatted string
    formatted_date = f"{year}{month}"
    return formatted_date

# Define a function to show the error message
def error_pass():
   ttk.messagebox.showerror('Python Error', 'Error: This is an Error Message!')

def mostrar_pestaña2():
    if pass_entry.get() == PG.generar_pass(current_date()):
        my_notebook.tab(1, state="normal")
        my_notebook.select(1)
    else:
        tk.messagebox.showerror("Error", "Contraseña incorrecta. Inténtalo de nuevo.")
        my_notebook.tab(1, state="hidden")



# Crear una ventana
ventana = tk.Tk()
ventana.title("Pestañas con Contraseña")
ventana.geometry("800x600")

# Crear un objeto Notebook (cuaderno) para las pestañas
my_notebook = ttk.Notebook(ventana)

# Crear pestañas
pestaña1 = tk.Frame(my_notebook)
pestaña2 = tk.Frame(my_notebook)

# Agregar contenido a la pestaña 1
pass_label = tk.Label(pestaña1, text="Ingresa la contraseña:")
pass_label.pack(padx=20, pady=20)

pass_entry = ttk.Entry(pestaña1, show="*")
pass_entry.pack(padx=20, pady=20)

boton_mostrar = tk.Button(pestaña1, text="Comprobar Contraseña", command=mostrar_pestaña2)
boton_mostrar.pack(padx=20, pady=20)

# Agregar contenido a la pestaña 2
contenido_pestaña2 = tk.Label(pestaña2, text="Contenido de la Pestaña 2")
contenido_pestaña2.pack(padx=20, pady=20)

# Agregar las pestañas al cuaderno
my_notebook.add(pestaña1, text="Acceso")
my_notebook.add(pestaña2, text="Programa")

# Ocultar la pestaña 2 inicialmente
my_notebook.tab(1, state="hidden")

# Empacar el cuaderno
my_notebook.pack(fill="both", expand=True)

# Iniciar la aplicación
ventana.mainloop()
