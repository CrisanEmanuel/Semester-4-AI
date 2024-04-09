import csv

import pandas as pd


def processData(data_to_process, output_file):
    # Încarcă datele din fișierul CSV
    data = pd.read_csv(data_to_process, usecols=['Happiness.Score', 'Economy..GDP.per.Capita.', 'Freedom'])

    # Înlocuiește valorile lipsă din fiecare coloană cu media respectivă
    data.fillna(data.mean(), inplace=True)

    # Înlocuiește valorile egale cu zero din fiecare coloană cu media respectivă
    data.replace(0, data.mean(), inplace=True)

    # Salvează datele actualizate înapoi în fișierul CSV
    data.to_csv(output_file, index=False)


def loadDataOneFeature(fileName, inputVariabName, outputVariabName):
    data = []
    dataNames = []
    with open(fileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                dataNames = row
            else:
                data.append(row)
            line_count += 1
    selectedVariable = dataNames.index(inputVariabName)
    inputs = [float(data[i][selectedVariable]) for i in range(len(data))]
    selectedOutput = dataNames.index(outputVariabName)
    outputs = [float(data[i][selectedOutput]) for i in range(len(data))]

    return inputs, outputs

def loadDataTwoFeatures(fileName, inputVariabName1, inputVariabName2, outputVariabName):
    data = []
    dataNames = []
    with open(fileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                dataNames = row
            else:
                data.append(row)
            line_count += 1
    selectedVariable = dataNames.index(inputVariabName1)
    inputs1 = [float(data[i][selectedVariable]) for i in range(len(data))]
    selectedVariable = dataNames.index(inputVariabName2)
    inputs2 = [float(data[i][selectedVariable]) for i in range(len(data))]
    selectedOutput = dataNames.index(outputVariabName)
    outputs = [float(data[i][selectedOutput]) for i in range(len(data))]

    return inputs1, inputs2, outputs
