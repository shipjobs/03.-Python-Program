# Graph 그리기
from matplotlib import pyplot as plt , font_manager
import numpy as np
import math
import pandas as pd


#한글 폰트 사용 하기 위해 설정
#윈도 10에 있는 기본 폰트 파일을 사용하도록 설정
import matplotlib.font_manager as fm 
import matplotlib 

font_location = "C:/windows/Fonts/H2GTRM.TTF"   
font_name = fm.FontProperties(fname = font_location).get_name()
matplotlib.rc('font',family=font_name )

# #샘플 데이터 - 사원별 월별 실적을 랜덤으로 생성함
# np.random.seed()
# hong = np.ceil(np.random.rand(12) * 100)
# kang = np.ceil(np.random.rand(12) * 100)
# date = np.arange(1,13)

# # 1-1 라인 그래프 설정
# plt.style.use('ggplot')
# fig = plt.figure()
# ax = fig.add_subplot(111)

# ax.plot(date, hong, label ='홍길동')
# ax.plot(date, kang, label ='강감찬')

# # #축, 제목과 범례 그리기
# ax.set_title('월별실적' ) # fontProperties 지정 없을 경우 한글 깨짐 현상
# ax.set_ylabel('단위'    )
# ax.set_xlabel('월'     )

# ax.legend()
# plt.show()


# # 1-2 막대 그래프 활용 하기
# df = pd.read_excel("d:\\VS Code\\03.-Python-Program\\excel TEST.xlsx" ,   parse_cols ="A,B,C,D,E" )   # parse_cols 원하는 컬럼별 불러오기
# df.head(10)

# fig = plt.figure(figsize=(20,10))   # 켄버스 
# ax = fig.add_subplot(111)           # 챠트 생성, 위치 지정 (1,1,1)

# wt = np.array(range(len(df)))       # 개수 많큼 분할
# w = 0.1                             # 막대 그래프 폭

# for i in df.columns :                               # 반복.....
#     ax.bar( wt , df[i], width = w , label = i )     # bar 
#     wt = wt + w

# ax.set_xticks(np.array(range(len(df))))
# ax.set_xticklabels(df.index)
# ax.set_ylabel('발생 건수')

# ax.legend()
# plt.show()

## 1-3. 라인 차트 , Bar 함께 사용하기
# s_df = pd.read_excel("d:\\VS Code\\03.-Python-Program\\excel TEST.xlsx" ,   parse_cols ="A,B,C,D,E,F,G" )   # parse_cols 원하는 컬럼별 불러오기
# s_df.head(10)

# fig = plt.figure (figsize=(10,5))
# s_ax_1 = fig.add_subplot(111)
# plt.style.use('ggplot')  # 스타일 지정


# s_ax_1.plot(s_df.index , s_df['종가'] , color='g' , label='L_주가')           #  y 축 값 설정. / 라인 차트
# #plt.show()

# # 1개의 y축에 2개의 y축 설정 하기
# s_ax_2 = s_ax_1.twinx()     
# s_ax_2.bar(s_df.index , s_df['거래금액'] , color='r' , label='L_거래금액')    #  y 축 2번 (우측) 값 설정. // 바차트..

# #축과 레이블 값 지정 하기
# s_ax_1.set_yticks( [i * 2000 for i in range(5)])
# s_ax_1.set_ylabel('주가')
# s_ax_1.set_ylabel('년월')

# s_ax_2.set_yticks( [i * 5000 for i in range(5)])
# s_ax_2.set_ylabel('거래금액')

# s_ax_1.set_title('주가 변동과 거래 금액')

# #범례 설정
# s_ax_1.legend(loc=1)
# s_ax_2.legend(loc=2)

# plt.show()


# ## 1-4. 산포도 그래프 활용하기
# df = pd.read_excel("d:\\VS Code\\03.-Python-Program\\excel TEST.xlsx" ,   parse_cols ="A,B,C,D,E,F,G" )   # parse_cols 원하는 컬럼별 불러오기
# df.head(10)


# #종가가 5000 이상 인 것만 골라내기..
# df.loc[df['종가'] >= 5000 , ['행정구역명','종가']]    #해당 조건에 해당하는 선택 컬럼에 해당 하는 리스트 불러오기

# #종가가 5000 이상 인 것만 골라내기..
# df.loc[df['거래금액'] >= 100 , ['행정구역명','거래금액']]


# #위치 별 추출 하기
# types = df['위치'].unique()

# print(types)

# #산포도 시각화 하기   > 흐름이나 유형을 한눈에 파악하기 용이
# fig = plt.figure(figsize=(15,7))

# ax = fig.add_subplot(111)

# for t in types:
#     x = df.loc[df['위치'] == t , '종가' ]
#     y = df.loc[df['위치'] == t , '거래금액' ]
    
#     ax.scatter(x,y,alpha = 0.5 , label = t)

# ax.set_title('종가별 거래금액에서의 위치')
# ax.set_xlabel('종가')
# ax.set_ylabel('거래금액')

# ax.legend(loc= 'lower right', fontsize = 10)  #

# plt.show()


## 1-5.  다수 pie 챠트 그리고 비교 하기
c_df = pd.read_excel("d:\\VS Code\\03.-Python-Program\\excel TEST.xlsx" , parse_cols ="C,D,E,F,G" )   # parse_cols 원하는 컬럼별 불러오기
c_df.head(10)
 

c_df_2004 = c_df.iloc[2]  # 컬럼명 제외 이후, 0 부터 시작 하는 3번째 선택열
c_df_2005 = c_df.iloc[3]  # 컬럼명 제외 이후, 0 부터 시작 하는 4번째 선택열

#print (c_df_2004)
#print (c_df_2005)

#선택열 ... pie chart 로 비교 하기
fig = plt.figure(figsize = (10,5))
ax1 = fig.add_subplot(121)   
ax2 = fig.add_subplot(122)


#색깔 결정하기.
color = ("red","orange","yellow","green")

ax1.pie(c_df_2004,
        explode = (0,0,1,0,0),
        labels = c_df_2004.index ,
        autopct = '%1.0f%%',
        colors = color ,
        startangle = 90 , counterclock = False )

ax2.pie(c_df_2005,
        explode = (0,0,1,0,0),
        labels = c_df_2005.index ,
        autopct = '%1.0f%%',
        colors = color ,
        startangle = 90 , counterclock = False )

ax1.set_title('2004년 현황')
ax2.set_title('2005년 현황')

fig.subplots_adjust(wspace = 0.2)  # 두 그래프 사이의 간격 
plt.show()







