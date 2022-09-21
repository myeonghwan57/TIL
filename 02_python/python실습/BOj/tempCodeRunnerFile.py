N = int(input())
result = N
for i in range(1,N):
    result *= (N-i)

print(result)