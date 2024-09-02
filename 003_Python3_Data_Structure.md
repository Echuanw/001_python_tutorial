## 1 List

### 1.1 Create List

* list is a data sequence composed of **a series of elements** in **a specific order**, so we can use it to save multiple data.
* list is a mutable type, so you can add and remove element.

```python
"""
create
"""
list0 = []                 # empty list
list1 = [35, 12, 99, 68, 55, 35, 87]
list2 = ['Python', 'Java', 'Go', 'Kotlin']
list3 = [100, 12.3, 'Python', True]
print(list1)               # [35, 12, 99, 68, 55, 35, 87]
print(list2)               # ['Python', 'Java', 'Go', 'Kotlin']
print(list3)               # [100, 12.3, 'Python', True]
```

```python
"""
list comprehensions : create list by a simple way
"""
items = [i for i in range(1, 100) if i % 3 == 0 or i % 5 == 0]
print(items)

nums2 = [num ** 2 for num in [35, 12, 97, 64, 55]]
print(nums2)

nums2 = [num for num in [35, 12, 97, 64, 55] if num > 50]
print(nums2)
```

```python
"""
Nested lists :use list comprehensions to generate nested list
	five element , each element is a list which have three element.
"""
import random
scores = [[random.randrange(60, 101) for _ in range(3)] for _ in range(5)]
print(scores)
```

### 1.2 Use of List

```python
"""
list(obj)       : make other sequences turned into lists.
len(obj)        : get number of element in list.
range([num:]num): Traversal of elements
"""
list3 = []
list4 = list(range(1, 10))  # range() offen use to traversal
list5 = list('hello')
print(list3)                # []
print(list4)                # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list5)                # ['h', 'e', 'l', 'l', 'o']
print(len(list3))           # 0
print(len(list4))           # 9
print(len(list5))           # 5

print("\r\nTraversal of elements:")
languages = ['Python', 'Java', 'C++', 'Kotlin']
print("\r\nTraversal of elements 1:")
for ele in languages:
    print("\t" + ele)
print("\r\nTraversal of elements 2:")
for index in range(len(languages)):
    print("\t" + languages[index])
```

```python
"""
`+`              splice two lists
`*`              repetition operations on lists.
`in` `not in`  determine whether an element is in the list
"""
items5 = [35, 12, 99, 45, 66]
items6 = [45, 58, 29]
items7 = ['Python', 'Java', 'JavaScript']

print("\r\nOperator + splice two lists:")
print(items5 + items6)  # [35, 12, 99, 45, 66, 45, 58, 29]
print(items6 + items7)  # [45, 58, 29, 'Python', 'Java', 'JavaScript']
items5 += items6
print(items5)  # [35, 12, 99, 45, 66, 45, 58, 29]

print("\r\nOperator * repetition:")
print(items6 * 3)  # [45, 58, 29, 45, 58, 29, 45, 58, 29]
print(items7 * 2)  # ['Python', 'Java', 'JavaScript', 'Python', 'Java', 'JavaScript']

print("\r\nOperator in determine whether an element is in the list:")
print(29 in items6)  # True
print(99 in items6)  # False
print('C++' not in items7)     # True
print('Python' not in items7)  # False
```

```python
"""
list[index]              index, index alse can be -1 to -N
list[start:end]          slicing operation, default stride is 1
list[start:end:stride]   slicing operation
"""
items8 = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']
print("\r\nlist[index]:")
print(items8[0])   # apple
print(items8[2])   # pitaya
print(items8[4])   # watermelon
items8[2] = 'durian'
print(items8)      # ['apple', 'waxberry', 'durian', 'peach', 'watermelon']
print(items8[-5])  # 'apple'       

print("\r\nlist[start:end]:")
print(items8[1:3])     # ['strawberry', 'durian']
print(items8[:3:1])    # ['apple', 'strawberry', 'durian']
print(items8[::2])     # ['apple', 'durian', 'watermelon']
print(items8[-4:-2])   # ['strawberry', 'durian']
print(items8[-2::-1])  # ['peach', 'durian', 'strawberry', 'apple']
```

