"""
[1주차 6일차] 필수 알고리즘 - 이진 탐색(Binary Search) & bisect & 매개변수 탐색

1. 이진 탐색(Binary Search) 기본 원리 (O(log N))
2. 파이썬 bisect 모듈 (bisect_left, bisect_right) 활용
3. 특정 범위 안의 원소 개수 세기 (count_by_range)
4. 매개변수 탐색(Parametric Search) 개념 맛보기
"""

import time
from bisect import bisect_left, bisect_right

# ==========================================
# 1. 이진 탐색 (Binary Search) 직접 구현
# ==========================================
def binary_search_manual(arr, target):
    """
    정렬된 배열 arr에서 target의 인덱스를 반환 (없으면 -1)
    시간 복잡도: O(log N)
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1   # 오른쪽 구간 탐색
        else:
            right = mid - 1  # 왼쪽 구간 탐색
            
    return -1


# ==========================================
# 2. 파이썬 bisect 모듈 활용
# ==========================================
def bisect_module_example():
    # 정렬된 배열이어야 함!
    arr = [1, 2, 4, 4, 4, 7, 9]
    target = 4
    
    # bisect_left: target이 들어갈 가장 왼쪽 인덱스 (4가 시작하는 첫 위치: 2)
    left_idx = bisect_left(arr, target)
    
    # bisect_right: target이 들어갈 가장 오른쪽 인덱스 (4가 끝난 직후 위치: 5)
    right_idx = bisect_right(arr, target)
    
    print("--- bisect 모듈 사용 예시 ---")
    print(f"배열: {arr}, Target: {target}")
    print(f"bisect_left 인덱스 : {left_idx}")
    print(f"bisect_right 인덱스: {right_idx}")
    print(f"숫자 {target}의 개수 : {right_idx - left_idx}개")


# ==========================================
# 3. 범위 내 원소 개수 구하기 (count_by_range)
# ==========================================
def count_by_range(arr, left_val, right_val):
    """
    정렬된 배열 arr에서 [left_val, right_val] 범위에 속하는 원소 개수를 O(log N)에 반환
    """
    right_idx = bisect_right(arr, right_val)
    left_idx = bisect_left(arr, left_val)
    return right_idx - left_idx


# ==========================================
# 4. O(N) 순차 탐색 vs O(log N) 이진 탐색 성능 비교
# ==========================================
def performance_comparison():
    N = 10000000  # 1천만 개 데이터
    arr = list(range(N))
    target = N - 1
    
    # 1) O(N) 순차 탐색
    start = time.time()
    _ = target in arr
    linear_time = time.time() - start
    
    # 2) O(log N) 이진 탐색 (bisect)
    start = time.time()
    idx = bisect_left(arr, target)
    binary_time = time.time() - start
    
    print(f"\n--- {N:,}개 데이터 탐색 성능 비교 ---")
    print(f"O(N) 순차 탐색 (in 연산)  : {linear_time:.6f}초")
    print(f"O(log N) 이진 탐색 (bisect): {binary_time:.6f}초")


if __name__ == "__main__":
    print("=== 1. 수동 이진 탐색 예제 ===")
    sample = [1, 3, 5, 7, 9, 11, 13, 15]
    print(f"배열 {sample}에서 9의 위치:", binary_search_manual(sample, 9))
    
    print("\n=== 2. bisect 모듈 예제 ===")
    bisect_module_example()
    
    print("\n=== 3. 범위 탐색 (count_by_range) ===")
    data = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
    print(f"배열 {data}에서 [3, 4] 범위 원소 개수:", count_by_range(data, 3, 4))
    
    print("\n=== 4. 이진 탐색 성능 비교 ===")
    performance_comparison()
