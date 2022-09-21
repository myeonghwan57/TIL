color = ['black','brown','red','orange','yellow',
        'green','blue', 'violet','grey','white']

color1 = color.index(input())
color2 = color.index(input())
color3 = color.index(input())

result = ((color1*10)+color2)*(10**color3)
print(result)
