import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Se nos ha solicitado desarrollar una aplicación para llevar registro de las entradas vendidas en el Estadio River 
Plate, para el concierto de Taylor Swift. Para ello, se solicitará al usuario la siguiente información al momento de 
comprar cada entrada:

Al presionar el boton se debera pedir la carga de los siguientes datos, hasta que el usuario lo desee:

Los datos que deberas pedir para los ventas son:
    * Nombre del comprador
    * Edad (no menor a 16)
    * Género (Masculino, Femenino, Otro)
    * Tipo de entrada (General, Campo delantero, Platea)
    * Medio de pago (Crédito, Efectivo, Débito) 
    * Precio de la entrada (Se debe calcular)

Para cada venta, se calculará el total a pagar en función del tipo de entrada elegida, 
el medio de pago y su precio correspondiente.

 * Lista de precios: 
        * General: $16000
        * Campo:   $25000
        * Platea:  $30000

Las entradas adquiridas con tarjeta de crédito tendrán un 20% de descuento sobre el 
precio de la entrada, mientras que las adquiridas con tarjeta de débito un 15%. 

Al finalizar la carga, el programa debera mostrar los siguientes informes:

    #!X 1) - Determina el género más frecuente entre las personas que compraron entradas de tipo "Campo".
    #!X 2) - Determina cuántas personas compraron entradas de tipo "General" pagando con tarjeta 
    #!          de crédito y su edad promedio.
    #!X 3) - Calcula el porcentaje de personas que compraron entradas de tipo "Platea" y 
    #!          pagaron con tarjetab de déito  respecto al total de personas en la lista.
    #!X 4) - Cuál es el total de descuentos en pesos que aplicó la empresa, pero solo de 
    #!          los aplicados a tarjetas de crédito
    #! 5) - El nombre y la edad de la persona que pagó el precio más alto por una entrada de 
    #!          tipo "General" y pagó con tarjeta de débito (Solo la primera que se encuentre)
    #! 6) - La cantidad de personas que compraron entradas de tipo "Platea" y cuya 
    #!          edad es un número primo.
    #! 7) - Calcula el monto total recaudado por la venta de entradas de tipo "Platea" y 
    #!          pagadas con tarjeta de debito por personas cuyas edades son múltiplos de 6.
'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        ''' '''
        seguir = True
        precio_entrada = 0
        contador_campo = 0
        contador_masculino = 0
        contador_femenino = 0
        contador_otro = 0
        contador_general_credito = 0
        acumulador_edad_general = 0
        contador_personas_total = 0
        contador_platea_debito = 0
        acumulador_descuento_credito = 0
        while seguir == True:
            nombre = input("Ingrese su nombre: ")
            edad = input("Ingrese su edad: ")
            edad = int(edad)
            while edad < 16:
                edad = input("Ingrese su edad: ")
                edad = int(edad)
            genero = input("Ingrese su genero (Masculino, Femenino, Otro): ")
            while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
                genero = input("Ingrese un genero valido (Masculino, Femenino, Otro): ")
            tipo_entrada = input("Elija el tipo de entrada (General, Campo delantero, Platea): ")
            while tipo_entrada != "General" and tipo_entrada != "Campo delantero" and tipo_entrada != "Platea":
                tipo_entrada = input("Elija un tipo de entrada valida (General, Campo delantero, Platea): ")
            medio_pago = input("Elija el metodo de pago (Credito, Efectivo, Debito): ")
            while medio_pago != "Credito" and medio_pago != "Efectivo" and medio_pago != "Debito":
                medio_pago = input("Elija un metodo de pago valido (Credito, Efectivo, Debito): ")
            contador_personas_total += 1
            match genero:
                case "Masculino":
                    contador_masculino += 1
                case "Femenino":
                    contador_femenino += 1
                case "Otro":
                    contador_otro += 1
            match tipo_entrada:
                case "General":
                    precio_entrada = 16000
                    if medio_pago == "Credito":
                        contador_general_credito += 1
                        acumulador_edad_general += edad
                case "Campo delantero":
                    contador_campo += 1
                    precio_entrada = 25000
                    if contador_masculino > contador_femenino and contador_masculino > contador_otro:
                        genero_maximo_campo = print("El genero más frecuente en las entradas Campo delantero fue Masculino")
                    elif contador_otro > contador_femenino:
                        genero_maximo_campo = print("El genero más frecuente en las entradas Campo delantero fue Otro")
                    else:
                        genero_maximo_campo = print("El genero más frecuente en las entradas Campo delantero fue Femenino")
                case "Platea":
                    precio_entrada = 30000
                    if medio_pago == "Debito":
                        contador_platea_debito += 1
            match medio_pago:
                case "Credito":
                    descuento_total_credito = precio_entrada * 0.2
                    precio_entrada = precio_entrada * 0.8
                    acumulador_descuento_credito += descuento_total_credito
                case "Debito":
                    precio_entrada = precio_entrada * 0.75
            print(f"El precio de la entrada es: {precio_entrada}")
            seguir = question("Pregunta","Desea continuar?")
        if contador_general_credito > 0:
            promedio_edad_general_credito = acumulador_edad_general / contador_general_credito
        print(f"La cantidad de personas que compraron General con Tarjeta de credito fueron: {contador_general_credito} y el promedio de edad es: {promedio_edad_general_credito}")
        porcentaje_platea_debito = contador_platea_debito * 100 / contador_personas_total
        print(f"El porcentaje de personas que compraron Platea con Tarjeta de debito sobre el total de personas en lista es {porcentaje_platea_debito}")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()