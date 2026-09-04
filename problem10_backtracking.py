"""
[2주차 10일차 실습 문제 10] 피로도 (프로그래머스 Lv.2 / 백트래킹)

■ 문제 개요
유저의 현재 피로도 k와 던전별 [최소 필요 피로도, 소모 피로도]가 담긴 dungeons 배열이 주어집니다.
유저가 탐험할 수 있는 [최대 던전 수]를 반환하는 solution(k, dungeons) 함수를 작성하세요.
"""

def solution(k, dungeons):
    n = len(dungeons)
    visited = [False] * n
    max_dungeons = 0
    
    def dfs(current_k, count):
        nonlocal max_dungeons
        max_dungeons = max(max_dungeons, count)
        
        for i in range(n):
            min_req, consume = dungeons[i]
            if not visited[i] and current_k >= min_req:
                visited[i] = True
                dfs(current_k - consume, count + 1)
                visited[i] = False  # 백트래킹 상태 복구
                
    dfs(k, 0)
    return max_dungeons


# --- 자가 검증 및 동작 확인 코드 ---
if __name__ == "__main__":
    k1 = 80
    dungeons1 = [[80,20],[50,40],[30,10]]
    expected1 = 3
    
    result1 = solution(k1, dungeons1)
    status1 = "[PASS]" if result1 == expected1 else f"[FAIL] (결과: {result1}, 정답: {expected1})"
    print("=== [10일차 실습 문제: 피로도 (백트래킹) 검증] ===")
    print(f"테스트 케이스 1: {status1}")
