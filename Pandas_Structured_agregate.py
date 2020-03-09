import pandas as pd 

# 대량의 데이터 Handling 

# CSV 파일 읽어오기  , 경로/포멧 설정 주의
# pop_1 = pd.read_csv("d:\\VS Code\\03.-Python-Program\\pop_2014.csv", encoding="UTF-8")  //euc_kr
# print(pop_1.head(10))

# Excel 파일 읽어오기  , 경로/포멧 설정 주의
# pop_2 = pd.read_excel("d:\\VS Code\\03.-Python-Program\\excel TEST.xlsx")               //euc_kr
# print(pop_2.head(10))

# 여러 데이터 관리 하기   / 조회 / 연산 등

#pop_4 = pd.read_excel("d:\\VS Code\\03.-Python-Program\\excel TEST.xlsx" ,header=3)   # 지정된 3번행 부터 불러오기
#print(pop_4.head(10))


# 
pop_4 = pd.read_excel("d:\\VS Code\\03.-Python-Program\\excel TEST.xlsx" ,   parse_cols ="A,B,C,D,E" )   # parse_cols 원하는 컬럼별 불러오기
#print(pop_4.head(10))

#pop_4.rename ( columns = { pop_4.columns[1] : '남자', pop_4.columns[2] : '여자'} , inplace=True)    #불러오느 컬럼은 0부터 시작,
#print(pop_4.head(10))   

##
#pop_5 = pop_4.sort_values(by="행정구역명" , ascending="True")

pop_4['여자인구비율'] = pop_4['여자 인구수'] / pop_4['총인구수'] * 100
pop_4['남자인구비율'] = pop_4['남자 인구수'] / pop_4['총인구수'] * 100 
#print(pop_4.head(10)) 



##데이터 프레임 합치기 * Concat  ,  Merge 
sal_2016 = {'이름':['홍길동','일지매','전우치'] , 
            '급여': [200,150,250] }

sal_2017 = {'이름':['일지매','강감찬','전우치','홍길동'] , 
            '급여' : [180,210,270,220] }
df_sal_2016 = pd.DataFrame (sal_2016 , columns=['이름','급여'])  
df_sal_2017 = pd.DataFrame (sal_2017 , columns=['이름','급여'])   


## Concat
sal_concat = pd.concat ([df_sal_2016 , df_sal_2017])   # 열에 이어 붙어 넣기 
sal_concat2 = pd.concat ([df_sal_2016 , df_sal_2017] , axis=1)  # 행을 열에 기준하여 붙어 넣기
sal_concat3 = pd.concat ([df_sal_2016 , df_sal_2017] , axis=1 , join='inner')  # 공통이 있는 내용만  가져 오기

## Merge 
sal_merge_4 = pd.merge (df_sal_2016 , df_sal_2017 , on='이름')   # 이름에 기준 하여 합치기  [ ] 없는 것 주의
sal_merge_4 = pd.merge (df_sal_2016 , df_sal_2017 , on='이름' ,  how='right')   # 이름에 기준 하여 합치기  [ ] 없는 것 주의
print(sal_merge_4)
