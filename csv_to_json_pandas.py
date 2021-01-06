import pandas
df = pandas.read_csv('hrdata.csv')
df.to_json('hrdata_modified.json')