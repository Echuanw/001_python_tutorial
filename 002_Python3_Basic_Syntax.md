## 1 Variables in Python

### 1.1 Variables and types

1. `int`: Python can handle integers of any size,  support:
	* **BIN** stands for binary, **binary** (for example `0b100`, converted to decimal is 4)
	* **OCT** represents the octal system, **octal** (for example `0o100`, converted to decimal is 64)
	* **DEC** represents the decimal system, **decimal** ( `100`) 
	* **HEX** means hexadecimal, **hexadecimal** ( `0x100`, converted to The decimal notation is 256). 

```python
print(0b100)  # BIN binary
print(0o100)  # OCT octal
print(100)    # DEC decimal
print(0x100)  # HEX hexadecimal
```

2. `float`: Floating point numbers are also decimals. They are called floating point numbers because when expressed in scientific notation, the index of the decimal point of a floating point number is variable. In addition to mathematical writing (such as `123.456`) Scientific notation is also supported (e.g. `1.23456e2`, representing $\small{1.23456 \times 10^{2}}$). Run the code below and see what the output is.

```python
print(123.456)    # decimals
print(1.23456e2)  # scientific notation
```

3. `str`: A string is any text wrapped in **single quotes** or **double quotes**, such as `'hello'`and `"hello"`.
    
4. `bool`: Boolean type has only `True`two `False`values. If the value of a variable has only two states, we can use Boolean.

### 1.2 Variable naming

- Rules section:
    - Rule 1: Variable names consist of **letters** , **numbers** and **underscores** , and cannot begin with numbers. We strongly recommend that you understand the letters mentioned here to mean **using only English letters as much as possible** .
    - Rule 2: Python is **a case-sensitive** programming language. Simply put, uppercase `A`and lowercase `a`are two different variables. 
    - Rule 3: Variable names **should not have the same name as Python keywords** , and **avoid Python reserved words as much as possible** . The keywords here refer to words with special meanings in Python programs (such as: `is`, `if`, `else`, `for`, `while`, `True`, `False`etc.). Reserved words mainly refer to the names of built-in functions and built-in modules of the Python language (such as: `int`, `print`, `input`, `str`, `math`, `os`etc. ).
- **Conventional(惯例) part**:
    - **Convention 1**: Variable names usually use lowercase English letters, and multiple words are connected with underscores.
    - **Convention 2**: Protected variables begin with a single underscore.
    - **Convention 3**: Private variables start with two underscores.

### 1.3 Use of variables

```python
"""
use `type`functions to check the type of variables
Author: echuan
"""
a = 100
b = 123.45
c = 'hello, world'
d = True
print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'str'>
print(type(d))  # <class 'bool'>
```

```python
"""
change the type of variables through Python's built-in functions
- `int()`  : Convert a numerical value or string into an integer, you can specify the base.
- `float()`: Convert a string (when possible) to a floating point number.
- `str()`  : Convert the specified object into string form, and you can specify the encoding method.
- `chr()`  : Convert an integer (character encoding) into the corresponding (one-character) string.
- `ord()`  : Convert a (one-character) string into the corresponding integer (character encoding).
"""  
a = 100
b = 123.45
c = '123'
d = '100'
e = '123.45'
f = 'hello, world'
g = True
print(float(a))         # int类型的100转成float，输出100.0
print(int(b))           # float类型的123.45转成int，输出123
print(int(c))           # str类型的'123'转成int，输出123
print(int(c, base=16))  # str类型的'123'按十六进制转成int，输出291
print(int(d, base=2))   # str类型的'100'按二进制转成int，输出4
print(float(e))         # str类型的'123.45'转成float，输出123.45
print(bool(f))          # str类型的'hello, world'转成bool，输出True
print(int(g))           # bool类型的True转成int，输出1
print(chr(a))           # int类型的100转成str，输出'd'
print(ord('d'))         # str类型的'd'转成int，输出100
```

```python
"""
	Variable Swap
"""
a = 100
b = 'hello, world'
c = '123'
d = '100'
print(a, b, c, d)
d, c, a, b = a, b, c, d
print(a, b, c, d)
```

## 2 Operators in Python

### 2.1 Operator Group
Python divides the operators in the following groups:

