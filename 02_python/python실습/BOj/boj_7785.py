n = int(input())
names = {}
for _ in range(n):
    name, register_ = input().split()
    names[name] = register_
    if names[name] == 'leave':
        del names[name]
rev_names = sorted(names.keys(), reverse= True)
for i in rev_names:
    print(i)