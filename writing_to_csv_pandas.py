#This will create the CSV. If a CSV already exists with that name, it will overwrite that CSV data.

import pandas
df = pandas.read_csv('hrdata.csv', 
            index_col='Employee',
            parse_dates=['Hired'],
            header=0,
            names=['Employee', 'Hired','Salary', 'Sick Days'])
df.to_csv('hrdata_modified.csv')