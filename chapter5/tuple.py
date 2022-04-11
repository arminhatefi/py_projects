
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

marx_tuple1.insert(2, 'Gummo')
print(marx_tuple1)

marx_tuple2 = ['Gummo', 'Karl']
marx_tuple1.extend(marx_tuple2)
print(marx_tuple1)

marx_tuple3 = ['Adam', 'Misa']
marx_tuple1 += marx_tuple3
print(marx_tuple1)

marx_tuple3[1] = 'Wanda'
print(marx_tuple3)

numbers = [1, 2, 3, 4]
numbers[1:3] = [8,9]
print(numbers)

numbers = [1, 2, 3, 4]
numbers[1:3] = [7, 8, 9]
print(numbers)

numbers = [1, 2, 3, 4]
numbers[1:3] = []
print(numbers)

numbers = [1, 2, 3, 4]
numbers[1:3] = (98, 99, 100)
print(numbers)

numbers = [1, 2, 3, 4]
numbers[1:3] = 'wat?'
print(numbers)

print(marx_tuple1[-1])
del marx_tuple1[-1]
print(marx_tuple1)

# Delete an itme by Value and remove
print(marx_tuple1)
marx_tuple1.remove('Adam')
print(marx_tuple1)

# Get an item by offset
marx_tuple1.pop()
print(marx_tuple1)
marx_tuple1.pop(3)
print(marx_tuple1)

# Delete all item with clear()
work_quotes = ['hard', 'questions', 'quick']
work_quotes
work_quotes.clear()
print(work_quotes)