import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Lautaro
apellido: Alderete
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        seguir = True
        acumulador_votos = 0
        while seguir == True:
            nombre_candidato = input("Ingrese nombre del candidato: ")
            edad = input("Ingrese la edad del candidato: ")
            edad = int(edad)
            while edad <= 25:
                edad = input("Reingrese la edad del candidato: ")
                edad = int(edad)
            votos = input("Ingrese cuantos votos recibió: ")
            votos = int(edad)
            while votos < 0:
                votos = input("Reingrese cuantos votos recibió: ")
                votos = int(edad)
            acumulador_votos += votos
            seguir = question ("Pregunta", "Desea continuar?")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
