import csv

users = [{"name": "Abdus Salam", "phone": "7977646886", "role": "Programmer"}, 
{"name": "Anas Khan", "phone": "8928963329", "role": "DSA"},
{"name": "Ahmed Faraz", "phone": "5454555643", "role": "Graphic Designer"}]

keys = ["name", "phone", "role"]
with open("Employee.csv", "w") as employee:
    writer = csv.DictWriter(employee, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)