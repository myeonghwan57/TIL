# 리스트 메서드 사용 -> 그 해당 메서드를 사용하면 원본을 변경
a = [10,1,100]
new_a = a.sort()
print(a, new_a)
# [1, 10, 100] None


# 리스트에 sotred 함수를 사용-> 원본을 변경하지 않고 return 을 하는것은 새롭게 정의 된것(list)을 return
b = [10, 1, 100 ]
new_b= sorted(b) #input 을 넣었을때 output이 존재.
print(b,new_b)
# [10, 1, 100] [1, 10, 100]

