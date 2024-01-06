import os
import random
import time
import  pandas as pd
import warnings

# Ignorar FutureWarning
warnings.simplefilter(action='ignore', category=FutureWarning)

def total_income():
    income = input("Añade tu salario para analizar tu salud financiera: ")
    income = float(income)
    return income

def add_expenses(df):
    menu_expense = """\
            +---+----------------+
            | 1 | Gastos medicos |
            +---+----------------+
            | 2 | Gastos de casa |
            +---+----------------+
            | 3 | Ocio           |
            +---+----------------+
            | 4 | Educación      |
            +---+----------------+
            | 5 | Ahorros        |
            +---+----------------+
            | S | Volver al menú |
            +---+----------------+\
                        """

    while True:
        os.system("cls")
        print("############## Añadir gastos ###############")
        print(menu_expense)
        type_expense = input("Seleciona el tipo de gasto: ")
        type_expense = type_expense.lower()

        if type_expense == "s":
            return df
        elif type_expense in ["1", "2", "3", "4", "5"]:
            expense_money = input("Gasto: ")
            expense_money = float(expense_money)
            new_expense = pd.DataFrame([[type_expense, expense_money]],
                                         columns = list(df.columns.values))
            print(new_expense)
            df = pd.concat([df, new_expense], ignore_index=True)
            print(df)
        else:
            print("No te he entendido.")
            input("Pulsa enter para continuar.")

def analyze_financial(income, df, dic_expense):
    os.system("cls")
    total_expense = df['expenses'].sum()
    expense_grouped = df.groupby(by='type_expense')

    print("########### Resumen de gastos ########### ")
    print(f"Tu balance de gastos es de: {total_expense}")
    print("----------------------------------------------")
    for x in ["1", "2", "3", "4", "5"]:
        if x in expense_grouped['type_expense'].unique():
            group = expense_grouped.get_group(x)['expenses']
            print(f"{x}.{dic_expense[x]} = {group.sum()}")

    print("----------------------------------------------")

    if total_expense == income:
        print("Tienes que tener cuidado, tus gastos son tan\n"
              "altos como tus ingresos.")
    elif total_expense > income:
        print("Estas gastando demasiado, ahorrar es importante.")
    elif total_expense < income:
        print("Tu salud financiera es ideal.")




#variable

dic_expense = {'1':'Gastos medicos', '2':'Gastos de casa', '3':'Ocio', '4':'Educación',
                 '5': 'Ahorros'}

# code

df = pd.DataFrame(columns = ['type_expense', 'expenses'])

income = total_income()
df = add_expenses(df)

analyze_financial(income, df, dic_expense)
