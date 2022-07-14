a = ['apple']
a.extend(['banana','mango']) #리스트 형태로 묶어서 넣어야 함.
print(a)  # ['apple', 'banana', 'mango']
a.extend('banana')
print(a)  # ['apple', 'banana', 'mango', 'b', 'a', 'n', 'a', 'n', 'a'] -> 문자열도 반복 가능하기 때문.
