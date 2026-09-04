"""
[2주차 8일차 실습 문제 8] 바이러스 (백준 2606 / DFS 기초)

■ 문제 개요
신종 바이러스인 웜 바이러스는 네트워크를 통해 전파됩니다.
한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 됩니다.
1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 [웜 바이러스에 걸리게 되는 컴퓨터의 수]를 구하는 solution(n, edges) 함수를 작성하세요.
(컴퓨터의 수 n, 네트워크 연결 쌍 edges)
"""

from collections import defaultdict

def solution(n, edges):
    """
    DFS 기반의 연결된 컴퓨터 수 세기
    """
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        
    visited = [False] * (n + 1)
    
    def dfs(node):
        visited[node] = True
        count = 1  # 자기 자신 포함
        for neighbor in graph[node]:
            if not visited[neighbor]:
                count += dfs(neighbor)
        return count

    # 1번 컴퓨터가 감염되었을 때 1번을 제외한 감염 컴퓨터 수
    total_infected = dfs(1)
    return total_infected - 1  # 1번 제외


# --- 자가 검증 및 동작 확인 코드 ---
if __name__ == "__main__":
    test_n = 7
    test_edges = [(1, 2), (2, 3), (1, 5), (5, 2), (5, 6), (4, 7)]
    # 1번과 연결된 컴: 2, 3, 5, 6 (총 4개)
    
    expected = 4
    result = solution(test_n, test_edges)
    status = "[PASS]" if result == expected else f"[FAIL] (결과: {result}, 정답: {expected})"
    print(f"=== [8일차 실습 문제: 바이러스 (DFS) 검증] ===")
    print(f"테스트 케이스 검증: {status}")