```python
"""
list operate:
	list.append(ele)        : adding elements to the end of the list
	list.insert(index, ele) : new elements at the specified index
	list.remove(ele)        : delete specified elements from the list
	list.pop()              : deletes the last element in the list by default
	list.pop(index)         : delete the element at the specified index. If not found, raise `IndexError`
	list.clear()            : clear the elements in the list
	del list[index]         : like list.pop(index)
"""
languages = ['Python', 'Java', 'C++']
print("\r\n append insert:")
languages.append('JavaScript')
print(languages)  # ['Python', 'Java', 'C++', 'JavaScript']
languages.insert(1, 'SQL')
print(languages)  # ['Python', 'SQL', 'Java', 'C++', 'JavaScript']

print("\r\n remove pop clear:")
languages = ['Python', 'SQL', 'Java', 'C++', 'JavaScript']
if 'Java' in languages:
    languages.remove('Java')
if 'Swift' in languages:
    languages.remove('Swift')
print(languages)  # ['Python', 'SQL', C++', 'JavaScript']
languages.pop()
temp = languages.pop(1)
print(temp)       # SQL
languages.append(temp)
print(languages)  # ['Python', C++', 'SQL']
languages.clear()
print(languages)  # []

print("\r\n del:")
items = ['Python', 'Java', 'C++']
del items[1]
print(items)  # ['Python', 'C++']
```

```python
"""
ele index and frequency:
	list.index(ele)        : find the index position of an element in the list. If not found, raise `ValueError`
	list.index(ele,index)  : find the index position of an element from specified index.
	list.count(ele)        : new elements at the specified index
"""
items = ['Python', 'Java', 'Java', 'C++', 'Kotlin', 'Python']
print(items.index('Python'))     # 0
# find 'Python' from index 1
print(items.index('Python', 1))  # 5
print(items.count('Python'))     # 2
print(items.count('Kotlin'))     # 1
print(items.count('Swfit'))      # 0
# find 'Java' from index 3
print(items.index('Java', 3))    # ValueError: 'Java' is not in list
```

```python
"""
Sort and reverse
	list.sort()     : sort by letter 
	list.reverse()
"""
items = ['Python', 'Java', 'C++', 'Kotlin', 'Swift']

print("\r\n sort reverse:")
items.sort()
print(items)  # ['C++', 'Java', 'Kotlin', 'Python', 'Swift']
items.reverse()
print(items)  # ['Swift', 'Python', 'Kotlin', 'Java', 'C++']
```

## 2 Tuple

* Tuple alse is a data sequence composed of **a series of elements** in **a specific order**, so we can use it to save multiple data.
* But tuple is a immutable type. Once a tuple is defined, elements cannot be added or deleted, elements cannot be modify.

```python 
"""
() or ,                 : create tuple
type(tuple)             : check type
len(tuple)              : get num of tuple elements 
tuple[index]            : get element by index
tuple[start:end]        : slicing operation, default stride is 1
tuple[start:end:stride] : slicing operation
"""
t1 = (35, 12, 98)
t2 = 35, 12, 98
t3 = ('echuan', 43, True, '四川成都')
t4 = ()
t5 = 'hello',    

print("\r\n type and len:")
print(type(t1))  # <class 'tuple'>
print(type(t2))  # <class 'tuple'>
print(type(t3))  # <class 'tuple'>
print(type(t4))  # <class 'tuple'>
print(type(t5))  # <class 'tuple'>
print(len(t1))  # 3
print(len(t2))  # 4
print(len(t3))  # 4
print(len(t4))  # 4
print(len(t5))  # 4

print("\r\n []:")
print(t1[0])    # 35
print(t1[2])    # 98
print(t2[-1])   # 四川成都
print(t2[:2])   # (35, 12)
print(t2[::3])  # (35,)
```

```python
"""
immutable tuple
package and unpackage
"""
# package  
print("\r\n package unpackage:")
a = 1, 10, 100
print(type(a))  # <class 'tuple'>
print(a)        # (1, 10, 100)

# unpackage
i, j, k = a
print(i, j, k)  # 1 10 100

# immutable
print("\r\n immutable:")
a[0] = 88888  # TypeError
```

