# FineSquare
### 프로그래머스 멀쩡한 사각형문제
#### 가로 w 세로 h의 작은 정사각형들로 이루어진 사각형 중에 두 꼭지점을 이어 잘려나가는 사각형을 제외한 사각형 수 구하기

- 1. y = h/w의 그래프를 이용하는 방법
- :  모든 점을 이으면 그래프가 나오는데 각 y값에 대하여 정수가 아니라면 2개씩 빼는 방법을 사용
- : 만약 세로가 더 크다면 가로세로를 바꿔서 y값을 구함


- 2. w,h의 공약수를 구하는 방법 ( 찾아본 방법 )
- : 가로*세로-(가로+세로-두수의공약수) 라는 방법으로 가능
