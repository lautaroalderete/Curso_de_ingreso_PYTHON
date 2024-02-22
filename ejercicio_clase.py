import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nos encargan el desarrollo de una aplicación que le permita a sus usuarios operar en la bolsa de 
valores:

Para ello deberás programar el botón  para poder cargar 10 operaciones de compra con los siguientes datos:
    * Nombre
    * Monto en pesos de la operación (no menor a $10000)
    * Tipo de instrumento(CEDEAR, BONOS, MEP) 
    * Cantidad de instrumentos  (no menos de cero) 
    
Realizar los siguientes informes:

    #!X 1) - Tipo de instrumento que menos se operó en total.
    #!X 2) - Cantidad de usuarios que compraron entre 50  y 200 MEP 
    #!X 3) - Cantidad de usuarios que no compraron CEDEAR 
    #!X 4) - Nombre y cantidad invertida del primer usuario que compró BONOS o CEDEAR
    #! 5) - Nombre y posicion del usuario que invirtio menos dinero
    #!X 6) - Promedio de dinero en CEDEAR  ingresado en total.  
    #!X 7) - Promedio de cantidad de instrumentos  MEP vendidos en total

'''
class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        contador = 0
        contador_cedear = 0
        contador_bonos = 0
        contador_mep = 0
        contador_usuarios_mep = 0
        contador_no_cedear = 0
        monto = 0
        acumulador_monto_cedear = 0
        acumulador_cantidad_mep = 0
        bandera_primer_cedear_bonos = False
        minimo_dinero = 0
        bandera_minimo_dinero = False
        while contador < 3:
            nombre = input("Ingrese su nombre: ")
            monto_operacion = input("Ingrese su monto: ")
            monto_operacion = int(monto_operacion)
            while monto_operacion < 10000:
                monto_operacion = input("Reingrese su monto (Minimo $10000): ")
                monto_operacion = int(monto_operacion)
            tipo_instrumento = input("Ingrese el tipo de instrumento (CEDEAR, BONOS O MEP): ")
            while tipo_instrumento != "CEDEAR" and tipo_instrumento != "BONOS" and tipo_instrumento != "MEP":
                tipo_instrumento = input("Reingrese el tipo de instrumento (CEDEAR, BONOS O MEP): ")
            cantidad_instrumentos = input("Ingrese la cantidad de instrumentos: ")
            cantidad_instrumentos = int(cantidad_instrumentos)
            while cantidad_instrumentos < 0:
                cantidad_instrumentos = input("Reingrese la cantidad de instrumentos: ")
                cantidad_instrumentos = int(cantidad_instrumentos)
            match tipo_instrumento:
                case "BONOS":
                    contador_bonos += 1
                case "CEDEAR":
                    contador_cedear += 1
                    acumulador_monto_cedear += monto_operacion
                case "MEP":
                    contador_mep += 1
                    acumulador_cantidad_mep += cantidad_instrumentos
            #! 2) - Cantidad de usuarios que compraron entre 50  y 200 MEP
                    if cantidad_instrumentos > 50 and cantidad_instrumentos < 200:
                        contador_usuarios_mep += 1
            #! 3) - Cantidad de usuarios que no compraron CEDEAR
            if tipo_instrumento != "CEDEAR":
                contador_no_cedear += 1
            #! 4) - Nombre y cantidad invertida del primer usuario que compró BONOS o CEDEAR
            if bandera_primer_cedear_bonos == False or (tipo_instrumento == "CEDEAR" or tipo_instrumento == "BONOS"):
                primer_nombre = nombre
                monto = monto_operacion
                bandera_primer_cedear_bonos = True
            #! 5) - Nombre y posicion del usuario que invirtio menos dinero
            if bandera_minimo_dinero == False or minimo_dinero > monto_operacion:
                minimo_dinero = monto_operacion
                nombre_minimo = nombre
                bandera_minimo_dinero = True
            contador += 1
        #! 1) - Tipo de instrumento que menos se operó en total.
        if contador_bonos < contador_cedear and contador_bonos < contador_mep:
            print("BONOS fue el tipo que menos se operó")
        elif contador_cedear < contador_mep:
            print("CEDEAR fue el tipo que menos se operó")
        else:
            print("MEP fue el tipo que menos se operó")
        #! 6) - Promedio de dinero en CEDEAR  ingresado en total.
        promedio_monto_cedear = acumulador_monto_cedear / contador_cedear
        #! 7) - Promedio de cantidad de instrumentos  MEP vendidos en total
        promedio_cantidad_mep = acumulador_cantidad_mep / contador_mep
        print(f"La cantidad de usuarios que compraron MEP entre 50 y 200 fue: {contador_usuarios_mep}")
        print(f"La cantidad de usuarios que no compraron CEDEAR es: {contador_no_cedear}")
        print(f"El nombre del primer usuario que compró BONOS o CEDEAR fue {primer_nombre} y la cantidad invertida es {monto}")
        print(f"El promedio de dinero en CEDEAR es {promedio_monto_cedear}")
        print(f"El Nombre del usuario que invirtió menos dinero fue: {nombre_minimo} con una inversión de {minimo_dinero}")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()