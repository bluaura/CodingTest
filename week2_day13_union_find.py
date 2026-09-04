"""
[2주차 13일차] 그래프 알고리즘 - 서로소 집합(Disjoint Set / Union-Find)

1. 서로소 집합(Union-Find) 개념: 여러 노드가 같은 집합(그래프)에 속해있는지 판단하는 자료구조
2. find(x) 경로 압축(Path Compression) 최적화
3. union(x, y) 집합 합치기 연산
"""

class UnionFind:
    def __init__(self, n):
        # 자기 자신을 부모 노드로 초기화
        self.parent = list(range(n + 1))
        
    def find(self, x):
        """
        x가 속한 집합의 대표(루트) 노드를 찾는 연산 (경로 압축 적용)
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 루트를 부모로 재설정 (경로 압축)
        return self.parent[x]
        
    def union(self, x, y):
        """
        x가 속한 집합과 y가 속한 집합을 합치는 연산
        """
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x != root_y:
            self.parent[root_y] = root_x
            return True  # 합치기 성공
        return False  # 이미 같은 집합에 속해 있음 (사이클 발생 의미)


if __name__ == "__main__":
    print("=== [13일차] 서로소 집합(Union-Find) 예제 ===")
    uf = UnionFind(6)
    
    # (1, 2), (2, 3), (4, 5) 연결
    uf.union(1, 2)
    uf.union(2, 3)
    uf.union(4, 5)
    
    print("1과 3은 같은 집합인가?", uf.find(1) == uf.find(3))  # True
    print("1과 5는 같은 집합인가?", uf.find(1) == uf.find(5))  # False
