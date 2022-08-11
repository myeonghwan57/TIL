list_ = [] 
for i in range(1, 6): 
    w = input() 
    if "FBI" in w: 
        list_.append(i) 
if list_: 
    print(*list_) 
else: 
    print("HE GOT AWAY!")