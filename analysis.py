import numpy as np
import csv

cases = {}

# Read data from file
with open('result.csv') as f:
    csv_reader = csv.reader(f, delimiter='\t')
    for row in csv_reader:
        prob_number = row[0]
        dim = row[1]
        value = row[2]
        if prob_number not in cases:
            cases[prob_number] = {}
        if dim not in cases[prob_number]:
            cases[prob_number][dim] = []
        cases[prob_number][dim].append(float(value))

# Calculate infos
with open('infos.csv', 'w') as f:
    csv_writer = csv.writer(f, delimiter='\t')
    # melhor, mediana, média, desvio padrão, pior
    csv_writer.writerow(['prob_number', 'dim', 'best', 'median', 'mean', 'std', 'worst'])
    for prob_number, dims in cases.items():
        for dim, values in dims.items():
            csv_writer.writerow([prob_number, dim, min(values), np.median(values), np.mean(values), np.std(values), max(values)])
    