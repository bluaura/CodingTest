"""
[1주차 필수 개념] 파이썬 코테 기본 템플릿 & 2차원 격자(Grid) 탐색 원리

1. 빠른 입출력 & 재귀 깊이 설정
2. 4방향 (상, 하, 좌, 우) 이동 벡터 (dx, dy)
3. 격자 경계 검사 (Boundary Check)
"""

import sys
from collections import deque

# 1. 빠른 입출력 (백준/LG역량평가 필수)
input = sys.stdin.readline

# 2. 재귀 깊이 제한 해제 (DFS 필수)
sys.setrecursionlimit(10**6)


def grid_traversal_example():
    # 예시 3x3 격자 (0: 빈칸, 1: 벽)
    grid = [
        [0, 0, 1],
        [0, 1, 0],
        [0, 0, 0]
    ]
    
    N = len(grid)     # 행 (Row 개수, Y축 방향)
    M = len(grid[0])  # 열 (Column 개수, X축 방향)
    
    # 4방향 이동 벡터 (상, 하, 좌, 우)
    # (r, c) 좌표계 기준: r은 행(위아래), c는 열(좌우)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    # 현재 위치 (행: 1, 열: 0) -> grid[1][0]
    r, c = 1, 0
    print(f"현재 위치: ({r}, {c}), 값: {grid[r][c]}")
    
    print("\n--- 4방향 인접 칸 탐색 시작 ---")
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        
        # 1) 격자 범위(경계)를 벗어나는지 확인
        if 0 <= nr < N and 0 <= nc < M:
            # 2) 이동 가능한 위치인지 확인 (벽이 아닌지)
            if grid[nr][nc] == 0:
                print(f"방향 {i} (이동 가능): ({nr}, {nc}) -> 빈칸")
            else:
                print(f"방향 {i} (벽 있음): ({nr}, {nc}) -> 벽(1)")
        else:
            print(f"방향 {i} (범위 밖): ({nr}, {nc}) -> 격자 외부")

if __name__ == "__main__":
    grid_traversal_example()
