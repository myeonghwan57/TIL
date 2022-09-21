# a= 0
# while a<5:
#     print(a)
#     a+=1

n = 0
total = 0
user_input = int(input())

while n <= user_input:
    print(f'n={n}')
    total += n
    n+=1
print(total)