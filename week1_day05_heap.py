"""
[1주차 5일차] 필수 자료구조 - 우선순위 큐(Heap / Priority Queue)

1. 최소 힙(Min Heap) 개념 & heapq 사용법 (삽입/삭제 O(log N))
2. 최대 힙(Max Heap) 구현법 (음수 값 -val 활용)
3. 힙 구성(heapify) 및 다중 조건 튜플 힙
4. 리스트 매번 정렬 vs 힙 성능 비교
"""

import sys
import time
import heapq

# ==========================================
# 1. 최소 힙 (Min Heap) 기본 사용법
# ==========================================
def min_heap_example():
    heap = []
    
    # 힙에 요소 추가: O(log N)
    heapq.heappush(heap, 40)
    heapq.heappush(heap, 10)
    heapq.heappush(heap, 30)
    heapq.heappush(heap, 20)
    
    print("--- 최소 힙 (Min Heap) ---")
    print("힙 트리 내부 배열 상태:", heap)
    
    # 최소값 확인 (POP 하지 않고 조회만): O(1)
    print("현재 최솟값 (heap[0]):", heap[0])
    
    # 최솟값 추출: O(log N)
    print("pop 결과순서 (오름차순 자등 정렬):")
    while heap:
        val = heapq.heappop(heap)
        print(val, end=" ")
    print()


# ==========================================
# 2. 최대 힙 (Max Heap) 구현법
# ==========================================
def max_heap_example():
    # 파이썬 heapq는 기본이 최소 힙이므로, 음수(-val)로 변환하여 넣으면 최대 힙이 됩니다.
    values = [40, 10, 30, 20, 50]
    max_heap = []
    
    for v in values:
        heapq.heappush(max_heap, -v)
        
    print("\n--- 최대 힙 (Max Heap) 추출 결과 ---")
    while max_heap:
        val = -heapq.heappop(max_heap)  # 부호를 반대로 복원
        print(val, end=" ")
    print()


# ==========================================
# 3. heapify & 튜플 힙 (다중 조건 힙)
# ==========================================
def tuple_heap_example():
    # 기존 리스트를 O(N) 만에 힙 구조로 변환
    data = [5, 1, 9, 3, 7]
    heapq.heapify(data)
    print("\n--- heapify(data) 결과 ---")
    print("최소 요소 data[0]:", data[0])
    
    # 튜플 힙: (우선순위, 데이터) -> 첫 번째 원소를 기준으로 정렬됨
    task_heap = []
    heapq.heappush(task_heap, (3, "낮은 우선순위 작업"))
    heapq.heappush(task_heap, (1, "긴급 작업"))
    heapq.heappush(task_heap, (2, "보통 작업"))
    
    print("\n--- (우선순위, 작업) 튜플 힙 추출 ---")
    while task_heap:
        priority, task_name = heapq.heappop(task_heap)
        print(f"우선순위 {priority}: {task_name}")


# ==========================================
# 4. 반복 정렬 vs heapq 성능 비교
# ==========================================
def performance_comparison():
    N = 5000
    
    # 1) 매번 list.sort() 호출 시: O(N^2 log N)
    lst = []
    start = time.time()
    for i in range(N, 0, -1):
        lst.append(i)
        lst.sort()
        _ = lst[0]
    sort_time = time.time() - start
    
    # 2) heapq.heappush & heappop 활용 시: O(N log N)
    hp = []
    start = time.time()
    for i in range(N, 0, -1):
        heapq.heappush(hp, i)
        _ = hp[0]
    heap_time = time.time() - start
    
    print(f"\n--- {N}회 요소 추가 및 최솟값 유지 성능 비교 ---")
    print(f"매번 list.sort() 호출 : {sort_time:.5f}초 (느림, O(N^2 log N))")
    print(f"heapq 사용             : {heap_time:.5f}초 (빠름, O(N log N))")


if __name__ == "__main__":
    print("=== 1. 최소 힙 예제 ===")
    min_heap_example()
    
    print("\n=== 2. 최대 힙 예제 ===")
    max_heap_example()
    
    print("\n=== 3. 튜플 힙 & heapify ===")
    tuple_heap_example()
    
    print("\n=== 4. 매번 정렬 vs 힙 성능 비교 ===")
    performance_comparison()
