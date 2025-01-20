import csv

def query(value):
    with open("loads.csv", mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['reference_number'] == value:
                return row
    return "Not found"

print(query('REF04684'))