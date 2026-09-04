"""
[2주차 12일차] 최단 경로 알고리즘 - 다익스트라 (Dijkstra)

1. 가중치(Weight)가 있는 그래프의 최단 거리 구하기
2. 우선순위 큐(heapq) 기반 다익스트라 알고리즘 (O((V + E) log V))
3. 최단 거리 테이블 dist[u] + weight < dist[v] 갱신 원리
"""

import sys
import heapq
from collections import defaultdict

def dijkstra(V, edges, start_node):
    """
    V개의 노드, edges: (u, v, weight) 리스트, start_node에서 출발
    """
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))  # 양방향 그래프 기준
        
    INF = float('inf')
    dist = [INF] * (V + 1)
    dist[start_node] = 0
    
    # 우선순위 큐: (거리, 노드)
    heap = []
    heapq.heappush(heap, (0, start_node))
    
    while heap:
        current_dist, u = heapq.heappop(heap)
        
        # 이미 처리된 더 짧은 경로가 있다면 스킵
        if current_dist > dist[u]:
            continue
            
        for v, weight in graph[u]:
            distance = current_dist + weight
            
            # 더 짧은 경로를 찾은 경우 갱신하고 힙에 삽입
            if distance < dist[v]:
                dist[v] = distance
                heapq.heappush(heap, (distance, v))
                
    return dist


if __name__ == "__main__":
    V = 5
    sample_edges = [
        (1, 2, 2),
        (1, 3, 4),
        (2, 3, 1),
        (2, 4, 7),
        (3, 5, 3),
        (4, 5, 1)
    ]
    print("=== [12일차] 다익스트라 최단 거리 예제 (출발: 1번 노드) ===")
    distances = dijkstra(V, sample_edges, 1)
    for node in range(1, V + 1):
        print(f"1번 노드 ➔ {node}번 노드 최단 거리: {distances[node]}")
