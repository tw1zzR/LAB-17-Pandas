import csv

with open('weight.csv', 'w', newline='') as file:
    writer = csv.writer(file, dialect='excel')

    field = ['CarMake', 'LoadCapacity', 'NumFlights']
    writer.writerow(field)

    writer.writerow(['Volvo', '20', '31'])
    writer.writerow(['Daf', '20', '22'])
    writer.writerow(['Scania', '25', '27'])
    writer.writerow(['Mercedes', '24', '16'])
    writer.writerow(['Iveco', '15', '33'])
    writer.writerow(['Renault', '18', '28'])
    writer.writerow(['Man', '22', '26'])
    writer.writerow(['Chevrolet', '16', '12'])