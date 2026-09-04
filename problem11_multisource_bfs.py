"""
[2주차 11일차 실습 문제 11] 토마토 (백준 7576 / 다중 시작점 BFS)

■ 문제 개요
N x M 창고에 보관된 토마토들의 상태가 주어집니다. (1: 익은 토마토, 0: 안 익은 토마토, -1: 토마토 없음)
보관된 토마토들이 인접 4방향으로 익어갈 때, 모든 토마토가 익는 데 걸리는 [최소 일수]를 반환하는 solution(N, M, grid) 함수를 작성하세요.
(처음부터 모두 익어있으면 0, 모두 익지 못하는 상황이면 -1 반환)
"""

from collections import deque

def solution(N, M, grid):
    queue = deque()
    
    for r in range(N):
        for c in range(M):
            if grid[r][c] == 1:
                queue.append((r, c))
                
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == 0:
                grid[nr][nc] = grid[r][c] + 1
                queue.append((nr, nc))
                
    max_days = 0
    for r in range(N):
        for c in range(M):
            if grid[r][c] == 0:
                return -1
            max_days = max(max_days, grid[r][c])
            
    return max_days - 1


# --- 자가 검증 및 동작 확인 코드 ---
if __name__ == "__main__":
    N1, M1 = 4, 6
    grid1 = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 0]
    ]
    expected1 = 7
    
    result1 = solution(N1, M1, grid1)
    status1 = "[PASS]" if result1 == expected1 else f"[FAIL] (결과: {result1}, 정답: {expected1})"
    print("=== [11일차 실습 문제: 토마토 (다중 시작점 BFS) 검증] ===")
    print(f"테스트 케이스 1: {status1}")
