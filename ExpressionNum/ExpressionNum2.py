# 한줄풀이( 등차수열의 합 풀이 )
def expressions(num):
    return len([i  for i in range(1,num+1,2) if num % i is 0])