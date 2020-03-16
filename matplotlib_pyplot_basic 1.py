import matplotlib.pyplot as plt

""" 1. matplotlib  장점  운영체제의 제약 없음, 다양한 설정이 가능 함 """
#  1. pip install matplotlib 설치 명령어 


## 2. 그리는 순서,   .figule()  새로운 종이 가져오기
fig = plt.figure( )

## 3. 그리는 순서,   .add_subplot() 그래프 작성/불러오기
ax =  fig.add_subplot(111)  # 행번호 , 열변호, 그림번호

## 4. 데이터 생성
data = [0,1,4,5,8] ## y 값??? 

## 5. 데이터 지정
ax.plot(data)     ## 그래프에 데이터 바인딩
#plt.show()        ## 보여주기

"""2. 여러 그래프 작성"""
# fig = plt.figure( )


# x1 =  fig.add_subplot(221)  # 2행 2열 1번째 그래프
# x2 =  fig.add_subplot(222)  # 2행 2열 2번째 그래프
# x3 =  fig.add_subplot(223)  # 2행 2열 3번째 그래프

# data = [0,1,4,5,8] ## y 값??? 

# x1.plot(data)
# x2.plot(data)
# x3.plot(data)

# plt.show()        ## 보여주기 

"""3. 그래프 스타일 지정"""
# plt.style.use('ggplot')    #  배경 블록, 선색 변경
# fig = plt.figure()          
# x = fig.add_subplot(111)
# data = [0,1]

# x.plot(data)

# plt.show()

""" 4. 꺽은선 그래프 """
# fig = plt.figure()           # 켄버스 생성
# ax = fig.add_subplot(111)    # 그래프 배치
 
# x = [0,2,4]
# y = [0,4,2]

# ax.plot(x,y)                 # 그래프에 데이터 지정

# plt.show()


""" 5 . 산포도 그리기 """
fig = plt.figure()


