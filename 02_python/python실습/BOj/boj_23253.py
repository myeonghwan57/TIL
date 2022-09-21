# import sys
# input = sys.stdin.readline

# N, M = map(int,input().split())

# flag = True 
# for i in range(M): 
#     num = int(input())
#     book_list = list(map(int,input().split()))
#     for j in range(num-1):
#         if book_list[j] < book_list[j+1]:
#             flag = False
#             break
#     if not flag : 
#         break
# print('Yes' if flag else 'No') 


N, M = map(int,input().split())

for i in range(M):
    T  = int(input())
    book_list = list(map(int,input().split()))
    comparison = book_list.pop()
    answer = 'YES'
    while len(book_list) != 0:
        if comparison < book_list[-1]:
            comparison = book_list.pop()
        else:
            answer = 'NO'
            break
    if answer == 'NO':
        break
print(answer)
