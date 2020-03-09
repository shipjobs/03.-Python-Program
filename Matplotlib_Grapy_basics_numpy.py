import matplotlib.pyplot as plt
import numpy as np 


"""산포도 그래프 그리기 : 회귀 분석 등 특정 패턴을 찾을때 유용한 그래프"""
plt.style.use('ggplot')   # 그래프 속성 

np.random.seed(2)          # 속성
x = np.arange(1, 1001)     # 수치 범위 지정
y = 2 * x * np.random.rand(1000)  # random 값 생성, arange 와 같아야 함

fig = plt.figure()         #
ax = fig.add_subplot(111)  # 그래프 위치 행, 열 , 번호
ax.scatter(x,y)            # 산포도 데이터 지정

plt.show()                 # 보이지