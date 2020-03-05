import pandas as pd 

member3 = {'번호' : ['1번','2번','3번'] , 
           '이름' : ['홍길동','전우치','강감찬'] , 
           '생일' : [1975 , 1980 , 1992] }

#print(member3)

member4 = pd.DataFrame(member3)                                  # 데이타 프레임 형태로 만들어라
#print(member4)

member5 = pd.DataFrame(member3 , columns=['번호','생일','이름'])  #  주의 사항  columns vs colums
#print(member5)

##print(member5['생일']) #조회 하기 > 출력
##print(member5[['이름','생일']]) # []  vs [[]]
##print(member5.loc[0]) # 원하는 행번호 지정 조  - 행번호
##print(member5.loc[member5['번호'] >= '2번']) # 원하는 행번호 지정 조  - 행번호, 조건 부여

#DataFrame 조회 방법

#member6 =  {'번호':['1번','2번','3번','4번','5번'], 
#            '이름':['홍길동','전우치','강감찬','홍길동','일지매'],
#            '매출':[100,200,250,300,150]  }

#member7= pd.DataFrame(member6 ,columns = ['번호','매출','이름'])
#print(member7['매출'])

#member7.loc[(member7['번호'] >= '3번'  )]   ## VS Code 에서데이터 조건 조회 실패 ?? 이유가 뭐지? 
#print(member7)

member8 = pd.DataFrame(member5 ,columns = ['번호','이름','생일','지역'])
#print(member8)

member8['지역'] = ['서울','부산','대전']              #열추가
#print(member8)

member8.loc[3] = ['4번','호날두',1985 , '유벤투스']   # 행 추가
#print(member8)  #

#행 삭제
#member8.drop([0])
#print(member8)             #반영된 결과가 나타나지 않음  , 왜일까?
#print(member8.drop([0]))   #이경우는 나타남.. 같이 고민해 봅시다~  

#Data Frame  - Column 이 있는 형태 , dictionalry / list 사용

member3 = {'번호' : ['1번','2번','3번'] , 
           '이름' : ['홍길동','전우치','강감찬'] , 
           '생일' : [1975 , 1980 , 1992]   }

member4 = pd.DataFrame(member3)        # 컬럼 이름이 순서대로 지정 되지 않음 -> Columns 이용
#print(member4)    

member5 = pd.DataFrame(member3 , columns = ['번호','이름','생일'])
#print(  member5  )    

member5.loc[ member5['번호'] >= '2번']
print(  member5  ) 
print(  member5.loc[ member5['번호'] >= '2번'] )

member6 =  {'번호':['1번','2번','3번','4번','5번'], 
            '이름':['홍길동','전우치','강감찬','홍길동','일지매'],
            '매출':[100,200,250,300,150] }

member7 = pd.DataFrame(member6 , columns = ['번호','이름','매출'])  # 컬럼 생성