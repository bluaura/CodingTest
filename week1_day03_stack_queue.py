"""
[1주차 3일차] 필수 자료구조 - 스택(Stack) & 큐(Queue) & 덱(Deque)

1. 스택(Stack, LIFO): 파이썬 list (append, pop)
2. 큐(Queue, FIFO): collections.deque (append, popleft) -> list.pop(0) 대비 O(1) 성능 차이
3. 덱(Deque) 활용: 양방향 입출력 및 rotate() 함수
4. 대표 응용: 올바른 괄호 검사 (Stack 패턴)
"""

import sys
import time
from collections import deque

# ==========================================
# 1. 스택 (Stack, 후입선출 LIFO)
# ==========================================
def stack_example():
    stack = []
    
    # 데이터 삽입 O(1)
    stack.append(10)
    stack.append(20)
    stack.append(30)
    print("스택 상태 (append 후):", stack)
    
    # 최상단 데이터 확인 (TOP) O(1)
    if stack:
        print("스택 TOP 요소:", stack[-1])
        
    # 데이터 추출 O(1)
    popped = stack.pop()
    print("추출된 요소:", popped)
    print("스택 상태 (pop 후):", stack)


# ==========================================
# 2. 큐(Queue) vs 덱(Deque) 성능 차이 비교
# ==========================================
def queue_performance_comparison():
    N = 100000
    
    # 1) list.pop(0) 사용 시 - O(N) 발생
    lst = list(range(N))
    start_time = time.time()
    while lst:
        lst.pop(0) # 첫 번째 요소를 빼고 나머지를 다 당기므로 O(N)
    list_time = time.time() - start_time
    
    # 2) collections.deque.popleft() 사용 시 - O(1)
    dq = deque(range(N))
    start_time = time.time()
    while dq:
        dq.popleft() # 이중 연결 리스트 구조로 O(1) 시간에 제거
    deque_time = time.time() - start_time
    
    print(f"\n--- 10만 개 데이터 큐 추출 시간 비교 ---")
    print(f"list.pop(0) 소요 시간   : {list_time:.5f}초 (느림, O(N))")
    print(f"deque.popleft() 소요 시간: {deque_time:.5f}초 (빠름, O(1))")


# ==========================================
# 3. 덱(Deque)의 회전 기능 (rotate)
# ==========================================
def deque_rotate_example():
    dq = deque([1, 2, 3, 4, 5])
    print("\n--- Deque 회전 기능 (rotate) ---")
    print("원래 deque:", list(dq))
    
    # 시계방향 회전 (오른쪽으로 Shift)
    dq.rotate(2)
    print("rotate(2)  [오른쪽 2칸 Shift]:", list(dq))
    
    # 반시계방향 회전 (왼쪽으로 Shift)
    dq.rotate(-2)
    print("rotate(-2) [왼쪽 2칸 Shift]:", list(dq))


# ==========================================
# 4. 스택 대표 응용: 올바른 괄호 검사
# ==========================================
def is_valid_parentheses(s):
    """
    괄호 문자열 s가 올바른 괄호쌍인지 검사하는 함수
    예: "()()" -> True, ")(" -> False, "({[]})" -> True
    """
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in "({[":
            stack.append(char)
        elif char in ")}]" :
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
            
    return len(stack) == 0


if __name__ == "__main__":
    print("=== 1. 스택 기본 동작 ===")
    stack_example()
    
    print("\n=== 2. 큐 vs 덱 성능 비교 ===")
    queue_performance_comparison()
    
    print("\n=== 3. Deque rotate 예제 ===")
    deque_rotate_example()
    
    print("\n=== 4. 괄호 검사 예제 ===")
    test_strings = ["()()", "(({[]}))", ")(", "({[)]}"]
    for s in test_strings:
        print(f"문자열: '{s}' -> 올바른 괄호인가? {is_valid_parentheses(s)}")
