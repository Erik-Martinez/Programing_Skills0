

import csv
import os


# prepare data
def data_from_file(filename):
    """
    Extracts the exchanges rates from the csv file.
    Args:
        filename (string): path to the CSV file

    Returns:
        clp, ars, usd, eur, try_money, gbp (list of floats)
    """
    clp = []
    ars = []
    usd = []
    eur = []
    try_money =[]
    gbp = []
    with open(filename) as file:
        csvreader = csv.reader(file, delimiter=';')
        for item in csvreader:
            clp.append(item[1])
            ars.append(item[2])
            usd.append(item[3])
            eur.append(item[4])
            try_money.append(item[5])
            gbp.append(item[6])
        clp.pop(0)
        ars.pop(0)
        usd.pop(0)
        eur.pop(0)
        try_money.pop(0)
        gbp.pop(0)

        clp = [float(i.replace(',', '.')) for i in clp]
        ars = [float(i.replace(',', '.')) for i in ars]
        usd = [float(i.replace(',', '.')) for i in usd]
        eur = [float(i.replace(',', '.')) for i in eur]
        try_money = [float(i.replace(',', '.')) for i in try_money]
        gbp = [float(i.replace(',', '.')) for i in gbp]


    return clp, ars, usd, eur, try_money, gbp

def currency_converter(currency, exchange, valor):
    """
    Currency converter

    Arg:
        currency ("CLP", "ARS", "USD", "EUR", "TRY", "GBP"): type of currency of the client
        exchange ("CLP", "ARS", "USD", "EUR", "TRY", "GBP"): type of currency the client want to convert to
        valor (float): amount of money to exchange
    Returns:
        exchange_valor
    """

    clp, ars, usd, eur, try_money, gbp = data_from_file("Data/exchangeRate_03012024.csv")

    currency = currency.upper()
    exchange = exchange.upper()

    if currency == 'CLP':
        if exchange == 'CLP':
            print('Conversion no posible.')
        elif exchange == 'ARS':
            type_exchange = ars[0]
        elif exchange == 'USD':
            type_exchange = usd[0]
        elif exchange == "EUR":
            type_exchange = eur[0]
        elif exchange == 'TRY':
            type_exchange = try_money[0]
        elif exchange == 'GBP':
            type_exchange = gbp[0]
        else:
            print("Error en la seleción de la divisa de intercambio.")

    elif currency == "ARS":
        if exchange == 'CLP':
            type_exchange = clp[1]
        elif exchange == 'ARS':
            print('Conversion no posible.')
        elif exchange == 'USD':
            type_exchange = usd[1]
        elif exchange == "EUR":
            type_exchange = eur[1]
        elif exchange == 'TRY':
            type_exchange = try_money[1]
        elif exchange == 'GBP':
            type_exchange = gbp[1]
        else:
            print("Error en la seleción de la divisa de intercambio.")

    elif currency == 'USD':
        if exchange == 'CLP':
            type_exchange = clp[2]
        elif exchange == 'ARS':
            type_exchange = ars[2]
        elif exchange == 'USD':
            print('Conversion no posible.')
        elif exchange == "EUR":
            type_exchange = eur[2]
        elif exchange == 'TRY':
            type_exchange = try_money[2]
        elif exchange == 'GBP':
            type_exchange = gbp[2]
        else:
            print("Error en la seleción de la divisa de intercambio.")

    elif currency == 'EUR':
        if exchange == 'CLP':
            type_exchange = clp[3]
        elif exchange == 'ARS':
            type_exchange = clp[3]
        elif exchange == 'USD':
            type_exchange = usd[3]
        elif exchange == "EUR":
            print('Conversion no posible.')
        elif exchange == 'TRY':
            type_exchange = try_money[3]
        elif exchange == 'GBP':
            type_exchange = gbp[3]
        else:
            print("Error en la seleción de la divisa de intercambio.")

    elif currency == 'TRY':
        if exchange == 'CLP':
            type_exchange = clp[4]
        elif exchange == 'ARS':
            type_exchange = ars[4]
        elif exchange == 'USD':
            type_exchange = usd[4]
        elif exchange == "EUR":
            type_exchange = eur[4]
        elif exchange == 'TRY':
            print('Conversion no posible.')
        elif exchange == 'GBP':
            type_exchange = gbp[4]
        else:
            print("Error en la seleción de la divisa de intercambio.")

    elif currency == 'GBP':
        if exchange == 'CLP':
            type_exchange = clp[5]
        elif exchange == 'ARS':
            type_exchange = ars[5]
        elif exchange == 'USD':
            type_exchange = usd[5]
        elif exchange == "EUR":
            type_exchange = eur[5]
        elif exchange == 'TRY':
            type_exchange = try_money[5]
        elif exchange == 'GBP':
            print('Conversion no posible.')
        else:
            print("Error en la seleción de la divisa de intercambio.")

    else:
        print('Error en la seleción de la divisa a intercambiar.')



    exchange_valor = round(float(valor) * type_exchange, 5)
    commission = exchange_valor * 0.01
    new_currency = exchange


    return exchange_valor, commission, new_currency



def initial_questions():
    print("###################### NUEVA OPERACIÓN ######################")
    print("-------------------------------------------------------------")
    currency = input("Tipo de divisa a intercarbiar (CLP, ARS, USD, EUR, TRY, GBP): ")
    exchange = input("Tipo de divisa de intercambio (CLP, ARS, USD, EUR, TRY, GBP): ")
    valor = input("Valor: ")

    return currency, exchange, valor


on = True

while on == True:

    try:
        currency, exchange, valor = initial_questions()
        valor_usd, commision, new_currency = currency_converter(currency, "USD", valor)


        if valor_usd > 10000 and valor_usd > 3:
            os.system("cls")
            print("\n \n-------------------------------------------------------------")
            print(f"Si la operación ha realizar tiene un valor al cambio que supera \nlos 10000 USD o es inferior a "
                  f"los 2 USD no podemos realizarla. \n"
                  f"Tu operación acutal: {valor} {currency} -> {valor_usd} USD.")
            print("------------------------------------------------------------- \n")

        else:
            exchange_valor, commision, new_currency = currency_converter(currency, exchange, valor)
            os.system("cls")

            print(f"Intercambio: {currency} -> {new_currency}\n"
                  f"El valor de intercambio es {exchange_valor}\n"
                  f"En caso de querer hacer el intercambio hay una comision de {commision} {new_currency}, "
                  f"un 1% en la nueva divisa.")

            complet = True

            while complet == True:
                decision = input("Quieres completar la operación? (Si/No)\n")

                decision = decision.upper()

                if decision == "SI" or decision == "S":
                    print(f"Se ha realizado el cambio de divisa. Tus fondos estan ahora en {new_currency}")
                    complet = False
                elif decision == "NO" or decision == "N":
                    complet = False
                else:
                    os.system("cls")
                    print("No entiendo tu respuesta.")

            more_operations = True
            while more_operations == True:
                os.system("cls")
                decision = input("Quieres hacer más operaciones? (Si/No) \n")

                decision = decision.upper()

                if decision == "SI" or decision == "S":
                    break
                elif decision == "NO" or decision == "N":
                    more_operations = False
                    on = False
                else:
                    print("No entiendo tu respuesta.")

    except:
        continue





