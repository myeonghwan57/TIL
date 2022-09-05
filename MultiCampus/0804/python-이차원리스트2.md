# Python - 이차원리스트 2

 **순회**

이차원 리스트 생성 

```python
matrix = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 0, 1, 2]
]

print(matrix)
>>> [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2]]

```

각각의 인덱스의 요소를 출력하고 싶은경우

```python
print(matrix[0][0], matrix[0][1], matrix[0][2], matrix[0][3])
print(matrix[1][0], matrix[1][1], matrix[1][2], matrix[1][3])
print(matrix[2][0], matrix[2][1], matrix[2][2], matrix[2][3])

>>> 1 2 3 4
>>> 5 6 7 8
>>> 9 0 1 2

# 크기가 커진다면 비효율적이다.
-> # for문을 사용해서 출력 할 수 있다 . 
for i in range(3):
	for j in range(4):
		print(matrix[i][j], end=" ")
	print()


```

행 우선 순회 /열 우선 순회

```python
 # 행 우선 순회
matrix = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 0, 1, 2]
]
for i in range(3):
	for j in range(4):
		print(matrix[i][j], end=" ")
	print()
>>> 1 2 3 4
>>> 5 6 7 8
>>> 9 0 1 2



# 열 우선 순회
matrix = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 0, 1, 2]
]
for i in range(4):
	for j in range(3):
		print(matrix[j][i], end=" ")
	print()
>>> 1 5 9
>>> 2 6 0
>>> 3 7 1
>>> 4 8 2
```

이차원 리스트의 합 구하기 

```python
matrix = [
[1, 1, 1, 1],
[1, 1, 1, 1],
[1, 1, 1, 1]
]
total = 0
for i in range(3):
	for j in range(4):
		total += matrix[i][j]
print(total)
>>> 12

# 보다 더 간단하게 코드를 구현해 구할수 있다.
matrix = [
[1, 1, 1, 1],
[1, 1, 1, 1],
[1, 1, 1, 1]
]
total = sum(map(sum, matrix))
print(total)
>>> 12


```

**전치**: 전치란 행렬의 행과 열을 서로 맞바꾸는것을 의미한다.

```python
matrix = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 0, 1, 2]
]
transposed_matrix = [[0] * 3 for _ in range(4)]
	for i in range(4):
		for j in range(3):
			transposed_matrix[i][j] = matrix[j][i] # 행, 열 맞바꾸기
"""
transposed_matrix = [
[1, 5, 9],
[2, 6, 0],
[3, 7, 1],
[4, 8, 2]
]
"""
```

**회전** : 행렬의 요소들을 전부 회전한 위치로 변경해주는것을 의미한다.

```python
# 왼쪽으로 90도 회전
matrix = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
n = 3
rotated_matrix = [[0] * n for _ in range(n)]
for i in range(n):
	for j in range(n):
		rotated_matrix[i][j] = matrix[j][n-i-1]

# 오른쪽으로 90도 회전 
matrix = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
n = 3
rotated_matrix = [[0] * n for _ in range(n)]
for i in range(n):
	for j in range(n):
		rotated_matrix[i][j] = matrix[n-j-1][i]
```

