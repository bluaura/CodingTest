"""
[1주차 3일차 실습 문제 3] 큐 기반 프로세스 스케줄링 시뮬레이션 (프로그래머스 Lv.2 핵심)

■ 문제 개요
컴퓨터의 프로세스 실행 목록 priorities(우선순위 리스트)와 
내가 추적하고자 하는 특정 프로세스의 위치 location(0부터 시작하는 인덱스)이 주어집니다.

프로세스 실행 규칙:
1. 실행 대기 큐(Queue)에서 맨 앞의 프로세스를 하나 꺼냅니다.
2. 큐에 남아있는 프로세스 중 현재 꺼낸 프로세스보다 우선순위가 높은 프로세스가 하나라도 있다면, 
   꺼낸 프로세스를 큐의 맨 뒤로 다시 넣습니다.
3. 그러한 프로세스가 없다면 현재 꺼낸 프로세스를 즉시 실행(완료)합니다.

내가 지정한 location 위치의 프로세스가 [몇 번째로 실행되는지] 반환하는 solution(priorities, location) 함수를 작성하세요.
"""

from collections import deque

def solution(priorities, location):
    """
    collections.deque를 활용한 프로세스 큐 시뮬레이션
    각 프로세스를 (우선순위, 원래_인덱스) 형태의 튜플로 큐에 보관합니다.
    """
    # 1. (우선순위, 원래인덱스) 튜플을 담은 큐 생성
    # 예: priorities = [2, 1, 3, 2] -> queue = deque([(2,0), (1,1), (3,2), (2,3)])
    queue = deque([(priority, i) for i, priority in enumerate(priorities)])
    
    execution_order = 0  # 몇 번째로 실행되었는지 카운트
    
    # 2. 큐가 빌 때까지 시뮬레이션 진행
    while queue:
        # 맨 앞의 프로세스를 꺼냄 (O(1))
        current = queue.popleft()
        
        # 3. 큐에 남아있는 프로세스 중 현재 프로세스보다 우선순위가 높은 게 있는지 검사
        # current[0]은 현재 프로세스의 우선순위
        if any(current[0] < item[0] for item in queue):
            # 우선순위가 더 높은 게 있다면 큐의 맨 뒤로 다시 넣음
            queue.append(current)
        else:
            # 우선순위가 가장 높으므로 실행 완료 처리
            execution_order += 1
            
            # 내가 찾던 location의 프로세스라면 즉시 순서 반환
            if current[1] == location:
                return execution_order


# --- 자가 검증 및 동작 확인 코드 ---
if __name__ == "__main__":
    test_cases = [
        # (priorities, location, expected)
        ([2, 1, 3, 2], 2, 1),
        ([1, 1, 9, 1, 1, 1], 0, 5),
        ([3, 3, 4, 2], 3, 4)
    ]
    
    print("=== [3일차 실습 문제: 큐 프로세스 스케줄링 검증] ===")
    for i, (priorities, location, expected) in enumerate(test_cases, 1):
        result = solution(priorities, location)
        status = "[PASS]" if result == expected else f"[FAIL] (결과: {result}, 정답: {expected})"
        print(f"테스트 케이스 {i}: {status}")