```python
"""
* Traversal of elements
* + , in ,not in
"""
t1 = (35, 12, 98)
t3 = ('echuan', 43, True, '四川成都')
# Traversal of elements
for elem in t1:
    print(elem)

# operator in
print(12 in t1)         # True
print(99 in t1)         # False
print('Hao' not in t3)  # False

# operator +
t6 = t1 + t3
print(t6)  # (35, 12, 98, 'echuan', 43, True, '四川成都')
```

```python
"""
tuple and list convert to each other
"""
infos = ('apple', 'banana', 'orange')
print(list(infos))  # ['apple', 'banana', 'orange']

frts = ['apple', 'banana', 'orange']
print(tuple(frts))  # ('apple', 'banana', 'orange')
```

## 3 Strings

### 3.1 String Definition

The so-called **string** is **a limited sequence composed of zero or more characters** , generally recorded as: $$ s = a_1a_2 \cdots a_n ,,,,, (0 \le n \le \infty) $$In Python program , we can represent a string by surrounding **single or multiple characters** with **single or double quotes**. The characters in the string can be special symbols (such as: 💩, 🐷, 🀄️), etc.

```python
"""
	* single or multiple characters
	* single or double quotes
	* three single or double quotes can include multiple lines 
"""
s1 = 'hello, world!'
s2 = "你好，世界！❤️"
s3 = '''
hello,
wonderful
world!
'''
print(s1)
print(s2)
print(s3)    # multiple lines
```

