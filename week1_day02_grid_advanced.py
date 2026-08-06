"""
[1주차 2일차] 2차원 배열 회전 & 8방향 탐색 & itertools 필수 테크닉

1. 8방향 탐색 (상, 하, 좌, 우 + 대각선 4개)
2. 2차원 배열 90도 시계방향 회전 공식
3. itertools (조합 combinations, 순열 permutations)
"""

import sys
from itertools import combinations, permutations

# ==========================================
# 1. 8방향 탐색 (상, 하, 좌, 우 + 대각선 4방향)
# ==========================================
def search_8_directions():
    # 8방향 벡터: 상, 하, 좌, 우, 좌상, 우상, 좌하, 우하
    dr = [-1, 1, 0, 0, -1, -1, 1, 1]
    dc = [0, 0, -1, 1, -1, 1, -1, 1]
    
    r, c = 2, 2
    N, M = 5, 5
    print(f"--- 8방향 탐색 (기준: {r}, {c}) ---")
    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M:
            print(f"방향 {i}: ({nr}, {nc})")


# ==========================================
# 2. 2차원 배열 90도 시계방향 회전 (★ 코테 빈출)
# ==========================================
def rotate_90_clockwise(matrix):
    """
    N x M 행렬을 90도 시계방향으로 회전시키는 공식
    원래 (r, c) 요소는 회전 후 (c, N - 1 - r) 위치로 이동합니다.
    """
    N = len(matrix)         # 행 개수
    M = len(matrix[0])      # 열 개수
    
    # 회전 후 크기는 M x N 이 됨
    rotated = [[0] * N for _ in range(M)]
    
    for r in range(N):
        for c in range(M):
            rotated[c][N - 1 - r] = matrix[r][c]
            
    return rotated

def rotate_90_pythonic(matrix):
    """
    파이썬다운 90도 시계방향 회전 한 줄 팁:
    zip(*matrix[::-1])
    """
    return [list(row) for row in zip(*matrix[::-1])]


# ==========================================
# 3. itertools 조합(combinations) & 순열(permutations)
# ==========================================
def itertools_example():
    data = ['A', 'B', 'C', 'D']
    
    # 4개 중 2개를 순서 없이 뽑기 (조합)
    comb = list(combinations(data, 2))
    print("\n--- 조합 (combinations) 4C2 ---")
    print(comb) # [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]
    
    # 4개 중 2개를 순서 있게 뽑기 (순열)
    perm = list(permutations(data, 2))
    print("\n--- 순열 (permutations) 4P2 ---")
    print(perm)


if __name__ == "__main__":
    search_8_directions()
    
    sample_grid = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print("\n--- 원본 2x3 행렬 ---")
    for row in sample_grid:
        print(row)
        
    rotated_grid = rotate_90_clockwise(sample_grid)
    print("\n--- 90도 시계방향 회전 후 (3x2 행렬) ---")
    for row in rotated_grid:
        print(row)
        
    itertools_example()
