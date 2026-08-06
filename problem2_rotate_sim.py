"""
[1주차 2일차 실습 문제 2] 지뢰 탐지기 및 2차원 배열 90도 회전 시뮬레이션

■ 문제 개요
N x N 크기의 격자 지도 grid가 주어집니다. (0: 빈칸, 1: 지뢰)
1. 먼저 지도를 [90도 시계방향으로 1회 회전]시킵니다.
2. 회전된 지도에서 빈칸(0)인 위치에 대하여, [인접한 8방향(상,하,좌,우,대각선 4개)]에 있는 지뢰(1)의 총 개수를 카운트하여 기록합니다.
   (지뢰가 있던 위치는 그대로 -1 또는 원래 지뢰 표시 유지)

최종적으로 회전 및 지뢰 카운트가 완료된 N x N 결과 배열을 반환하는 solution(N, grid) 함수를 작성하세요.
"""

def solution(N, grid):
    """
    1단계: 2차원 배열 90도 시계방향 회전
    원래 (r, c) 좌표 ➔ 회전 후 (c, N - 1 - r) 좌표
    """
    rotated_grid = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            rotated_grid[c][N - 1 - r] = grid[r][c]
            
    # 2단계: 8방향 탐색 벡터 정의 (상, 하, 좌, 우, 좌상, 우상, 좌하, 우하)
    dr = [-1, 1, 0, 0, -1, -1, 1, 1]
    dc = [0, 0, -1, 1, -1, 1, -1, 1]
    
    # 3단계: 결과 지도를 보관할 N x N 배열
    result_grid = [[0] * N for _ in range(N)]
    
    for r in range(N):
        for c in range(N):
            if rotated_grid[r][c] == 1:
                # 이미 지뢰가 있던 칸은 -1로 표기
                result_grid[r][c] = -1
            else:
                # 빈칸인 경우 인접한 8방향의 지뢰 개수 세기
                mine_count = 0
                for i in range(8):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    
                    # 격자 경계(Boundary Check) 검사
                    if 0 <= nr < N and 0 <= nc < N:
                        if rotated_grid[nr][nc] == 1:
                            mine_count += 1
                            
                result_grid[r][c] = mine_count
                
    return result_grid


# --- 자가 검증 및 동작 확인 코드 ---
if __name__ == "__main__":
    sample_N = 3
    sample_grid = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    
    # 90도 회전 후 모습:
    # [0, 0, 1]
    # [0, 1, 0]
    # [0, 0, 0]
    
    expected_result = [
        [1, 2, -1],
        [1, -1, 2],
        [1, 1, 1]
    ]
    
    res = solution(sample_N, sample_grid)
    status = "[PASS]" if res == expected_result else f"[FAIL]\n결과:\n{res}\n정답:\n{expected_result}"
    print(f"테스트 케이스 검증: {status}")
