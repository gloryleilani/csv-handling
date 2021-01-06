import csv

# Column names are name,address,date joined
# john smith lives at 1132 Anywhere Lane Hoboken NJ, 07030 and joined the company on Jan 4.
# erica meyers lives at 1234 Smith Lane Hoboken NJ, 07030 and joined the company on March 2.
# Processed 3 lines.

with open('employee_address.txt', mode ='r') as csv_file:

    csv_reader = csv.DictReader(csv_file)
    line_count = 0

    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {",".join(row)}')
            line_count += 1
        print(f'\t {row["name"]} lives at {row["address"]} and joined the company on {row["date joined"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')