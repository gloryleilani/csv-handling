import csv

with open('employee_info2.txt', mode = 'w') as csv_file:
    employee_writer = csv.writer(csv_file, delimiter=',', quotechar = '"', quoting=csv.QUOTE_MINIMAL)
    employee_writer.writerow(['Mary Adams', 'Legal', 'May'])
