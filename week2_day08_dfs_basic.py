"""
[2주차 8일차] 그래프 탐색 - 그래프 표현법 & DFS (깊이 우선 탐색)

1. 그래프 표현 방식: 인접 행렬(Adjacency Matrix) vs 인접 리스트(Adjacency List)
2. 재귀 함수 기반 DFS (Depth-First Search) 동작 원리
3. 방문 처리(visited) 배열의 중요성
"""

import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

# ==========================================
# 1. 그래프 표현법 (인접 행렬 vs 인접 리스트)
# ==========================================
def graph_representation_example():
    # 노드 개수: 4개 (1~4번), 간선 정보: (1-2), (1-3), (2-4)
    edges = [(1, 2), (1, 3), (2, 4)]
    V = 4
    
    # 1) 인접 행렬 (Adjacency Matrix) - O(V^2) 공간
    adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]
    for u, v in edges:
        adj_matrix[u][v] = 1
        adj_matrix[v][u] = 1  # 무방향 그래프
        
    # 2) 인접 리스트 (Adjacency List) - O(V + E) 공간 (코테 추천)
    adj_list = defaultdict(list)
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
        
    print("--- 인접 리스트 출력 ---")
    for node in range(1, V + 1):
        print(f"노드 {node}와 연결된 노드들: {adj_list[node]}")


# ==========================================
# 2. 재귀(Recursion) 기반 DFS 구현
# ==========================================
def dfs(graph, node, visited, dfs_result):
    # 1. 현재 노드 방문 처리
    visited[node] = True
    dfs_result.append(node)
    
    # 2. 인접 노드 방문 (깊이 우선)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, dfs_result)


if __name__ == "__main__":
    print("=== 1. 그래프 표현법 예제 ===")
    graph_representation_example()
    
    print("\n=== 2. DFS 재귀 탐색 예제 ===")
    # 그래프 구성: 1-2, 1-3, 2-4, 3-4
    sample_graph = defaultdict(list)
    sample_edges = [(1, 2), (1, 3), (2, 4), (3, 4)]
    for u, v in sample_edges:
        sample_graph[u].append(v)
        sample_graph[v].append(u)
        
    visited = [False] * 5
    result = []
    dfs(sample_graph, 1, visited, result)
    print("1번 노드부터 시작한 DFS 방문 순서:", result)
