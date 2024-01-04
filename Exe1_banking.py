import csv
import os
import time


def log_in_funtion():

    num_attempts = 0

    while num_attempts < 3:

        os.system("cls")
        print("------------------------------------------------\n"
              "###### Banco Central del Reino Champiñon ######\n"
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
                        return row['id_account']
            num_attempts += 1
            os.system("cls")
            print(f"!!! Alguno de los datos no es correcto. Te quedan {3 - num_attempts} intentos !!!\n")
            input("Pulsa enter para volver a intentar.")

    print("Has superado el número de intentos maximos.")
    exit()

def read_coins(id_account):

    with open("Data/account_balance.csv", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            if row['id_account'] == id_account:
                coins_account = int(row['total_account'])
                break

    return coins_account

def deposit(id_account, my_coins):

    os.system("cls")
    print("------------------------------------------------\n"
          "###### Banco Central del Reino Champiñon ######\n"
          "------------------------------------------------")
    print("@@@@@@@@ Depositar dinero en la cuenta @@@@@@@@")
    print("------------------------------------------------")
    coins = input("Cuantas monedas te gustaria añadir a tu cuenta?\n")
    comment = input("Si quieres puedes añadir un comentario a tu transación, si no pulsa enter.\n")

    num_operation = 1

    with open("Data/tranfers.csv", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            num_operation = row['id_transfer']
        num_operation = int(num_operation) + 1

    with open("Data/tranfers.csv", "a", encoding="utf-8-sig") as file:

        fieldnames = ["id_transfer", "issuing_account", "recipient_account", "value", "comment"]
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')
        writer.writerow({'id_transfer': str(num_operation),"issuing_account": 'None', "recipient_account": id_account,
                         'value': coins, 'comment': comment})

    my_coins = int(my_coins) + int(coins)

    print("Operación completada con exito.")
    input("Pulsa enter para volver al menú.")

    return my_coins

def withdraw(id_account, my_coins):

    os.system("cls")
    print("------------------------------------------------\n"
          "###### Banco Central del Reino Champiñon ######\n"
          "------------------------------------------------")
    print("@@@@@@@@ Retirar dinero en la cuenta @@@@@@@@")
    print("------------------------------------------------")
    coins = input("Cuantas monedas te gustaria retirar de tu cuenta?\n")
    comment = input("Si quieres puedes añadir un comentario a tu transación, si no pulsa enter.\n")

    if int(coins) <= my_coins:
        num_operation = 1

        with open("Data/tranfers.csv", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                num_operation = row['id_transfer']
            num_operation = int(num_operation) + 1

        with open("Data/tranfers.csv", "a", encoding="utf-8-sig") as file:

            fieldnames = ["id_transfer", "issuing_account", "recipient_account", "value", "comment"]
            writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')

            writer.writerow(
                {'id_transfer': str(num_operation), "issuing_account":  id_account, "recipient_account": 'None' ,
                 'value': coins, 'comment': comment})

        my_coins = int(my_coins) - int(coins)

        print("Operación completada con exito.")
        input("Pulsa enter para volver al menú.")

        return my_coins
    else:
        print("La operación no es posible por falta de saldo.")
        input("Pulsa enter para volver al menú.")
        return my_coins

def transfer_coins(id_account, my_coins):
    os.system("cls")
    print("------------------------------------------------\n"
          "###### Banco Central del Reino Champiñon ######\n"
          "------------------------------------------------")
    print("@@@@@@@@ Transferencia a otras cuentas @@@@@@@@")
    print("------------------------------------------------")
    coins = input("Cuantas monedas te gustaria enviar?\n")
    addres = input("Indica el id de la cuenta destinataria(ej: b3):")
    comment = input("Si quieres puedes añadir un comentario a tu transación, si no pulsa enter.\n")

    if int(coins) <= my_coins:
        num_operation = 1

        with open("Data/tranfers.csv", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                num_operation = row['id_transfer']
            num_operation = int(num_operation) + 1

        with open("Data/tranfers.csv", "a", encoding="utf-8-sig") as file:

            fieldnames = ["id_transfer", "issuing_account", "recipient_account", "value", "comment"]
            writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')

            writer.writerow(
                {'id_transfer': str(num_operation), "issuing_account":  id_account, "recipient_account": addres,
                 'value': coins, 'comment': comment})

        my_coins = int(my_coins) - int(coins)

        print("Operación completada con exito.")
        input("Pulsa enter para volver al menú.")


        return my_coins
    else:
        print("La operación no es posible por falta de saldo.")
        input("Pulsa enter para volver al menú.")
        return my_coins


def view_account(my_coins):
    os.system("cls")
    print("------------------------------------------------\n"
          "###### Banco Central del Reino Champiñon ######\n"
          "------------------------------------------------")
    print("@@@@@@@@ Revision de saldo se la cuenta @@@@@@@@")
    print("------------------------------------------------")
    print(f"Tu saldo actual es de {my_coins} monedas.")
    life = int(my_coins / 100)
    if life >= 1:
        print(f"{life} vidas extras.")

    input("Pulsa enter para volver al menú.")

inicio = """\
       ┌─────────────┐
       └┼───────────┼┘
        │           │
        │           │
        │           │
        │           │
        │           │
        │           │
        │           │
        │           │
        ├───────────┤
────────┴───────────┴─────────
   Banco del Reino Champiñon

      Cargando ...\
"""
despedida = """\
       ┌─────────────┐
       └┼───────────┼┘
        │           │
        │           │
        │           │
        │           │
        │           │
        │           │
        │           │
        │           │
        ├───────────┤
────────┴───────────┴─────────
   Banco del Reino Champiñon
   
    Esperamos verte pronto!\
"""

table_menu = """\
+---+------------------------------+
| 1 | Revisar saldo de cuenta.     |
+---+------------------------------+
| 2 | Depositar monedas.           |
+---+------------------------------+
| 3 | Retirar monedas.             |
+---+------------------------------+
| 4 | Tranferencias entre cuentas. |
+---+------------------------------+
| S | Cerrar sesion.               |
+---+------------------------------+\
"""
print(inicio)
time.sleep(3)
os.system("cls")


id_account = log_in_funtion()

my_coins = read_coins(id_account)

log_out = False

while log_out == False:

    os.system("cls")
    print("------------------------------------------------\n"
          "###### Banco Central del Reino Champiñon ######\n"
          "------------------------------------------------")
    print(table_menu, '\n')
    operation = input("Indica la operación a realizar: ")

    operation = operation.lower()

    if operation == "1":
        view_account(my_coins)
    elif operation == "2":
        my_coins = deposit(id_account, my_coins)
    elif operation == "3":
        my_coins = withdraw(id_account, my_coins)
    elif operation == "4":
        my_coins = transfer_coins(id_account, my_coins)
    elif operation == "s":
        os.system("cls")
        print(despedida)
        time.sleep(3)
        exit()
    else:
        os.system("cls")
        print("ERROR: Esa operación no existe.")
        input("Pulsa enter para volver al menú.")

