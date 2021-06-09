# CardNumber
주어진 카드 속 재료(원소) 찾기
1. 시간초과답
- 리스트 두개 생성 후 A리스트 원소가 B원소에 있나 검사( 시간복잡도 O(N^2))
2. 이진탐색을 이용한 답
- 1번과 똑같이 하되 검사를 이진탐색으로 함.
 
3. A리스트를 리스트로 만들지 않고 set자료형으로 만듬( set자료형은 순서가 정해지지않음 ) -> 속도 fast

### 이진 탐색 다시 복습할 것
- def binary_search(num):
- l = 0
- r = n-1
- while l <= r :
- mid = (l+r)//2
- if a[mid] == num :
-  return 1
- elif a[mid] > num :
- r = mid - 1
- # 반 줄여주기 1
- else:
- l = mid + 1
- # 반 줄여주기 2
- return 0
