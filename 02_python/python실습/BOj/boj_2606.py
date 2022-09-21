n = int(input())
m = int(input())
list_ = [[] for _ in range(n+1)]
for i in range(m):
    p1, p2 = map(int,input().split())
      
    list_[p1].append(p2)
    list_[p2].append(p1)

