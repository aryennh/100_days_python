import pandas as pd

file = pd.read_csv('birthdays.csv')
di = file.to_dict()
print(di['name'][0])