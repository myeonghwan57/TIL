A, B = input().split()

min_value = int(A.replace('6', '5')) + int(B.replace('6', '5'))
max_value = int(A.replace('5', '6')) + int(B.replace('5', '6'))

print(min_value, max_value)