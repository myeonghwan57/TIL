# numbers = input().split()
# print(sum(numbers))
# unsupported operand type(s) for +: 'int' and 'str' -> int형을 str 형과 + 연산자로 더할수 없음 

# 수정 numbers 리스트를 정수형으로 변환.
numbers = input().split()
numbers = map(int,numbers)
print(sum(numbers))