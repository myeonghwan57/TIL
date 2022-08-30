import sys
input = sys.stdin.read

s = input().replace("\n","").replace(" ","")
c = [0] * 26
for i in s:
    c[ord(i)-97]+=1
    
maxx = max(c)
r = []
for i in range(len(c)):
    if c[i] == maxx:
        r.append(chr(i+97))
        
r.sort()
print(*r,sep="")