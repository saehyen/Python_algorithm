# statistic2
## 산술평균, 중앙값, 최빈값, 범위
### 산술평균
 - 사용한 함수: 
   1) round(num) : 반올림
   2) ceil(num) : 올림
   3) floor(num) : 내림(음의 극을 향한 내림)
   4) trunc(num) : 내림(0을 향한 내림)
   
### 중앙값
 - 사용한 함수:
  1) len(array) : 리스트의 길이
### 최빈값
 - 사용한 함수:
  1) mode_dict = Counter(nums) : 리스트의 개수를 딕셔너리에 저장
  2) mode_dict.mott_common() : 원소와 개수의 형태를 내림차순으로 정렬
  3) 사용하기 위해선 from collections import Counter 을 선언해줘야 함.(collection 안의 Counter)
 
### 범위
 - 사용한 함수:
  1) Max(array) : 리스트의 최대값
  2) Min(array) : 리스트의 최소값
  
 #### 틀렸습니다가 자꾸 작동되었던 문제. 꼼꼼히 확인하는 습관 들일 것
