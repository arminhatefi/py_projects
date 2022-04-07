poem = '''All that doth the flow we cannot the liquid.'''
print(poem[:13])
print(len(poem))
print(poem.startswith('All'))
print(poem.endswith('quid.'))

word = 'the'
print(poem.find(word))
print(poem.index(word))
print(poem.rfind(word))
print(poem.rindex(word))
print(poem.isalnum())

word2 = 'duck'
print(poem.find(word2))