```python
"""
escape character:
	some character itself has specified mean, such as `'` or `"`, use to represent string. if want string container it, it must be escaped.
	use backslash(`\`) to indicate escape:
		\<new line>   str still connect 
		\\            \\
		\'            '
		\"            "
		\n            New Line
		\r            Carriage Return
		\t            Tab
		\b            Backspace
		\ooo          Octal value, o is ortal number,from 0 to 7
		\ xhh         Hex value, h is hexadecimal number, from 0 to F 
"""
s = 'This string will not include \
backslashes or newline characters.'
print(s)                     # This string will not include backslashes or newline characters.

s='The \\character is called backslash'
print(s)                     # The \character is called backslash

s='Hello \'Python\"'
print(s)                     # Hello 'Python"

s='Hel\blo'
print(s)                     # Helo

s='Hello\nPython'
print(s)                     # Hello<New Line>Python

s='Hello\tPython'
print(s)                     # Hello	Python

s="\141"
print(s)                     # OCT 141 is 64 + 32 + 1 = 97 Decimal , the ASCII value is a

s="\x41"
print (s)                    # Hex 41 is 4 * 16 + 1 = 65 Decimal, the ASCII value is A

s="中文"
unicode_str = s.encode('unicode_escape').decode('utf-8')
print(unicode_str)        # \u4e2d\u6587
s = '\u4e2d\u6587'
print(s)                  # 中文
```

```python
"""
raw string:
	Start with `r` or `R`.
	every character in the string has its original meaning without so-called escape characters
"""
s = r'This string will not include \
backslashes or newline characters.'
print(s)                     # This string will not include \<New Line>backslashes or newline characters.

s=r'The \\character is called backslash'
print(s)                     # The \\character is called backslash

s=R'Hello \'Python\"'
print(s)                     # Hello \'Python\"

s=R'Hello\nPython'
print(s)                     # Hello\nPython

s=R"\141"
print(s)                     # \141

s=R"\x41"
print (s)                    # \x41
```

### 3.2 String Operations

The Python language provides a very rich set of operators for string types, many of which have similar functions to list type operators. 
For example:
* use `+`operators to concatenate strings
* use `*`operators to repeat the content of a string
* use `in`and `not in`to determine whether a string contains another string
* use the `[]`and `[:]`operator to convert characters from 
* Remove a certain character or certain string from the string.

```python
"""
len(str) : obtaining the number of list elements
str(obj) : convert other to string
"""
print(len('goodbye, world'))  # 14
print(str(list(range(5))))
print(str(True))
print(str(100.001))
```

```python
"""
 `+`AND `*`operator to concatenate and repeat strings
"""
s1 = 'hello' + ', ' + 'world'
print(s1)    # hello, world
s2 = '!' * 3
print(s2)    # !!!
s1 += s2
print(s1)    # hello, world!!!
s1 *= 2
print(s1)    # hello, world!!!hello, world!!!
```

```python
"""
Indexing and slicing
	str[index] 
	str[start:stop:step]
"""
s = 'abc123456'
n = len(s)
print(s[0], s[-n])    # a a
print(s[n-1], s[-1])  # 6 6
print(s[2], s[-7])    # c c
print(s[5], s[-4])    # 3 3
print(s[2:5])         # c12
print(s[-7:-4])       # c12
print(s[2:])          # c123456
print(s[:2])          # ab
print(s[::2])         # ac246
print(s[::-1])        # 654321cba
```

```python
"""
comparison string:
	the string is compared to the size of the encoding corresponding to each character.
"""
s1 = 'a whole new world'
s2 = 'hello world'
print(s1 == s2)             # False
print(s1 < s2)              # True
print(s1 == 'hello world')  # False
print(s2 == 'hello world')  # True
print(s2 != 'Hello world')  # True
s3 = '三毛'
print(ord('三'))            # 19977
print(ord('毛'))            # 27611
s4 = 'フェイ'
print(ord('フ'))            # 12501
print(ord('ェ'))            # 12455
print(ord('イ'))            # 12452
print(s3 >= s4)             # True
print(s3 != s4)             # True
```


```python
"""
Travalsel String Character
"""
s = 'hello'
print("\r\nfor_in string by element:")
for elem in s:
    print(elem)
print("\r\nfor_in string by index:")
for i in range(len(s)):
    print(s[i])
```

### 3.3 String Methods

* Case related operations
* Find operation
* Judgment of nature
* Format string
* pruning operation
* Replacement operation
* Split and merge
* encoding and decoding
* Other methods

```python
"""
Case related operations, won't affect the original string
	str.capitalize() : Upper First Character
	str.title()      : Upper First Character of Each Word
	str.upper()      : Upper String
	str.lower()      : Lower String
"""
s1 = 'hello, man. hello, world!'
# Upper First Characher
print(s1.capitalize())  # Hello, man. hello, world!
# Upper First Character of Each Word
print(s1.title())       # Hello, Man. Hello, World!
# Upper String
print(s1.upper())       # HELLO, MAN. HELLO, WORLD!
s2 = 'GOODBYE'
# Lower String
print(s2.lower())       # goodbye
# operation not affect the original string 
print(s1)               # hello, man. hello, world!
print(s2)               # GOODBYE
```

```python
"""
Find operation
	str.find(f_str[, index]), return index. if not found, return -1
	str.index(f_str[, index]), return index. if not found, raise `ValueError`
"""
s = 'hello, world!'
print(s.find('or'))      # 8
print(s.find('or', 9))   # -1
print(s.find('of'))      # -1
print(s.index('or'))     # 8
print(s.index('or', 9))  # ValueError: substring not found
```

```python
"""
Judgment of nature
	str.startswith(s_str)  : return Ture or False
	str.endswith(e_str)    : return Ture or False
	str.isdigit()          : return Ture or False, determine whether is completely composed of numbers
	str.isalpha()          : return Ture or False, determine whether is completely composed of letters
	str.isalnum()          : return Ture or False, determine whether is made up of letters and numbers
"""
s1 = 'hello, world!'
print(s1.startswith('He'))   # False
print(s1.startswith('hel'))  # True
print(s1.endswith('!'))      # True
s2 = 'abc123456'
s2 = 'abc'
print(s2.isdigit())  # False
print(s2.isalpha())  # False
print(s3.isalpha())  # True
print(s2.isalnum())  # True
```

```python
"""
Format string
	* Control length
	* zfill
	* center and just
	* dict format
"""
# Control length， USE f""
year = 2016
event = 'Referendum'
f'Results of the {year:10} {event:15}'
'Results of the 2016       Referendum     '

# zfill (include decimal point and plus and minus signs)
print('33'.zfill(5))      # 00033
print('-33'.zfill(5))     # -0033

# center and just
s = 'hello, world'
print(s.center(20, '*'))  # ****hello, world****
print(s.rjust(20))        #         hello, world
print(s.ljust(20, '~'))   # hello, world~~~~~~~~
a = 321
b = 123
print(f'{str(a).zfill(5)} * {str(b).zfill(5)} = {a * b}')     # 00321 * 00123 = 39483


# dict format
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
	# Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```



```python
"""
pruning operation
"""
s1 = '   test@126.com  '
print(s1.strip())           # test@126.com
s2 = '~hello, world~'     
print(s2.lstrip('~'))       # hello, world~
print(s2.rstrip('~'))       # ~hello, world
```

```python
"""
Replacement operation
	str.replace(substr, replace_str[, replace_times])
"""
s = 'hello, good world'
print(s.replace('o', '@'))     # hell@, g@@d w@rld
print(s.replace('o', '@', 2))  # hell@, g@od world
```

```python
"""
Split and merge
	str.split()
	delimiter_str.join(str)
"""
s = 'I love you'
words = s.split()
print(words)            # ['I', 'love', 'you']
print('~'.join(words))  # I~love~you
```

```python
"""
encoding and decoding
"""
a = 'AEC中文フェイ'
b = a.encode('utf-8')
c = a.encode('gbk')
print(b)                  # b'AEC\xe4\xb8\xad\xe6\x96\x87\xe3\x83\x95\xe3\x82\xa7\xe3\x82\xa4'
print(c)                  # b'AEC\xd6\xd0\xce\xc4\xa5\xd5\xa5\xa7\xa5\xa4'
print(b.decode('utf-8'))  # AEC中文フェイ
print(c.decode('gbk'))    # AEC中文フェイ
```

regular expressions in subsequent courses

## 4 Sets

set is an **unordered** collection with **no duplicate elements**

### 4.1 Create Sets

```python
"""
	empty set     : only use `set()`, not Curly braces(`{}`)
	not empty set ：use `set()` or Curly braces(`{}`)
		set(string) will use letters as elements
"""
empty_set = set()
print(empty_set)       # set()
set1 = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(set1)            # {'orange', 'banana', 'pear', 'apple'}
set2 = set(['apple', 'orange', 'apple', 'pear', 'orange', 'banana'])
print(set2)            # {'orange', 'banana', 'pear', 'apple'}
set2 = set('abracadabra')
print(set2)            # {'a', 'r', 'b', 'c', 'd'}
```

```python
"""
	set comprehensions  
"""
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)      # {'d', 'r'}
```

### 4.2 Set operations

```python
"""
collection methods
	set.add(ele)     : add element
	set.discard(ele) : try to remove element. if not exists, no error be raise.  
	set.remove(ele)  : remove element. if not exists, raise `KeyError`
	set.clear()      : clear element
"""
set1 = {1, 10, 100}

set1.add(1000)
set1.add(10000)
print(set1)  # {1, 100, 1000, 10, 10000}

set1.discard(10)
if 100 in set1:
    set1.remove(100)
print(set1)  # {1, 1000, 10000}

set1.clear()
print(set1)  # set()
```

```python
"""
 `in` or `not in`
"""
set1 = {11, 12, 13, 14, 15}
print(10 in set1)      # False 
print(15 in set1)      # True
set2 = {'Python', 'Java', 'C++', 'Swift'}
print('Ruby' in set2)  # False
print('Java' in set2)  # True
```


![400](assets/note_image/image-20240830174057814.png)
```python
"""
	a intersection b           : elements in a but not in b
	a union b                  : elements in a or b or both
	a difference b             : elements in both a and b
	a symmetric difference b   : elements in a or b but not both
"""
set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {2, 4, 6, 8, 10}

# intersection
print(set1 & set2)                      # {2, 4, 6}
print(set1.intersection(set2))          # {2, 4, 6}

# union
print(set1 | set2)                      # {1, 2, 3, 4, 5, 6, 7, 8, 10}
print(set1.union(set2))                 # {1, 2, 3, 4, 5, 6, 7, 8, 10}

# difference
print(set1 - set2)                      # {1, 3, 5, 7}
print(set1.difference(set2))            # {1, 3, 5, 7}

# Symmetric difference
print(set1 ^ set2)                      # {1, 3, 5, 7, 8, 10}
print(set1.symmetric_difference(set2))  # {1, 3, 5, 7, 8, 10}

set1 = {1, 3, 5, 7}
set2 = {2, 4, 6}
set1 |= set2
print(set1)  # {1, 2, 3, 4, 5, 6, 7}
set3 = {3, 6, 9}
set1 &= set3
print(set1)  # {3, 6}
set2 -= set1
print(set2)  # {2, 4}
```

```python
"""
comparison operation
	==    : If the elements in the two sets are exactly the same
	a.issubset(b) 
	b.issuperset(a) : determine whether a is subset of a
	a.isdisjoint(b) : determine whether a and b have the same elements
"""
set1 = {1, 3, 5}
set2 = {1, 2, 3, 4, 5}
set3 = {5, 4, 3, 2, 1}
set4 = {7, 8, 9}

print(set2 == set3)           # True
print(set1.issubset(set2))    # True
print(set2.issuperset(set1))  # True
print(set1.isdisjoint(set2))  # True
print(set1.isdisjoint(set4))  # False
```

## 5 Dictionary

* dict is a immutable 

```python
"""
Create Dict
	* Use `{k:v,...}`
	* Use dict(k=v,...), dict(zip(), 'xxxxx')
	* dict comprehensions
"""
scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
print(scores)
items1 = dict(one=1, two=2, three=3, four=4)
items2 = dict(zip(['a', 'b', 'c'], '123'))
items3 = {num: num ** 2 for num in range(1, 10)}       
print(items1, items2, items3)
```

```python
"""
Use of Dict
	* Get Value by Key, if not exists, return default value. If not default value, return None
"""
# Get Value by Key
scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
print(scores['骆昊'])
print(scores['狄仁杰'])
print(scores.get('武则天', 60))
print(scores.get('武则天'))         # None
```

```python
"""
Use of Dict
	* Travelser Set
"""
# Travelser Set
scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
for key in scores:
    print(f'{key}: {scores[key]}')
    
for k, v in scores.items():
    print(k, v)
```

```python
"""
Use of Dict
	* Update Value by Key
	* add key value
"""
# Update Value by Key
scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
scores['白元芳'] = 65
scores['诸葛王朗'] = 71
scores.update(冷面=67, 方启鹤=85)
print(scores)
```

```python
"""
Use of Dict
	* remove item, if not exists, return default value
"""
# popitem pop(out stack) 
print(scores.popitem())         
print(scores.popitem())
# pop()     delete specified key, if exists return value, if not exists, return default value.
print(scores.pop('骆昊', 100))         # exists, return 95
```

```python
"""
Use of Dict
	* clear dict
"""
scores.clear()
print(scores)             # return {}
```

## 6 Travelser Advance

```python
# 字典遍历 ： items() 
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# 序列遍历 ： enumerate() 可以同时取出位置索引和对应的值
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# 同时循环两个或多个序列 : zip(x1, x2, x3, ...)
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# 逆向遍历序列 ： reversed()
for i in reversed(range(1, 10, 2)):
    print(i)  # 9, 7, 5, 3, 1

# 排序sorted & 去重set
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)

for f in sorted(set(basket)):
    print(f)
```

## 7 Case of Data Structure Practice

```python
"""Display marquee text on the screen"""
import os
import time
  
def main():
    lines = 0
    content = 'happy birthday to you…………'
    while lines < 20:
        # clear output
        os.system('cls')  # os.system('clear')
        print(content)
        # sleep 0.2 second, 200 milliseconds
        time.sleep(0.2)
        content = content[1:] + content[0]
        lines+=1
if __name__ == '__main__':
    main()
```

```python
"""
Design a function to return the suffix of a given file name.
"""
def get_suffix(filename, has_dot=False):
    """
    return the suffix of a given file name

    :param filename: filename
    :param has_dot: Whether the returned file extension should include a dot 
    :return: File extension
    """
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''

print(get_suffix("aaa.txt"))
print(get_suffix("aaa.txt."))
print(get_suffix(".txt"))
```

```python
"""
Design a function to return the suffix of a given file name.
"""
def get_suffix(filename, has_dot=False):
    """
    return the suffix of a given file name

    :param filename: filename
    :param has_dot: Whether the returned file extension should include a dot 
    :return: File extension
    """
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''

print(get_suffix("aaa.txt"))
print(get_suffix("aaa.txt."))
print(get_suffix(".txt"))
```

```python
"""
Tic-tac-toe
"""
import os

# Print chessboard
def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])

def check_victory_all_status(check_path, check_turn, board):
    match check_path:
        case 'r1': return (board['TL'] == check_turn and board['TM'] == check_turn and board['TR'] == check_turn)
        case 'r2': return (board['ML'] == check_turn and board['MM'] == check_turn and board['MR'] == check_turn)
        case 'r3': return (board['BL'] == check_turn and board['BM'] == check_turn and board['BR'] == check_turn)
        case 'c1': return (board['TL'] == check_turn and board['ML'] == check_turn and board['BL'] == check_turn)
        case 'c2': return (board['TM'] == check_turn and board['MM'] == check_turn and board['BM'] == check_turn)
        case 'c3': return (board['TR'] == check_turn and board['MR'] == check_turn and board['BR'] == check_turn)
        case 'x1': return (board['TL'] == check_turn and board['MM'] == check_turn and board['BR'] == check_turn)
        case 'x2': return (board['TR'] == check_turn and board['MM'] == check_turn and board['BL'] == check_turn)
        case _: RuntimeError('Failed to check victory')
def check_victory(move, board):
    curr_turn = board[move]
    if move == 'TL': return (check_victory_all_status('r1', curr_turn, board) or check_victory_all_status('c1', curr_turn, board) or check_victory_all_status('x1', curr_turn, board))
    if move == 'BL': return (check_victory_all_status('r3', curr_turn, board) or check_victory_all_status('c1', curr_turn, board) or check_victory_all_status('x2', curr_turn, board))
    if move == 'TR': return (check_victory_all_status('r1', curr_turn, board) or check_victory_all_status('c3', curr_turn, board) or check_victory_all_status('x2', curr_turn, board))
    if move == 'BR': return (check_victory_all_status('r3', curr_turn, board) or check_victory_all_status('c3', curr_turn, board) or check_victory_all_status('x1', curr_turn, board))
    if move == 'ML': return (check_victory_all_status('r2', curr_turn, board) or check_victory_all_status('c1', curr_turn, board))
    if move == 'TM': return (check_victory_all_status('r1', curr_turn, board) or check_victory_all_status('c2', curr_turn, board))
    if move == 'BM': return (check_victory_all_status('r3', curr_turn, board) or check_victory_all_status('c2', curr_turn, board))
    if move == 'MR': return (check_victory_all_status('r2', curr_turn, board) or check_victory_all_status('c3', curr_turn, board))
    if move == 'MM': return (check_victory_all_status('r2', curr_turn, board) or check_victory_all_status('c2', curr_turn, board) or check_victory_all_status('x1', curr_turn, board) or check_victory_all_status('x2', curr_turn, board))
    
def main():
    init_board = {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' '
    }
    begin = True
    while begin:
        curr_board = init_board.copy() 
        begin = False
        winner_exists = False
        turn = 'x'
        counter = 0
        os.system('clear')
        print_board(curr_board)
        while counter < 9 and (not winner_exists):
            move = input('轮到%s走棋, 请输入位置: ' % turn)
            while curr_board[move] != ' ':
                move = input('位置已有棋子，轮到%s重新走棋, 请输入位置: ' % turn)
            if curr_board[move] == ' ':
                counter += 1
                curr_board[move] = turn
                winner_exists = check_victory(move, curr_board)
                print(winner_exists)
                if winner_exists:
                    print(f"胜利者为{turn}")
                if turn == 'x':
                    turn = 'o'
                else:
                    turn = 'x'
            os.system('clear')
            print_board(curr_board)
        choice = input('再玩一局?(yes|no)')
        begin = choice == 'yes'

if __name__ == '__main__':
    main()
```

