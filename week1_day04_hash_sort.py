"""
[1주차 4일차] 필수 자료구조 & 알고리즘 - 해시(Hash) & 정렬(Sorting)

1. 해시(Hash Table): dict, set 의 O(1) 탐색 vs list 의 O(N) 탐색
2. collections 모듈: defaultdict, Counter 활용법
3. 다중 조건 정렬: sort(key=lambda x: ...) 테크닉
"""

import time
from collections import defaultdict, Counter

# ==========================================
# 1. 해시(dict/set) vs 리스트 탐색 성능 비교
# ==========================================
def hash_vs_list_performance():
    N = 100000
    data_list = list(range(N))
    data_set = set(range(N))
    target = N - 1  # 맨 끝 데이터 탐색
    
    # 1) list 탐색 (O(N) 순차 탐색)
    start = time.time()
    is_in_list = target in data_list
    list_time = time.time() - start
    
    # 2) set 탐색 (O(1) 해시 테이블 탐색)
    start = time.time()
    is_in_set = target in data_set
    set_time = time.time() - start
    
    print(f"--- {N}개 데이터 중 특정 요소 존재 여부 탐색 비교 ---")
    print(f"list 탐색 (target in list): {list_time:.6f}초 (O(N))")
    print(f"set 탐색  (target in set) : {set_time:.6f}초 (O(1))")


# ==========================================
# 2. collections.defaultdict & Counter 활용
# ==========================================
def collections_hash_example():
    # 1) defaultdict: 키가 없어도 KeyError 없이 기본값 자동 생성
    # int()의 기본값은 0, list()의 기본값은 []
    genre_scores = defaultdict(int)
    genre_scores["classic"] += 500
    genre_scores["pop"] += 1000
    print("\n--- defaultdict(int) 예시 ---")
    print("genre_scores:", dict(genre_scores))
    print("없는 키 'hiphop' 조회 시 기본값:", genre_scores["hiphop"])  # 0 자동 생성
    
    # 2) Counter: 요소 빈도수 자동 카운트
    items = ["apple", "banana", "apple", "orange", "banana", "apple"]
    counter = Counter(items)
    print("\n--- Counter 예시 ---")
    print("빈도수 측정 결과:", counter)
    print("가장 빈도 높은 상위 2개 (most_common):", counter.most_common(2))


# ==========================================
# 3. 파이썬 다중 조건 정렬 (sort key lambda)
# ==========================================
def multi_key_sorting_example():
    # 학생 정보: (이름, 국어점수, 영어점수)
    students = [
        ("Jun", 90, 80),
        ("Min", 90, 95),
        ("Kim", 80, 100),
        ("Lee", 90, 80)
    ]
    
    # 정렬 조건: 
    # 1) 국어점수 내림차순 (-x[1])
    # 2) 국어점수가 같다면 영어점수 내림차순 (-x[2])
    # 3) 국어/영어 모두 같다면 이름 오름차순 (x[0])
    students.sort(key=lambda x: (-x[1], -x[2], x[0]))
    
    print("\n--- 다중 조건 정렬 결과 (국어↓, 영어↓, 이름↑) ---")
    for s in students:
        print(f"이름: {s[0]}, 국어: {s[1]}, 영어: {s[2]}")


if __name__ == "__main__":
    print("=== 1. 해시(set/dict) vs 리스트 탐색 성능 비교 ===")
    hash_vs_list_performance()
    
    print("\n=== 2. defaultdict & Counter 활용 ===")
    collections_hash_example()
    
    print("\n=== 3. 다중 조건 정렬 (lambda) ===")
    multi_key_sorting_example()
