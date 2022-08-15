word = input()
reversed_word = ''

for i in word:
    reversed_word = i + reversed_word

print(f'{reversed_word}')