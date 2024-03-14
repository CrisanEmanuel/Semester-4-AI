"""
Se cunosc date despre angajatii unei companii, date salvate in fisierul "data/employees.csv".

1.a. Sa se stabileasca:
    1) numarul de angajati
    2) numar si tipul informatiilor (proprietatilor) detinute pentru un angajat
    3) numarul de angajati pentru care se detin date complete
    4) valorile minime, maxime, medii pentru fiecare proprietate
    5) in cazul proprietatilor nenumerice, cate valori posibile are fiecare astfel de proprietate
    6) daca sunt valori lipsa si cum se poate rezolva aceasta problema
1.b. Sa se vizualizeze:
    1) distributia salariilor acestor angajati pe categorii de salar
    2) distributia salariilor acestor angajati pe categorii de salar si echipa din care fac parte
    3) angajatii care pot fi considerati "outlieri"
"""
import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def numar_angajati(data):
    nr = len(data[1:])
    return nr


def date_angajat(lista):
    first_row = lista[0]
    num_properties = len(first_row)
    props = ""

    for property_name in first_row:
        props += property_name + " | "

    return num_properties, props


def date_angajat_complete():
    df = pd.read_csv('data/employees.csv')
    df = df.dropna()
    return len(df)


def valori_min_max_mediu():
    df = pd.read_csv('data/employees.csv')

    df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
    df['Bonus %'] = pd.to_numeric(df['Bonus %'], errors='coerce')

    summary_stats = df.describe()

    print("\nMinimum values:")
    print(summary_stats.loc['min'])
    print("\nMaximum values:")
    print(summary_stats.loc['max'])
    print("\nMedian values:")
    print(df[['Salary', 'Bonus %']].median())


def valori_numerice():
    df = pd.read_csv("data/employees.csv")

    # Identificarea tipurilor de date nenumerice
    non_numeric_columns = df.select_dtypes(exclude=['number']).columns

    # Afișarea numărului de valori unice pentru fiecare proprietate nenumerica
    for column in non_numeric_columns:
        unique_values = df[column].unique()
        print(f"Proprietatea '{column}' are {len(unique_values)} valori unice.")

    # Identificarea valorilor lipsă și numărul lor pentru fiecare proprietate nenumerica
    missing_values_count = df[non_numeric_columns].isnull().sum()
    print("\nValori lipsă pentru proprietățile nenumerice:")
    print(missing_values_count)


def problema1a():
    with open('data/employees.csv', 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
        print("Numarul de angajati:", numar_angajati(data))
        print("Numar proprietati:", date_angajat(data)[0], " Proprietati: |", date_angajat(data)[1])
        print("Numar angajati cu date complete:", date_angajat_complete())
        print(valori_min_max_mediu())
        print()
        print(valori_numerice())


def problema1b():
    df = pd.read_csv("data/employees.csv")

    # Visualizing salary distribution
    sns.histplot(df['Salary'], bins=10, kde=True)
    plt.title('Salary Distribution of Employees')
    plt.xlabel('Salary')
    plt.ylabel('Number of Employees')
    plt.show()

    # Visualizing salary distribution by team
    sns.boxplot(x='Team', y='Salary', data=df)
    plt.title('Salary Distribution by Team')
    plt.xlabel('Team')
    plt.ylabel('Salary')
    plt.xticks(rotation=45)
    plt.show()

    # Identifying outliers based on salary (lowest 1% and highest 1%)
    lower_percentile = df['Salary'].quantile(0.01)
    upper_percentile = df['Salary'].quantile(0.99)

    outliers = df[(df['Salary'] < lower_percentile) | (df['Salary'] > upper_percentile)]
    print()
    print("Employees considered as outliers based on salary:")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    # Print the DataFrame
    print(outliers)


def problema1():
    print("Problema 1.a")
    problema1a()
    print()
    print("Problema 1.b")
    problema1b()