| Group                           | Operators                                                                                      |
| ------------------------------- | ---------------------------------------------------------------------------------------------- |
| Arithmetic operators    算术      | `+`, `-`, `*`, `/`, `%`, `**`, `//`                                                            |
| Assignment operators     赋值     | `=`, `+= `, `-= `, `*= `, `/= `, `%= `, `//=`, `**=`, `&= `, `\|=`, `^= `, `>>=`, `<<=`, `:= ` |
| Comparison operators    比较      | `==`,`!=`,`>`,`<`,`>=`,`<=`                                                                    |
| Logical operators            逻辑 | `x and y`, `x or y`, `not x`                                                                   |
| Identity operators           is | `is`, `is not`                                                                                 |
| Membership operators   in       | `in`, `not in`                                                                                 |
| Bitwise operators             位 | `&`,`\|`,`^`,`~`,`<<`,`>>`                                                                     |

### 2.2 Operator Precedence

| Precedence | Operators                                                        | Description                                                 | Associativity |
| ---------- | ---------------------------------------------------------------- | ----------------------------------------------------------- | ------------- |
| 1          | `()`                                                             | Parentheses                                                 | Left to right |
| 2          | `x[index], x[index:index]`                                       | Subscription, slicing                                       | Left to right |
| 3          | [`await x`](https://www.geeksforgeeks.org/asyncio-in-python/)    | Await expression                                            | N/A           |
| 4          | `**`                                                             | Exponentiation power                                        | Right to left |
| 5          | `+x`, `-x`, `~x`                                                 | Positive, negative, bitwise NOT                             | Right to left |
| 6          | `*`, `/`,  `//`, `%`                                             | Multiplication, matrix, division, floor division, remainder | Left to right |
| 7          | `+`, `–`                                                         | Addition and subtraction                                    | Left to right |
| 8          | `<<`, `>>`                                                       | Shifts                                                      | Left to right |
| 9          | `&`                                                              | Bitwise AND                                                 | Left to right |
| 10         | `^`                                                              | Bitwise XOR                                                 | Left to right |
| 11         | [\|]()                                                           | Bitwise OR                                                  | Left to right |
| 12         | `in`, `not in`, `is`, `is not`, `<`, `<=`, `>`, `>=`, `!=`, `==` | Comparisons, membership tests, identity tests               | Left to Right |
| 13         | `not x`                                                          | Boolean NOT                                                 | Right to left |
| 14         | `and`                                                            | Boolean AND                                                 | Left to right |
| 15         | `or`                                                             | Boolean OR                                                  | Left to right |
| 16         | `if-else`                                                        | Conditional expression                                      | Right to left |
| 17         | `lambda`                                                         | Lambda expression                                           | N/A           |
| 18         | `:=`                                                             | Assignment expression (walrus operator)                     | Right to left |

### 2.3 Use of Operator

```python
"""
 Arithmetic operators
"""
print(5 / 12)    # 0.4166666666666667
print(5 ** 3)    # 125
print(25 // 12)  # 2      25 / 12 = 2 ······ 1
print(25 % 12)   # 1


"""
 Assignment operators
"""
print(x:=3)     # x = 3  print(x)
```

## 3 Control flow in Python

### 3.1 Branch Structure

```python
"""
if Statements
"""
x = 3
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
```


```python
"""
match 
	switch case like
	Match statements require Python 3.10 or newer
"""
def http_error(status):
    match status:
        case 400 | 401 | 402 | 403: # combine several literals in a single pattern using `|`
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:                     # `_` switch default like, use for else status
            return "Something's wrong with the internet"

class Point:
    x: int
    y: int
def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")
```

### 3.2 Loop Structure

```python
"""
for loop Statements  
range() function:
	* range(x,y) return x .... y-1 iterable object
	* range(y) return 0 .... y-1 iterable object
break, continue keywords
"""
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

# range(3,6) return iterable object 3,4,5
for i in range(3,6):
    print(i)

# break breaks out of the innermost enclosing for or while loop 
for n in range(2, 10):
   for x in range(2, n):
       if n % x == 0:
           print(n, 'equals', x, '*', n//x)
           break
   else:
       print(n, 'is a prime number')

# continue continues with the next iteration of the loop
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)
```

```python
"""
pass statement 
	does nothing
	be used when a statement is required syntactically but the program requires no action
"""
class MyEmptyClass:
    pass

def initlog(*args):
    pass   # Remember to implement this!

for i in range(3,6):
    pass   # Remember to implement this!
```

```python
"""
while loop Statements
"""
total = 0
i = 1
while i <= 100:
    total += i
    i += 1
print(total)
```

### 3.3 Case of Control flow

```python
"""
3.3.1 MAX Prime numbers within 10000
"""
for num in range(10000, 2, -1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
        break
```