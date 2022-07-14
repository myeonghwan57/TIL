a = input()
start = ord('a')

while True:
    print(chr(start), end = ' ')
    
    if (chr(start) == a):
        break
    
    start = start + 1
