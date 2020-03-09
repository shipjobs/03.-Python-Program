import pandas as pd 

# 대량의 데이터 Handling 

# CSV 파일 읽어오기  , 경로/포멧 설정 주의
# pop_1 = pd.read_csv("d:\\VS Code\\03.-Python-Program\\pop_2014.csv", encoding="UTF-8")
# print(pop_1.head(10))

# Excel 파일 읽어오기  , 경로/포멧 설정 주의
# pop_2 = pd.read_excel("d:\\VS Code\\03.-Python-Program\\excel TEST.xlsx")
# print(pop_2.head(10))

# 여러 데이터 관리 하기   / 조회 / 연산 등

#pop_4 = pd.read_excel("d:\\VS Code\\03.-Python-Program\\excel TEST.xlsx" ,header=3)   # 지정된 3번행 부터 불러오기
#print(pop_4.head(10))


pop_4 = pd.read_excel("d:\\VS Code\\03.-Python-Program\\excel TEST.xlsx" ,   parse_cols ="A,B,C" )   # 원하는 컬럼별 불러오기
print(pop_4.head(10))

pop_4.rename ( columns = { pop_4.columns[1] : '특기', pop_4.columns[2] : '연세'} , inplace=True)    #불러오느 컬럼은 0부터 시작,
print(pop_4.head(10))

pop_5 = pop_4.values 

