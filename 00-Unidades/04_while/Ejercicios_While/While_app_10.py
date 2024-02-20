import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        contador_iteraciones = 0
        suma_acumulada_positivos = 0
        suma_acumulada_negativos = 0
        contador_positivos = 0
        contador_negativos = 0
        contador_ceros = 0
        while True:
            numeros = prompt("Utn", "Ingrese un numero")
            if numeros == None:
                break
            numeros = int(numeros)
            if numeros > 0:
                suma_acumulada_positivos += numeros
                contador_positivos += 1
            if numeros < 0:
                suma_acumulada_negativos += numeros
                contador_negativos += 1
            if numeros == 0:
                contador_ceros += 1
            suma_acumulada_total = suma_acumulada_negativos + suma_acumulada_positivos
            contador_iteraciones += 1
        mensaje = "La suma acumulada de los positivos es: {0} \n La suma acumulada de los negativos es: {1} \n La cantidad de números positivos ingresados es: {2} \n La cantidad de números negativos ingresados es: {3} \n La cantidad de veces que se ingresó el cero fue: {4} \n La suma acumulada total es: {5}".format(suma_acumulada_positivos,suma_acumulada_negativos,contador_positivos,contador_negativos,contador_ceros,suma_acumulada_total)
        alert("Utn", mensaje)
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
