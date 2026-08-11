"""
[1주차 4일차 실습 문제 4] 장르별 베스트앨범 고르기 (해시 + 다중 정렬)

■ 문제 개요
노래의 장르를 나타내는 문자열 배열 genres와 
각 노래의 재생 횟수를 나타내는 정수 배열 plays가 주어집니다.

다음 조건에 따라 장르별로 최대 2개씩 베스트 앨범에 들어갈 노래의 고유 번호(인덱스)를 순서대로 수집합니다:
1. 속한 노래의 총 재생 횟수가 높은 장르를 먼저 수집합니다.
2. 장르 내에서는 재생 횟수가 높은 노래를 먼저 수집합니다.
3. 장르 내에서 재생 횟수가 같다면 고유 번호(인덱스)가 작은 노래를 먼저 수집합니다.

베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 리스트로 반환하는 solution(genres, plays) 함수를 작성하세요.
"""

from collections import defaultdict

def solution(genres, plays):
    """
    1. 장르별 총 재생 횟수를 누적하기 위한 defaultdict(int)
    2. 장르별 노래 목록 (재생횟수, 고유번호)을 저장하기 위한 defaultdict(list)
    """
    total_plays = defaultdict(int)
    genre_songs = defaultdict(list)
    
    # 1단계: 해시 맵 데이터 수집
    for i, (genre, play) in enumerate(zip(genres, plays)):
        total_plays[genre] += play
        genre_songs[genre].append((play, i))  # (재생횟수, 고유번호)
        
    # 2단계: 총 재생 횟수가 높은 장르 순으로 정렬 (내림차순)
    sorted_genres = sorted(total_plays.keys(), key=lambda g: total_plays[g], reverse=True)
    
    result = []
    
    # 3단계: 장르 순서대로 수집
    for genre in sorted_genres:
        songs = genre_songs[genre]
        
        # 장르 내 노래 정렬:
        # 1) 재생 횟수 내림차순 (-x[0])
        # 2) 재생 횟수 같으면 고유 번호 오름차순 (x[1])
        songs.sort(key=lambda x: (-x[0], x[1]))
        
        # 최대 2개까지 고유 번호(인덱스) 선택
        for play_count, song_id in songs[:2]:
            result.append(song_id)
            
    return result


# --- 자가 검증 및 동작 확인 코드 ---
if __name__ == "__main__":
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]
    expected = [4, 1, 3, 0]
    
    # 설명:
    # pop 총 재생: 600 + 2500 = 3100 (1위 장르) -> 노래 4번(2500), 1번(600)
    # classic 총 재생: 500 + 150 + 800 = 1450 (2위 장르) -> 노래 3번(800), 0번(500)
    # 결과: [4, 1, 3, 0]
    
    print("=== [4일차 실습 문제: 장르별 베스트앨범 검증] ===")
    result = solution(genres, plays)
    status = "[PASS]" if result == expected else f"[FAIL] (결과: {result}, 정답: {expected})"
    print(f"테스트 케이스 검증: {status}")
