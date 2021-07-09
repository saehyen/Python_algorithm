# 배달
import heapq
# 다익스트라 알고리즘
# 특정 노드에서 출발하여 다른 모든 노드로 가는 최단 경로 계산

def dijkstra(start, road, distance):
    # 시작 마을에 대한 초기화(자기 자신은 거리가 0)
    distance[start] = 0
    # 큐에 삽입
    q = []
    heapq.heappush(q, (0, start))
    # 큐가 비어있지 않은 경우 계속 실행
    while q:
        # 가장 최단 거리가 짧은 마을 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 이미 처리된 것이라면 무시
        if distance[now] < dist:
            continue
        # 거리 정보가 있는 road를 하나씩 접근
        for x in road:
            # 출발지가 현재 마을인 경우
            if x[0] == now:
                # 거쳐서 가는 비용
                cost = dist + x[2]
                # 거쳐서 간 다음 마을
                next = x[1]
                # 현재 마을을 거쳐서, 다른 마을로 이동하는 거리가 더 짧은 경우
                if cost < distance[next]:
                    distance[next] = cost
                    heapq.heappush(q, (cost, next))
            # 도착지가 현재 마을인 경우
            elif x[1] == now:
                cost = dist + x[2]
                # 현재 마을로 오기 위한 출발지
                prev = x[0]
                if cost < distance[prev]:
                    distance[prev] = cost
                    heapq.heappush(q, (cost, prev))
    return distance
# N: 마을의 수
# road: 도로의 정보가 쓰인 2차원 배열 각 요소의 인덱스는 [0]: 출발마을 [1]: 도착마을 [2]: 걸리는 시간
# 배달이 가능한 K이하의 시간
def solution(N, road, K):
    answer = 0
    # 처음의 시작 마을 번호
    start = 1
    # 최단 거리 테이블을 무한으로 초기화
    distance = [int(1e9)] * (N + 1)
    # 다익스트라 알고리즘 실행
    dijkstra(start, road, distance)
    # 배달 거리가 K이하인 마을 갯수 구하기
    for x in distance:
        if x <= K:
            answer += 1
    return answer