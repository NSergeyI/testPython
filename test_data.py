import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

plt.interactive(True)

grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(grid)
print('------------')
df = pd.DataFrame(grid)
print(df)
print('------------')
df = pd.DataFrame(grid, columns=["one", "two", "three"])
print(df)
print('------------')
print(df["two"])
print('------------')
for x in df["two"]:
    print(x)
print('------------')
edges = df[["one", "three"]]
print(edges)
print('------------')
print(edges.add(2))
print('------------')
chicago = pd.read_json("chicago_data_01.json")
# temp = pd.read_csv("temp_data_01.csv")
temp2 = pd.read_csv("temp_data_01.csv", na_values=['Missing'])
print(chicago)
df.to_csv("df_out.csv", index=False)

temp = pd.read_csv("temp_data_01.csv", na_values=['Missing'], header=0, names=range(18), usecols=range(4, 18))
# temp[17] = temp[17].str.strip("%")
# temp[17] = pd.to_numeric(temp[17])
# temp[17] = temp[17].div(100)
temp[17] = pd.to_numeric(temp[17].str.strip("%")).div(100)
# temp[17] = temp[17]*100
# temp[17] = temp[17].astype(str)
# temp[17] = temp[17]+'%'
temp[17] = (temp[17] * 100).astype(str) + '%'
print(temp)
print('------------')

calls = pd.read_csv("sales_calls.csv")
print(calls)
revenue = pd.read_csv("sales_revenue.csv")
print(revenue)
calls_revenue = pd.merge(calls, revenue, on=['Territory', 'Month'])
print(calls_revenue[calls_revenue.Territory == 3])
print(calls_revenue[calls_revenue.Amount / calls_revenue.Calls > 500])
calls_revenue['Call_Amount'] = calls_revenue.Amount / calls_revenue.Calls
print(calls_revenue)
print(calls_revenue.Calls.sum())
print(calls_revenue.Calls.mean())
print(calls_revenue.Calls.median())
print(calls_revenue.Calls.max())
print(calls_revenue.Calls.min())
print(calls_revenue.Call_Amount.median())
print(calls_revenue[calls_revenue.Call_Amount >= calls_revenue.Call_Amount.median()])
print(calls_revenue[['Month', 'Calls', 'Amount']].groupby(['Month']).sum())
print(calls_revenue[['Territory', 'Calls', 'Amount']].groupby(['Territory']).sum())
print(calls_revenue[['Team member','Month', 'Calls', 'Amount']].groupby(['Month', 'Team member']).sum())
calls_revenue[['Territory', 'Calls']].groupby(['Territory']).sum().plot.bar()
# plt.show()
calls_revenue[['Month', 'Call_Amount']].groupby(['Month']).mean().plot.bar()