import pandas 
df = pandas.read_csv('hrdata.csv')
print(df)

# To check the type of data in a column, e.g. 
# >>> print(type(df['Hire Date'][0]))
#<class 'str'>

#To make Pandas read the date string as a date, use parse_dates
# import pandas
# df = pandas.read_csv('hrdata.csv', index_col='Name', parse_dates=['Hire Date'])
# print(df)

#Confirm data type change:
# >>> print(type(df['Hire Date'][0]))
# <class 'pandas._libs.tslibs.timestamps.Timestamp'>