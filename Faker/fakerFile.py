from faker import Faker
import csv

fake = Faker()

with open('names.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['name', 'lastname'])
    for _ in range(600):
        name = fake.first_name()
        lastname = fake.last_name()
        writer.writerow([name, lastname])