"""
[2주차 9일차] 그래프 탐색 - BFS (너비 우선 탐색) & 2차원 미로 최단 거리

1. 큐(deque) 기반 BFS (Breadth-First Search) 동작 원리
2. 가중치가 없는 그래프/격자에서 BFS가 최단 거리를 보장하는 이유
3. visited 배열에 거리(distance)를 기록하는 테크닉
"""

from collections import deque

def bfs_maze(grid):
    """
    N x M 격자 미로에서 (0,0) -> (N-1, M-1) 최단 거리 구하기
    1: 이동 가능, 0: 벽
    """
    N = len(grid)
    M = len(grid[0])
    
    # 상, 하, 좌, 우 이동
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    # 거리 저장 겸 방문 처리 배열 (0: 미방문)
    dist = [[0] * M for _ in range(N)]
    
    queue = deque([(0, 0)])
    dist[0][0] = 1  # 시작점 거리 1
    
    while queue:
        r, c = queue.popleft()
        
        # 도착 지점에 도달하면 최단 거리 반환
        if r == N - 1 and c == M - 1:
            return dist[r][c]
            
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            # 경계 검사 & 빈칸 여부 & 미방문 여부
            if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == 1 and dist[nr][nc] == 0:
                dist[nr][nc] = dist[r][c] + 1
                queue.append((nr, nc))
                
    return -1


if __name__ == "__main__":
    sample_maze = [
        [1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 0, 1],
        [0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1]
    ]
    print("=== [9일차] 2차원 미로 BFS 최단 거리 ===")
    print("최단 이동 칸 수:", bfs_maze(sample_maze))
