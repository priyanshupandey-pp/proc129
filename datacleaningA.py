import pandas as pd

df = pd.read_csv("E:/OneDrive/Desktop/Python/proc126/dwarf_stars.csv")
print(df.head())

print(df.columns)
df = df.dropna()
print(df.columns)

df["Radius"]=0.102763*df["Radius"]
df["Mass"] =df["Mass"].apply(lambda x: x.replace('$', '').replace(',','')).astype('float')
df["Mass"]=0.000954588*df["Mass"]

print(df.head())
df.drop(['Unnamed: 0'],axis=1,inplace=True)
df.to_csv("data_cleaning.csv")