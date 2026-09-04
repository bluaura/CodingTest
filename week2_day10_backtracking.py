"""
[2주차 10일차] 백트래킹 (Backtracking) & 상태 공간 나무 가지치기

1. 백트래킹(Backtracking)의 개념: DFS 탐색 중 불필요한 경로를 끊는(Pruning) 기법
2. 상태 복구 패턴: visited[i] = True -> 재귀 호출 -> visited[i] = False
3. N과 M (1) 순열 생성 알고리즘
"""

def backtracking_n_and_m(N, M):
    """
    1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열(순열) 모두 구하기
    """
    result = []
    visited = [False] * (N + 1)
    current = []
    
    def dfs(depth):
        # M개를 모두 선택한 경우 (탈출 조건)
        if depth == M:
            result.append(list(current))
            return
            
        for i in range(1, N + 1):
            if not visited[i]:
                # 1. 상태 변경 (방문)
                visited[i] = True
                current.append(i)
                
                # 2. 다음 깊이 탐색
                dfs(depth + 1)
                
                # 3. 상태 복구 (원상복구 - 백트래킹 핵심!)
                current.pop()
                visited[i] = False
                
    dfs(0)
    return result


if __name__ == "__main__":
    print("=== [10일차] N과 M (1) 백트래킹 예제 (N=3, M=2) ===")
    res = backtracking_n_and_m(3, 2)
    print("생성된 순열 목록:", res)
