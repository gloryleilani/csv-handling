import csv

with open('employee_info1.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    for row in csv_reader:
        if line_count == 0:
            #Join list items into string, add comma separators
            print(f'Column names are { ", ".join(row)}')
            line_count += 1
        else:
            #Escape the tab key which affects the beginning of each row
            print(f'\t {row[0]} works in the {row[1]} dept, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.') 
