"""
[2주차 14일차] 2주차 그래프 알고리즘 총정리 & 알고리즘 선택 의사결정 매트릭스

1. 문제 요구사항별 그래프 알고리즘 선택 판단 기준:
   - 가중치 없는 미로/격자 최단 거리 ➔ BFS (deque)
   - 깊이 탐색 / 완전 탐색 / 모든 경로 조사 ➔ DFS (재귀 / 스택)
   - 가중치가 다른 그래프 최단 경로 ➔ 다익스트라 (heapq)
   - 사이클 검사 / 집합 결합 / 최소 스패닝 트리 ➔ Union-Find (Kruskal)
   - 조건에 맞지 않는 경로 도중 포기 ➔ 백트래킹 (Pruning)
"""

def graph_algorithm_decision_guide():
    print("=== [2주차] 그래프 알고리즘 선택 가이드라인 ===")
    print("1. 최단 거리 (가중치 1)    ➔ BFS")
    print("2. 최단 경로 (가중치 양수)  ➔ Dijkstra (heapq)")
    print("3. 연결 요소 개수 / 백트래킹 ➔ DFS")
    print("4. 집합 결합 / MST 다리    ➔ Union-Find")

if __name__ == "__main__":
    graph_algorithm_decision_guide()
