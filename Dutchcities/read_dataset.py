import pandas as pd

nl_cities = pd.read_csv('nl_cities.csv')

print(nl_cities.isna().sum())

print(nl_cities.admin_name.value_counts())
print(nl_cities.groupby("admin_name").count())


