"""
[2주차 13일차 실습 문제 13] 섬 연결하기 (프로그래머스 Lv.3 / Kruskal MST & Union-Find)

■ 문제 개요
n개의 섬 사이에 다리를 건설하는 비용 costs [u, v, cost] 가 주어집니다.
모든 섬이 서로 통행 가능하도록 만들기 위해 필요한 [최소 비용]을 반환하는 solution(n, costs) 함수를 작성하세요.
(크루스칼 알고리즘: 간선 비용 오름차순 정렬 후 사이클이 생기지 않도록 Union-Find 선택)
"""

def solution(n, costs):
    # 1. 건설 비용 기준 오름차순 정렬
    costs.sort(key=lambda x: x[2])
    
    parent = list(range(n))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
        
    def union(x, y):
        rx, ry = find(x), find(y)
        if rx != ry:
            parent[ry] = rx
            return True
        return False
        
    total_cost = 0
    edges_count = 0
    
    # 2. 작은 비용의 간선부터 탐욕적으로 선택
    for u, v, cost in costs:
        if union(u, v):  # 사이클이 형성되지 않을 때만 다리 건설
            total_cost += cost
            edges_count += 1
            if edges_count == n - 1:
                break
                
    return total_cost


# --- 자가 검증 및 동작 확인 코드 ---
if __name__ == "__main__":
    n1 = 4
    costs1 = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
    expected1 = 4
    
    result1 = solution(n1, costs1)
    status1 = "[PASS]" if result1 == expected1 else f"[FAIL] (결과: {result1}, 정답: {expected1})"
    print("=== [13일차 실습 문제: 섬 연결하기 (Union-Find / MST) 검증] ===")
    print(f"테스트 케이스 1: {status1}")
