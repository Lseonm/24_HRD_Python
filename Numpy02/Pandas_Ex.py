import pandas as pd

# se = pd.Series([1, 2, None, 4])
# print(se)
# print()
# print(se.isna()) # 빈 값이 들어있는지 확인 (값이 비어있으면 True 반환)
# print(type(se.isna()))
#
# print()
#
# for i in range(0, len(se.isna())):
#     if se.isna()[i] == False:
#         print(f"{i}번째 인덱스 빈 값이 없음")
#     else:
#         print(f"{i}번째 인덱스 None")
#
# print()
#
# income = {"1월":9500, "2월":6200, "3월":6050, "4월":7000}
# income_se = pd.Series(income)
# print(income_se)
# print(income_se['1월'])

# 데이터 수집
# month_se = pd.Series(['1월', '2월', '3월', '4월'])
# income_se = pd.Series([9500, 6200, 6050, 7000])
# expenses_se = pd.Series([5040, 2350, 2300, 4800])
#
# df = pd.DataFrame({"월":month_se, "수입":income_se, "지출":expenses_se})
# print(df)
# print(df.iloc[0])
# print()
# print(income_se.max)

df = pd.read_csv("Hollys_table.csv", index_col=0)
print(df)
print()
print(df.iloc[1])
print()
print(df.head()) #앞에서부터 5개만 출력
print()
print(df.columns) # columns의 정보 읽어옴
print()

column_list = df.columns.to_list() # columns를 리스트 형태로 변환
print(column_list)

name = "매장"
if name in df.columns:
    print("매장을 찾았습니다")

print()

df['Total'] = df.columns.name
print(df)