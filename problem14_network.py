"""
[2주차 14일차 실습 문제 14] 네트워크 (프로그래머스 Lv.3 / 그래프 컴포넌트 개수)

■ 문제 개요
컴퓨터의 개수 n과 인접 행렬 computers (computers[i][j] = 1이면 연결됨)가 주어집니다.
서로 연결된 컴퓨터들의 집합(네트워크)의 [총 개수]를 반환하는 solution(n, computers) 함수를 작성하세요.
"""

def solution(n, computers):
    visited = [False] * n
    
    def dfs(node):
        visited[node] = True
        for neighbor in range(n):
            if computers[node][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)
                
    network_count = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            network_count += 1
            
    return network_count


# --- 자가 검증 및 동작 확인 코드 ---
if __name__ == "__main__":
    n1 = 3
    computers1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    expected1 = 2
    
    result1 = solution(n1, computers1)
    status1 = "[PASS]" if result1 == expected1 else f"[FAIL] (결과: {result1}, 정답: {expected1})"
    print("=== [14일차 실습 문제: 네트워크 (그래프 컴포넌트) 검증] ===")
    print(f"테스트 케이스 1: {status1}")
