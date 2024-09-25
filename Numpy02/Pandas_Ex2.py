import pandas as pd

# df = pd.read_csv("https://github.com/dongupak/DataML/raw/main/csv/vehicle_prod.csv", index_col=0)
# df.to_csv("vehicle.csv", encoding="utf-8", index=False)
# print(df)

df = pd.read_csv("vehicle.csv")
print(df)
print()
print(df.columns)
print()
print(df['2007'])

df["Total"] = df.sum(axis=1) # 가로의 값을 모두 더한 값을 담을 column 추가
df["Mean"] = df.mean(axis=1) # 가로의 값들의 평균을 담을 column 추가
print(df)

df.to_csv("NewData.csv", encoding='utf-8')