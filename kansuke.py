import pandas as pd

df = pd.read_excel('https://data.kinoquest.jp/pandas/input/sample.xlsx', sheet_name='実績管理表_売上欠損')

df.groupby('氏名').mean()
k