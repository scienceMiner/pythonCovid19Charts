
import pandas as pd

df = pd.read_csv('data/prices.csv')
print(df.head())

df.to_parquet('data/prices.parquet')
 
df_parquet = pd.read_parquet('data/prices.parquet')
print(df_parquet.head())


