import pandas as pd
import seaborn as sns

# 데이터 셋 (집합) 불러오기
titanic = sns.load_dataset("titanic")
# titanic.to_csv("titanic.csv", index=False)

print(titanic.isnull().sum())

titanic["age"] = round(titanic['age'].fillna(titanic['age'].median())) # 값이 비어있는 곳에 값을 넣는 함수
print(titanic)
print(titanic['embarked'].value_counts()) # 값 별로 카운트해줌
titanic['embarked'] = titanic['embarked'].fillna('S')
titanic.to_csv("titanic.csv", index=False)
