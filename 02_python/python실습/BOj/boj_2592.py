numbers = [int(input()) for i in range(10)]
print(sum(numbers)//10)
print(max(numbers, key = numbers.count))