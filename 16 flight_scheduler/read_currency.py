import csv

with open('./data/currencyrates.csv', 'r') as file:
    lines = csv.reader(file)
    for line in lines:
        if 'Bangladesh' in line[0]:
            print(line)


# homework
# convert 50 USD to BDT
# convert 5000 BDT to USD