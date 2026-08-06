"""
[1주차 1일차 실습 문제 1] 상하좌우 로봇 이동 시뮬레이션 - 정답 및 완벽 해설

■ 문제 개요
N x N 크기의 격자 공간에서 로봇이 (0, 0) 위치에서 시작합니다.
입력으로 주어진 이동 명령 문자열(commands)에 따라 로봇을 이동시킵니다.
- 'U' : 위쪽으로 1칸 이동 (행 index - 1)
- 'D' : 아래쪽으로 1칸 이동 (행 index + 1)
- 'L' : 왼쪽으로 1칸 이동 (열 index - 1)
- 'R' : 오른쪽으로 1칸 이동 (열 index + 1)

★ 핵심 조건: 로봇이 격자 경계(0 <= r < N, 0 <= c < N)를 벗어나는 명령을 받으면 해당 명령은 무시합니다.
"""

def solution(N, commands):
    """
    방법 1: 딕셔너리를 활용한 방향 벡터 매핑 (가장 가독성이 좋고 실전 추천 방식)
    """
    # 1. 현재 로봇의 위치 초기화 (행: r, 열: c)
    r, c = 0, 0
    
    # 2. 이동 방향에 따른 (dr, dc) 변화량 딕셔너리 정의
    # (r: 행/세로 방향 변화량, c: 열/가로 방향 변화량)
    # U(상): r이 -1, D(하): r이 +1, L(좌): c가 -1, R(우): c가 +1
    move_dir = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)
    }
    
    # 3. 명령어를 하나씩 순회하며 이동 시뮬레이션 진행
    for cmd in commands:
        # 현재 명령어에 해당하는 방향 변화량 가져오기
        dr, dc = move_dir[cmd]
        
        # 이동 후 예상되는 다음 위치 계산 (Next Row, Next Column)
        nr = r + dr
        nc = c + dc
        
        # 4. 경계 검사 (Boundary Check)
        # N x N 격자이므로 행(nr)과 열(nc)이 모두 0 이상 N 미만이어야만 유효한 좌표
        if 0 <= nr < N and 0 <= nc < N:
            # 유효한 좌표인 경우에만 실제 로봇의 위치를 업데이트
            r, c = nr, nc
        else:
            # 경계를 벗어나는 경우: 아무 작업도 하지 않고 명령을 무시함 (pass)
            pass
            
    # 최종 위치 반환
    return r, c


def solution_alternative(N, commands):
    """
    방법 2: 리스트 인덱스를 활용한 전통적인 방향 벡터 방식 (DFS/BFS 탐색 시 주로 사용하는 구조)
    """
    r, c = 0, 0
    
    # 이동 명령 종류와 방향 벡터 배열
    move_types = ['U', 'D', 'L', 'R']
    dr = [-1, 1, 0, 0]  # 상, 하, 좌, 우 행 변화량
    dc = [0, 0, -1, 1]  # 상, 하, 좌, 우 열 변화량
    
    for cmd in commands:
        # 명령어가 move_types의 몇 번째 인덱스인지 찾기
        for i in range(4):
            if cmd == move_types[i]:
                nr = r + dr[i]
                nc = c + dc[i]
                break
                
        # 경계 검사 후 좌표 갱신
        if 0 <= nr < N and 0 <= nc < N:
            r, c = nr, nc
            
    return r, c


# --- 자가 검증 및 동작 확인 코드 ---
if __name__ == "__main__":
    test_cases = [
        (5, "RRDDLU", (1, 1)),
        (3, "UUUDDD", (2, 0)),
        (5, "RRRRRDDDDD", (4, 4)),
    ]
    
    print("=== [방법 1: 딕셔너리 매핑 방식 테스트] ===")
    for i, (N, commands, expected) in enumerate(test_cases, 1):
        result = solution(N, commands)
        status = "[PASS]" if result == expected else f"[FAIL] (결과: {result}, 정답: {expected})"
        print(f"테스트 케이스 {i}: {status}")
        
    print("\n=== [방법 2: 인덱스 배열 방식 테스트] ===")
    for i, (N, commands, expected) in enumerate(test_cases, 1):
        result = solution_alternative(N, commands)
        status = "[PASS]" if result == expected else f"[FAIL] (결과: {result}, 정답: {expected})"
        print(f"테스트 케이스 {i}: {status}")
