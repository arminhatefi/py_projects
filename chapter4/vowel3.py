letter = 'o'
letter2 = 'b'
letter3 = 'c'
letter4 = 'u'
letter5 = 'p'

vowel_set = {'a', 'e', 'i', 'o', 'u'}
if letter in vowel_set:
    print(letter, 'is in the vowel_set')

vowel_list =[
    'a', 'e', 'i', 'o', 'u'
]
if letter2 in vowel_list:
    print(letter2, 'is in the vowel_list')
else:
    print(letter2, 'is not in the vowel_list')

vowel_tuple = ('a', 'e', 'i', 'o', 'u')
if letter3 in vowel_tuple:
    print(letter3, 'is in the vowel_tuple')
else:
    print(letter3, 'is not in the vowel_tuple')

vowel_dic = {'a': 'apple', 'e': 'elephant',
            'i': 'impala', 'o': 'ocelot', 'u': 'unicorn'}

if letter4 in vowel_dic:
    print(letter4, 'is in the vowel_dic')
else:
    print(letter4, 'is not in the vowel_dic')

vowel_string = "aeiou"

if letter5 in vowel_string:
    print(letter5, 'is in the vowel_string')
else:
    print(letter5, 'is not in the vowel_string')
