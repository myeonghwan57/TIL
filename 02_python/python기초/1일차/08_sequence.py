numbers = [1, 100, 20 , 50]
numbers2 = [10, 1000, 200 , 500]

print(numbers[1])
print(len(numbers))
print (numbers+numbers2)


numbers[0] = 3 #접근 변경.
print(numbers)

numbers.append(3000)

print(numbers)

numbers.pop(4)
print(numbers)
