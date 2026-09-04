"""
[1주차 6일차 실습 문제 6] 나무 자르기 (이진 탐색 / 매개변수 탐색 대표 기출)

■ 문제 개요
나무 N개의 높이가 담긴 배열 trees와 
집으로 가져가기 위해 필요한 최소 나무 길이 M이 주어집니다.

절단기 높이 H를 지정하면 H보다 높은 나무는 (높이 - H)만큼 잘려서 가져가고, H 이하인 나무는 잘리지 않습니다.
가져갈 수 있는 나무 길이의 합이 [적어도 M 이상이 되도록 하는 절단기 높이 H의 최댓값]을 반환하는 solution(trees, M) 함수를 작성하세요.

■ 매개변수 탐색 (Parametric Search) 접근법
- 최적화 문제: "M 미터 이상을 가져갈 수 있는 H의 최댓값은 얼마인가?"
- 결정 문제: "절단기 높이가 H일 때, 잘라낸 나무의 합이 M 미터 이상인가? (Yes / No)"
- H의 범위: 0부터 max(trees)까지 이진 탐색으로 범위를 줄여나갑니다.
"""

def solution(trees, M):
    """
    절단기 높이 H의 탐색 범위: left = 0, right = max(trees)
    시간 복잡도: O(N log(max_height))
    """
    left = 0
    right = max(trees)
    result_H = 0  # 조건(나무 합 >= M)을 만족하는 H의 최댓값 저장
    
    while left <= right:
        mid_H = (left + right) // 2  # 현재 절단기 높이 후보
        
        # mid_H 높이로 자를 때 잘려나오는 나무 길이 합 계산
        total_wood = sum(tree - mid_H for tree in trees if tree > mid_H)
        
        if total_wood >= M:
            # M 미터 이상을 확보했으므로 현재 mid_H는 유효한 정답 후보!
            result_H = mid_H
            # 더 높게 잘라도 M 미터 이상이 될 수 있는지 오른쪽 범위 탐색
            left = mid_H + 1
        else:
            # 나무가 부족하므로 절단기 높이를 낮춰서 더 많이 잘라야 함 (왼쪽 범위 탐색)
            right = mid_H - 1
            
    return result_H


# --- 자가 검증 및 동작 확인 코드 ---
if __name__ == "__main__":
    test_cases = [
        # (trees, M, expected)
        ([20, 15, 10, 17], 7, 15),
        ([4, 42, 40, 26, 46], 20, 36),
        ([10, 20, 30], 10, 20)
    ]
    
    print("=== [6일차 실습 문제: 나무 자르기 (매개변수 탐색) 검증] ===")
    for i, (trees, M, expected) in enumerate(test_cases, 1):
        result = solution(trees, M)
        status = "[PASS]" if result == expected else f"[FAIL] (결과: {result}, 정답: {expected})"
        print(f"테스트 케이스 {i}: {status}")
