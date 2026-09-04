"""
[2주차 11일차] 그래프 탐색 - 다중 시작점 BFS (Multi-source BFS)

1. 시작점이 2개 이상일 때 BFS 처리 원리
2. 시점 0에 모든 시작점(Source)을 큐에 미리 넣는 기술
3. 격자 익히기 / 바이러스 동시 전파 시뮬레이션
"""

from collections import deque

def multisource_bfs_example(grid):
    """
    N x M 격자에서 여러 익은 토마토(1)가 동시에 전파되는 최소 일수 구하기
    1: 익은 토마토, 0: 안 익은 토마토, -1: 빈칸
    """
    N = len(grid)
    M = len(grid[0])
    
    queue = deque()
    
    # 1. 시점 0에 존재하는 모든 익은 토마토(1)를 큐에 동시에 삽입
    for r in range(N):
        for c in range(M):
            if grid[r][c] == 1:
                queue.append((r, c))
                
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    # 2. 동시 전파 시작
    while queue:
        r, c = queue.popleft()
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == 0:
                grid[nr][nc] = grid[r][c] + 1  # 날짜 1일 증가
                queue.append((nr, nc))
                
    # 3. 안 익은 토마토(0) 남아있는지 검사 및 최대 날짜 구하기
    max_days = 0
    for r in range(N):
        for c in range(M):
            if grid[r][c] == 0:
                return -1  # 모두 익히지 못함
            max_days = max(max_days, grid[r][c])
            
    return max_days - 1  # 시작일이 1이었으므로 1 차감


if __name__ == "__main__":
    sample_grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 0]
    ]
    print("=== [11일차] 다중 시작점 BFS 토마토 전파 ===")
    print("모두 익는 최소 일수:", multisource_bfs_example(sample_grid))
