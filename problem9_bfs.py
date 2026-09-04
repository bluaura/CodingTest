"""
[2주차 9일차 실습 문제 9] 게임 맵 최단거리 (프로그래머스 Lv.2 / BFS)

■ 문제 개요
N x M 크기의 게임 맵 maps가 주어집니다. (1: 이동 가능, 0: 벽)
내 캐릭터는 (0, 0) 위치에서 출발하고 상대 팀 진영은 (N-1, M-1) 위치에 있습니다.
상대 팀 진영에 도착하기 위해 지나가야 하는 [최소 칸 수]를 반환하는 solution(maps) 함수를 작성하세요.
(도달할 수 없는 경우 -1을 반환합니다.)
"""

from collections import deque

def solution(maps):
    N = len(maps)
    M = len(maps[0])
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    dist = [[0] * M for _ in range(N)]
    queue = deque([(0, 0)])
    dist[0][0] = 1
    
    while queue:
        r, c = queue.popleft()
        
        if r == N - 1 and c == M - 1:
            return dist[r][c]
            
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            if 0 <= nr < N and 0 <= nc < M:
                if maps[nr][nc] == 1 and dist[nr][nc] == 0:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))
                    
    return -1


# --- 자가 검증 및 동작 확인 코드 ---
if __name__ == "__main__":
    maps1 = [
        [1,0,1,1,1],
        [1,0,1,0,1],
        [1,1,1,0,1],
        [0,0,0,0,1],
        [1,1,1,1,1]
    ]
    expected1 = 13
    
    result1 = solution(maps1)
    status1 = "[PASS]" if result1 == expected1 else f"[FAIL] (결과: {result1}, 정답: {expected1})"
    print("=== [9일차 실습 문제: 게임 맵 최단거리 (BFS) 검증] ===")
    print(f"테스트 케이스 1: {status1}")
