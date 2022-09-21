from multiprocessing.sharedctypes import Value


num = -10
# 조건문 코드
if num >= 0:
    value = num
else:
    value = -num
print(num,value)

#조건 표현식 코드 
vlaue = num if num>=0 else -num
print(num,value)

