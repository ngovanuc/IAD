import pandas as pd
import numpy as np
from functools import reduce
from datetime import datetime
import os

files = os.listdir('metrics')
dfs = []

# Read csv files

for file in files:
	if '.csv' in file and 'wally' in file:
		df = pd.read_csv('metrics/'+file)
		df = df.drop(columns=['load.cpucore', 'load.min1', 'load.min5', 'load.min15'])
		dfs.append(df)

# Process dataframes

start = dfs[0].min()['now']
end = dfs[0].max()['now']
for df in dfs:
	if df.min()['now'] > start:
		start = df.min()['now']

id_vars = ['now']
dfs2 = []
for df in dfs:
	df = df.drop(np.argwhere(list(df['now'] < start)).reshape(-1))
	df = df.drop(np.argwhere(list(df['now'] > end)).reshape(-1))
	melted = df.melt(id_vars=id_vars).dropna()
	df = melted.pivot_table(index=id_vars, columns="variable", values="value")
	dfs2.append(df)
dfs = dfs2

def safe_merge(dfs):
    merged = dfs[0]
    for i in range(1, len(dfs)):
        # Xác định các cột trùng giữa hai DataFrame
        common_cols = merged.columns.intersection(dfs[i].columns)
        # Loại bỏ chúng khỏi DataFrame bên phải để tránh lỗi merge
        dfs[i] = dfs[i].drop(columns=common_cols)
        merged = pd.merge(merged, dfs[i], left_index=True, right_index=True)
    return merged

df_merged = safe_merge(dfs)

# Change timezone string format

ni = []
for i in df_merged.index:
	dt = datetime.strptime(i[:-5], '%Y-%m-%d %H:%M:%S')
	ni.append(dt.strftime('%Y-%m-%dT%H:%M:%SZ'))
df_merged.index = ni

# Save train and test sets

start = round(df_merged.shape[0] * 0.1)
df_merged = df_merged[start:]
split = round(df_merged.shape[0] / 2)
df_merged[:split].to_csv('train.csv')
df_merged[split:].to_csv('test.csv')
d = pd.DataFrame(0, index=np.arange(df_merged[split:].shape[0]), columns=df_merged.columns)
d.to_csv('labels.csv')