import csv

f = open("Employee.txt")
parse = csv.reader(f)
for row in parse:
    name, phone, role = row
    print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))

f.close()