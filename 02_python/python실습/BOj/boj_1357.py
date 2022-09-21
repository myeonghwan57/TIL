# 뒤집힌 덧셈 a 뒤집고 b 뒤집고 나온 결과 뒤집고.
a, b = map(str,input().split())
result = str(int(a[::-1]) + int(b[::-1]))
print(int(result[::-1]))

