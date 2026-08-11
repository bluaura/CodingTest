"""
[1주차 5일차 실습 문제 5] 더 맵게 (우선순위 큐 / heapq 대표 기출)

■ 문제 개요
모든 음식의 스코빌 지수를 K 이상으로 만들고자 합니다.
스코빌 지수가 가장 낮은 두 개의 음식을 다음과 같이 섞어 새로운 음식을 만듭니다:
  [새로운 스코빌 지수 = 가장 맵지 않은 음식 + (두 번째로 맵지 않은 음식 * 2)]

모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복할 때, 
음식을 섞어야 하는 [최소 횟수]를 반환하는 solution(scoville, K) 함수를 작성하세요.
(모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우 -1을 반환합니다.)
"""

import heapq

def solution(scoville, K):
    """
    1. heapq.heapify()로 기존 리스트를 O(N) 만에 최소 힙으로 변환합니다.
    2. 힙의 가장 작은 원소(scoville[0])가 K 미만인 동안 반복합니다.
    3. 음식이 2개 미만 남았는데도 K 미만이라면 만들어낼 수 없으므로 -1을 반환합니다.
    """
    # 1. 힙으로 변환 (O(N))
    heapq.heapify(scoville)
    
    mix_count = 0
    
    # 2. 가장 맵지 않은 음식(scoville[0])이 K 미만인 동안 계속 섞기
    while scoville[0] < K:
        # 음식이 2개 미만으로 남았는데 아직 K 미만이라면 -1 반환
        if len(scoville) < 2:
            return -1
            
        # 가장 맵지 않은 두 음식 추출 (O(log N))
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        # 새로운 음식 스코빌 지수 계산 후 힙에 다시 삽입 (O(log N))
        new_scoville = first + (second * 2)
        heapq.heappush(scoville, new_scoville)
        
        mix_count += 1
        
    return mix_count


# --- 자가 검증 및 동작 확인 코드 ---
if __name__ == "__main__":
    test_cases = [
        # (scoville, K, expected)
        ([1, 2, 3, 9, 10, 12], 7, 2),
        ([1, 1, 1], 10, -1),
        ([10, 12, 15], 7, 0)
    ]
    
    print("=== [5일차 실습 문제: 더 맵게 (우선순위 큐) 검증] ===")
    for i, (scoville, K, expected) in enumerate(test_cases, 1):
        result = solution(scoville.copy(), K)
        status = "[PASS]" if result == expected else f"[FAIL] (결과: {result}, 정답: {expected})"
        print(f"테스트 케이스 {i}: {status}")
