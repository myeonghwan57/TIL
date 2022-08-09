import sys
str = sys.stdin.read().replace('\n', '').replace(' ','')
alph = [0]*26
for i in str:
    alph[ord(i)-97] += 1
for i in range(26):
    if alph[i] == max(alph):
        print(chr(97+i),end='')