import matplotlib.pyplot as plt
import numpy as np 


""" 1 산포도 그래프 그리기 : 회귀 분석 등 특정 패턴을 찾을때 유용한 그래프"""
# plt.style.use('ggplot')   # 그래프 속성 

# np.random.seed(2)          # 속성
# x = np.arange(1, 1001)     # 수치 범위 지정
# y = 2 * x * np.random.rand(1000)  # random 값 생성, arange 와 같아야 함

# fig = plt.figure()         #
# ax = fig.add_subplot(111)  # 그래프 위치 행, 열 , 번호
# ax.scatter(x,y)            # 산포도 데이터 지정  !!!!

# plt.show()                 # 보이지


"""2 막대 그래프 그리기 :"""
# plt.style.use('ggplot')
# fig = plt.figure()

# ax = fig.add_subplot(111)

# x = [3,4]   # x 길이 ,  y 길이
# y = [1,2]   # x 길이 ,  y 길이   

# ax.bar(x,y)
# plt.show()


"""3 막대 그래프 2 그리기  : 그래프 제목 달기 : barh , tick_label """
# plt.style.use('ggplot')
# fig = plt.figure()

# ax = fig.add_subplot(111)
# labels = ['english','math']     # 제목 달기

# x = [3,4]   # x 길이 ,  y 길이
# y = [1,2]   # x 길이 ,  y 길이   

# ax.bar( x , y , tick_label =labels)   # bar , tick_label (tick_lable XXX) 지정
# plt.show()



"""4 막대 그래프 2 그리기  : 그래프 제목 달기 : 가로로 뉘우기 """
# plt.style.use('ggplot')
# fig = plt.figure()

# ax = fig.add_subplot(111)
# labels = ['english','math']     # 제목 달기

# x = [3,4]   # x 길이 ,  y 길이
# y = [1,2]   # x 길이 ,  y 길이   

# ax.barh( x , y , tick_label =labels)   # barh , tick_label (tick_lable XXX) 지정
# plt.show()


"""5 여러 데이터 묶어 그리기  : 각 1,2번 그래프의 시작점 위치 지정"""
# x = [1,2]   
# y1, y2, y3 =[1,2],[2,5],[3,7]   # 그래프 3개 

# fig = plt.figure()
# ax = fig.add_subplot(111)

# w = 0.2                         #x축 눈금 (너비값)

# ax.bar(x,                    y1,  width = w , label = 'english')  # english 그래프 1번, 2번
# #ax.bar(np.array(x) + w     , y2 , width = w , label = "math")     # math 그래프    1번, 2번
# #ax.bar(np.array(x) + w * 2 , y3 , width = w , label ='korean')    # korean 그래프  1번, 2번

# ax.bar(np.array(x) + w     , y2 , width = w , label = "math")     # math 그래프    1번, 2번
# ax.bar(np.array(x) + w * 2 , y3 , width = w , label ='korean')    # korean 그래프  1번, 2번

# ax.legend()
  
# plt.show()


    
""" 6. 히스토 그램 그리기 """

# plt.style.use('ggplot')

# data1 = 100
# data2 = 10

# np.random.seed(0)
# x = np.random.normal(data1, data2 , 1000)


# fig = plt.figure()
# ax = fig.add_subplot(111)

# ax.hist(x)

# plt.show()


""" 7. Boxplot 그리기   : boxplot """

# plt.style.use('ggplot')

# x = [1,2,3,3,11,20]
# fig = plt.figure()

# ax = fig.add_subplot(111)
# ax.boxplot(x)


# plt.show()

""" 8. Pie 차트 그리기   :    """

plt.style.use('ggplot')
labels = ['english','math','korea']

sizes = [45 , 30 , 10]     # 파이 3개 각각의 값 , 전체 합쳐서 100 의 비율 , label 지정시. 개수가 맞아야 함

fig = plt.figure( figsize=(3,3))

ax = fig.add_subplot(111)

ax.pie(sizes , labels=labels)


plt.show()



