names=' '.join(['홍길동','김몀환'])
print(names)

#numbers = ''.join([10, 20, 100])
# 오류 발생 int 라서 사용하지 못함. ->string 으로 형변환 필요
numbers = ' '.join(map(str,[10,20,100]))
print(numbers)
