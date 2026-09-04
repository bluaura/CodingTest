"""
[2주차 12일차 실습 문제 12] 배달 (프로그래머스 Lv.2 / 다익스트라)

■ 문제 개요
N개의 마을과 마을 사이를 잇는 도로 정보 road [u, v, w] (소요시간 w)가 주어집니다.
1번 마을에서 음식 주문을 받을 때, 배달 시간이 K 이하인 [마을의 개수]를 반환하는 solution(N, road, K) 함수를 작성하세요.
"""

import heapq
from collections import defaultdict

def solution(N, road, K):
    graph = defaultdict(list)
    for u, v, w in road:
        graph[u].append((v, w))
        graph[v].append((u, w))
        
    INF = float('inf')
    dist = [INF] * (N + 1)
    dist[1] = 0
    
    heap = [(0, 1)]
    
    while heap:
        current_dist, u = heapq.heappop(heap)
        
        if current_dist > dist[u]:
            continue
            
        for v, weight in graph[u]:
            distance = current_dist + weight
            if distance < dist[v]:
                dist[v] = distance
                heapq.heappush(heap, (distance, v))
                
    # 배달 시간 K 이하인 마을 개수 카운트
    return sum(1 for d in dist[1:] if d <= K)


# --- 자가 검증 및 동작 확인 코드 ---
if __name__ == "__main__":
    N1 = 5
    road1 = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
    K1 = 3
    expected1 = 4
    
    result1 = solution(N1, road1, K1)
    status1 = "[PASS]" if result1 == expected1 else f"[FAIL] (결과: {result1}, 정답: {expected1})"
    print("=== [12일차 실습 문제: 배달 (다익스트라) 검증] ===")
    print(f"테스트 케이스 1: {status1}")
