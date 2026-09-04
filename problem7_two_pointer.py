"""
[1주차 7일차 실습 문제 7] 연속된 부분 수열의 합 (프로그래머스 Lv.2 기출 / 투 포인터)

■ 문제 개요
비내림차순(오름차순)으로 정렬된 수열 sequence와 목표 부분합 k가 주어집니다.
다음 조건에 부합하는 연속된 부분 수열의 [시작 인덱스, 끝 인덱스]를 반환하는 solution(sequence, k) 함수를 작성하세요.

1. 부분 수열의 합은 k이어야 합니다.
2. 합이 k인 부분 수열이 여러 개인 경우, [길이가 가장 짧은 수열]을 선택합니다.
3. 길이가 가장 짧은 수열이 여러 개인 경우, [시작 인덱스가 가장 작은 수열]을 선택합니다.
"""

def solution(sequence, k):
    """
    투 포인터 (left, right) 알고리즘
    시간 복잡도: O(N)
    """
    n = len(sequence)
    left, right = 0, 0
    current_sum = sequence[0]
    
    min_len = float('inf')
    result = [0, 0]
    
    while left <= right and right < n:
        if current_sum == k:
            current_len = right - left + 1
            
            # 길이가 기존 최단 길이보다 짧은 경우 업데이트 (시작 인덱스 작은 순 자동 만족)
            if current_len < min_len:
                min_len = current_len
                result = [left, right]
                
            # 더 짧거나 다른 구간을 탐색하기 위해 left 이동
            current_sum -= sequence[left]
            left += 1
            
        elif current_sum < k:
            # 합이 k보다 작으면 right 포인터를 오른쪽으로 한 칸 이동하여 합을 증가
            right += 1
            if right < n:
                current_sum += sequence[right]
        else:
            # 합이 k보다 크면 left 포인터를 오른쪽으로 한 칸 이동하여 합을 감소
            current_sum -= sequence[left]
            left += 1
            
    return result


# --- 자가 검증 및 동작 확인 코드 ---
if __name__ == "__main__":
    test_cases = [
        # (sequence, k, expected)
        ([1, 2, 3, 4, 5], 7, [2, 3]),        # 3+4=7 (인덱스 2~3)
        ([1, 1, 1, 2, 3, 4, 5], 5, [6, 6]),  # 5 단독 (인덱스 6~6)
        ([2, 2, 2, 2, 2], 6, [0, 2])         # 2+2+2=6 (인덱스 0~2, 가장 앞선 것)
    ]
    
    print("=== [7일차 실습 문제: 연속된 부분 수열의 합 (투 포인터) 검증] ===")
    for i, (sequence, k, expected) in enumerate(test_cases, 1):
        result = solution(sequence, k)
        status = "[PASS]" if result == expected else f"[FAIL] (결과: {result}, 정답: {expected})"
        print(f"테스트 케이스 {i}: {status}")
