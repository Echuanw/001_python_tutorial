
## 1 Function

### 1.1 Function Describe

```python
# define function
def fib(n):                     # Fibonacci Sequence
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result               # return value

# parameter passing 
print(fib(20))

# Passing functions as arguments
f = fib
print(f(20))

# without a return statement returns `None`
def a(n):
    n = n + 1
print(a(1)) # None
```

### 1.2 Function Parameters

```python
# Set default values ​​for parameters
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    pass
ask_ok('Do')
ask_ok('OK', 2)
ask_ok('OK', 2, 'Come on')
```

```python
# Default values are evaluated only once
i = 5
def f(arg=i):
    print(arg)
i = 6
f()    # 5
```

```python
# When the default value is a mutable object like a list, dictionary, or class instance, it retains the computed value
	# Pass object address
def f(a, L=[]):
    L.append(a)
    return L
print(f(1))  # [1]
print(f(2))  # [1, 2]
print(f(3))  # [1, 2, 3]
```

```python
# Parameters with (*) :  add 0 or more parameters
def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))
```

```python
# dict as parameter, use ** tag
def test(**input_dict):
    for k, v in input_dict.items():
        print(k, v)
```

```python
# must specify the variable name when passing parameters
def kwd_only_arg(*, arg):
    print(arg)
kwd_only_arg(arg=3)  # must !!!
```

### 1.3 functions as parameters

```python
"""
func as parameter，time_record()，be used for caculate func running time
"""
import time as t
def time_record(func, n, a, x): 
    start = t.perf_counter_ns()
    func(n,a,x)
    end = t.perf_counter_ns()
    time_spend = end - start
    return print(time_spend)
    
def mutinomial(n,a,x):
    p = 0
    for i in range(0,n+1):
        p += a[i]*pow(x,i)
    return print(p)

def qinjiushao(n,a,x):
    p = a[n]
    for i in range(n,0,-1):
        p *= x
        p += a[i-1]
    return print(p)

if __name__ == '__main__':
    n = 3
    a = [2,1,3,4]
    x = 2.2
    time_record(mutinomial,n,a,x)
    time_record(qinjiushao,n,a,x)
```

```python
"""
function as return value
"""
def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
        　　ax = ax + n
        return ax
    return sum

f = lazy_sum(1,2,3,4,5)
print f    # <function sum at 0x02657770>
    # lazy_sum(1,2,3,4,5)返回的是一个指向求和的函数的函数名。
    # 在调用lazy_sum(1,2,3,4,5)的时候，不立刻求和，而是根据后面代码的需要在计算。
print f()   # 15   用f()调用求和函数，计算出结果。

f1 = lazy_sum(1,2,3,4,5,6)
f2 = lazy_sum(1,2,3,4,5,6)
print f1 == f2    # False  每次调用，都返回一个新的函数对象。

# 闭包中局部变量的使用
def count():
　　fs = []
　　for i in range(1,4):
　　　　def f():
　　　　　　return i*i  
　　　　fs.append(f)
　　return fs      # 返回的fs中的元素f函数引用了变量i，不是闭包，所以会发生改变
f1, f2, f3 = count() 
print f1()   # 9
print f2()   # 9
print f3()   # 9
```

### 1.4 Lambda Expressions

Lambda Expressions as some small anonymous functions,  they are just syntactic sugar for a normal function definition.

```python
# lambda Expressions As Return value
def make_incrementor(n):
    return lambda x: x + n
plusFive = make_incrementor(5)  # plusFive = lambda x: x+5
print(plusFive(4))              # 9
print(make_incrementor(4)(6))   # 10
    # # it likes scala Closure:
	# def make_incrementor(n)(x):
	#     return n + x
	# # plusFive = make_incrementor(5) just like:
	# def plusFive(x):
	#     return 5 + x
	
```

```python
# lambda Expressions As Return Parameter
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])                       # sort key is second col
pairs                                                      # [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
```

## 2 module & package

The project is developed by a team of **multiple people**, there have **defined same functions named**. 
So how to solve this naming conflict? The answer is actually very simple. 
**Each file in Python represents a module.** We can have functions with the same name in different modules. 
When using functions, we `import`can distinguish which ones to use by importing the specified module with keywords. 

#### 2.1 Use module management functions

`s004_sample_module1.py`
```python
def foo():
    print('hello, world!')
```

`s004_sample_module2.py`
```python
def foo():
    print('goodbye, world!')
```

```python
"""test1"""
from s004_sample_module1 import foo
foo()  # out hello, world!

from s004_sample_module2 import foo
foo()  # out goodbye, world!
```

```python
"""test2"""
# the later imported overwrites the previously imported
from s004_sample_module1 import foo
from s004_sample_module2 import foo
foo() # out goodbye, world!
```

### 2.2 `__name__`

Python interpreter will execute codes when importing this module.
* shen a module is run directly, the value of `__name__` is `'__main__'`; 
* when the module is imported by another module, the value of `__name__` is the name of the module.
So we can use `__name__` control running code.

`s004_sample_module3.py`
```python
def foo():
    pass

def bar():
    pass

# Only the name of the module that is directly executed by the Python interpreter is `__main__`
if __name__ == '__main__':
    print('call foo()')
    foo()
    print('call bar()')
    bar()
```

```python
"""test3"""
import s004_sample_module3
```

### 2.3 部分导入& 重命名
```python
>>> from fibo import fib
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

>>> import fibo as fib
>>> fib.fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

>>> from fibo import fib as fibonacci
>>> fibonacci(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

### 2.4 脚本执行模块
```python
# 执行
python fibo.py <arguments>

# 执行了module中的这部分内容
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
```
### 2.5 dir()
函数列出所有类型的名称：变量、模块、函数等
```python
>>> import fibo
>>> dir(fibo)
['__name__', 'fib', 'fib2']
```
### 2.6 Package
```python
# 包类似于 Java Package 
from sound.effects import echo  # 导入包里的模块
from sound.effects.echo import echofilter  # 导入模块里的函数
```
