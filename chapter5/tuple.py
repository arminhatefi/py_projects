
marx_tuple = ('Groucho', 'Chico', 'Harpo')
print(marx_tuple)
type(marx_tuple)
a, b, c = marx_tuple
print(a)

marx_tuple1 = ['Groucho', 'Chico', 'Harpo']
type(marx_tuple1)
tuple(marx_tuple1)

marx3 = ('yada',) * 3
print(marx3)

words = ('fresh', 'out', 'of', 'ideas')
for word in words:
    print(word)

t1 = ('fee', 'fie', 'foe')
t2 = ('flop',)
id(t1)
id(t2)
t1 += t2
print(t1)
id(t1)

t3 = list(t1)
print(t3[-1])

marx_tuple1 = ['Groucho', 'Chico', 'Harpo']
marx_tuple1.reverse()
print(marx_tuple1)
marx_tuple1.append('Zeppo')
print()