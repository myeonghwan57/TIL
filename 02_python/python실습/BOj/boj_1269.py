#대칭 차집합 힙 셋 
A, B = map(int,input().split())
num_A = set(map(int,input().split()))
num_B = set(map(int,input().split()))

for i in num_B:
    if i in num_A:
        num_A.remove(i)
    elif i not in num_A:
        num_A.add(i)
print(len(num_A))