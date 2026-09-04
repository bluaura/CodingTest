"""
[1주차 7일차] 필수 알고리즘 - 투 포인터(Two Pointers) & 슬라이딩 윈도우(Sliding Window)

1. 투 포인터(Two Pointers) 기본 개념 (O(N) 알고리즘)
   - 동일 방향 투 포인터 (start, end)
   - 양 끝 투 포인터 (left, right)
2. 슬라이딩 윈도우(Sliding Window) 개념 (고정 크기 구간 합 O(N))
3. O(N^2) 이중 반복문 vs O(N) 투 포인터/슬라이딩 윈도우 성능 비교
"""

import time

# ==========================================
# 1. 동일 방향 투 포인터 (부분 수열 합 구하기)
# ==========================================
def two_pointers_same_direction(arr, target_sum):
    """
    양의 정수로 이루어진 배열 arr에서 연속 부분 수열의 합이 target_sum인 구간 구하기
    시간 복잡도: O(N)
    """
    n = len(arr)
    count = 0
    current_sum = 0
    end = 0
    
    # start 포인터를 0부터 N-1까지 1씩 증가
    for start in range(n):
        # end 포인터를 가능한 만큼 오른쪽으로 이동
        while current_sum < target_sum and end < n:
            current_sum += arr[end]
            end += 1
            
        # 부분합이 target_sum과 같으면 카운트
        if current_sum == target_sum:
            count += 1
            
        # start를 다음 칸으로 옮기기 전에 현재 start의 값을 제외
        current_sum -= arr[start]
        
    return count


# ==========================================
# 2. 양 끝 투 포인터 (두 수의 합 구하기)
# ==========================================
def two_pointers_opposite(arr, target_sum):
    """
    정렬된 배열 arr에서 두 수의 합이 target_sum인 쌍 찾기
    시간 복잡도: O(N)
    """
    left, right = 0, len(arr) - 1
    pairs = []
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target_sum:
            pairs.append((arr[left], arr[right]))
            left += 1
            right -= 1
        elif current_sum < target_sum:
            left += 1   # 합을 키워야 하므로 left 증가
        else:
            right -= 1  # 합을 줄여야 하므로 right 감소
            
    return pairs


# ==========================================
# 3. 슬라이딩 윈도우 (고정 크기 K의 최대 구간 합)
# ==========================================
def sliding_window_fixed(arr, K):
    """
    크기가 N인 배열에서 길이가 K인 연속 구간의 최대합 구하기
    시간 복잡도: O(N)
    """
    n = len(arr)
    if n < K:
        return 0
        
    # 1. 첫 K개 원소의 합 구하기 (첫 윈도우)
    current_window_sum = sum(arr[:K])
    max_sum = current_window_sum
    
    # 2. 윈도우를 오른쪽으로 한 칸씩 미밀며 슬라이딩
    for i in range(K, n):
        # 새로 들어오는 원소 add(arr[i]), 나가는 원소 subtract(arr[i-K])
        current_window_sum += arr[i] - arr[i - K]
        max_sum = max(max_sum, current_window_sum)
        
    return max_sum


# ==========================================
# 4. 이중 반복문 O(N^2) vs 투 포인터 O(N) 성능 비교
# ==========================================
def performance_comparison():
    N = 20000
    arr = list(range(1, N + 1))
    target_sum = N  # 예: 20,000
    
    # 1) 이중 반복문 O(N^2)
    start = time.time()
    count_naive = 0
    for i in range(len(arr)):
        s = 0
        for j in range(i, len(arr)):
            s += arr[j]
            if s == target_sum:
                count_naive += 1
                break
            elif s > target_sum:
                break
    naive_time = time.time() - start
    
    # 2) 투 포인터 O(N)
    start = time.time()
    count_tp = two_pointers_same_direction(arr, target_sum)
    tp_time = time.time() - start
    
    print(f"--- {N:,}개 데이터에서 구간 합 탐색 성능 비교 ---")
    print(f"O(N^2) 이중 반복문 : {naive_time:.5f}초")
    print(f"O(N) 투 포인터     : {tp_time:.5f}초")


if __name__ == "__main__":
    print("=== 1. 동일 방향 투 포인터 예제 ===")
    data = [1, 2, 3, 2, 5]
    print(f"배열 {data}에서 합이 5인 부분수열 개수:", two_pointers_same_direction(data, 5))
    
    print("\n=== 2. 양 끝 투 포인터 예제 ===")
    sorted_data = [1, 2, 3, 4, 6, 8, 9]
    print(f"정렬 배열 {sorted_data}에서 두 수의 합이 10인 쌍:", two_pointers_opposite(sorted_data, 10))
    
    print("\n=== 3. 고정 슬라이딩 윈도우 예제 ===")
    win_data = [2, 4, 7, 1, 5, 3]
    print(f"배열 {win_data}에서 길이 3인 최대 구간 합:", sliding_window_fixed(win_data, 3))
    
    print("\n=== 4. 이중 반복문 vs 투 포인터 성능 비교 ===")
    performance_comparison()
