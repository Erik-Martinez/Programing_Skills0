
import os
import random
import time
import csv
import pandas as pd

data = pd.read_csv("Data/data_shiptments.csv", sep=";", encoding='utf-8')

def log_in_funtion():

    num_attempts = 0

    while num_attempts < 3:

        os.system("cls")
        print("------------------------------------------------\n"
              "############ Envios Caparazon Azul #############\n"
              "------------------------------------------------")
        print("Introduzca los datos para entrar en su cuenta.")
        print("(modo test - Usuario: Mario / Contraseña: Mario)")

        user = input("Usuario: ")
        password = input("Contraseña: ")

        with open("Data/login.csv", encoding="utf-8-sig") as file:
            csvreader = csv.DictReader(file, delimiter=';')
            for row in csvreader:
                if row['user'].lower() == user.lower():
                    if row['password'] == password:
                        return
            num_attempts += 1
            os.system("cls")
            print(f"!!! Alguno de los datos no es correcto. Te quedan {3 - num_attempts} intentos !!!\n")
            input("Pulsa enter para continuar.")

    print("Has superado el número de intentos maximos.")
    exit()

def informartion_shipment(data):
    os.system("cls")
    print("Necesitamos que conteste a la siguientes preguntas para poder realizar el envio.\n"
          "                               Cargando ...")
    time.sleep(3)
    os.system("cls")
    print("@@@@@@@@@@@ Información del remitente @@@@@@@@@@@")
    nameComplete_sender = input("Nombre y apellidos:")
    country_sender= input("En que país te encuentras:")
    print("\n@@@@@@@@@@@ Información del destinatario @@@@@@@@@@@")
    nameComplete_recipient = input("Nombre y appellidos: ")
    country_recipient = input("País de destino: ")
    cp_recipient = input("Codigo Postal: ")
    address_recipient = input("Direción de envio:")

    while True:
        number_packages = random.randint(1, 100000)
        if number_packages not in data.loc[:,'id_shipment']:
            break

    while True:
        os.system('cls')
        print("@@@@@@@@@@@ Información del remitente @@@@@@@@@@@")
        weight = input("Peso del paquete en kg: ")

        weight_price = float(weight) * 2

        print(f"\n\nEl precio es de 2$ por kg. Tu paquete pesa {weight}, "
              f"por tanto el precio final es de {weight_price} $.")
        answer = input("Aceptas estas condiciones (SI/NO)")

        answer = answer.lower()

        if answer == "si" or answer == "s":
            add_data = pd.DataFrame([[number_packages, nameComplete_sender, country_sender, nameComplete_recipient,
                                          country_recipient, cp_recipient, address_recipient]],
                                    columns = list(data.columns.values))
            data = pd.concat([data, add_data], ignore_index=True)

            os.system('cls')
            print("Los datos han sido correctamente introducidos")
            input("Pulsa enter para continuar.")
            return data
        elif answer == "no" or answer == "n":
            return data
        else:
            print("No entiendo tu respuesta.")
            input("Pulsa enter para continuar.")


logo = """\
    Envios Caparazon Azul
      >>>>>>>>>>>>>>>
┌─────────────────────┬────┐
│                     │    │
│                     │    │
│                     │    │
├─────────────────────┤    │
│                     │    │
│                     │    │
│                     │    │
└─────────────────────┴────┘

        Cargando ...\
"""
table_menu = """\
+---+----------------+
| 1 | Enviar paqueta |
+---+----------------+
| S | Cerrar sesion. |
+---+----------------+\
"""

print(logo)
time.sleep(3)
os.system("cls")

log_in_funtion()

while True:
    os.system("cls")
    print("------------------------------------------------\n"
          "############ Envios Caparazon Azul #############\n"
          "------------------------------------------------")
    print(table_menu, '\n')
    operation = input("Indica la operación a realizar: ")

    operation = operation.lower()

    if operation == "1":
        data = informartion_shipment(data)

    elif operation == "s":
        data.to_csv("Data/data_shiptments.csv", sep=";", encoding='utf-8')
        exit()
    else:
        os.system("cls")
        print("ERROR: Esa operación no existe.")
        input("Pulsa enter para volver al menú.")


