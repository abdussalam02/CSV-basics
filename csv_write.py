import csv

hosts = [['workstation.local', '192.168.25.46'],['webserver.local', '10.2.5.6']]
with open("hosts.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerows(hosts)