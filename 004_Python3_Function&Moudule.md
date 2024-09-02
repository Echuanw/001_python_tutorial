
## 1 Function

#### 1 函数概述

```python
# 函数 def 定义，函数体必须缩进
def fib(n):    # 斐波那契数列
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    return result   # return 返回值

# 函数传参
fib(20)

# 函数作为参数传递
f = fib
f(20)

# 没有 return 语句的函数也返回值，是 None
def a(n):
	n = n + 1
print(a(1)) # None
```

#### 4.2 函数的参数

```python
# 参数设置默认值，传参时可以不传有默认值的参数
def ask_ok(prompt, retries=4, reminder='Please try again!'):
	pass
ask_ok('Do')
ask_ok('OK', 2)
ask_ok('OK', 2, 'Come on')


# 默认值只计算一次
i = 5
def f(arg=i):
    print(arg)
i = 6
f()    # 5

# 默认值为列表、字典或类实例等可变对象时，会保留计算过的值
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))  # [1]
print(f(2))  # [1, 2]
print(f(3))  # [1, 2, 3]

# 可变数量的实参, 有若干个普通参数
def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))

# 字典作为参数
def test(**input_dict):
	for k, v in input_dict.items():
	    print(k, v)

# 位置限制参数，/ 前后位置不能变
def foo(name, /, **kwds):
   return 'name' in kwds

# 实名限制传参， * 必须指定变量名才能传参
def kwd_only_arg(*, arg):
    print(arg)
kwd_only_arg(arg=3)  # 必须这么传
```
#### 4.3 函数作为参数，返回值

```python
import time as t
# 函数 func 作为参数传入，time_record函数，用来计算func的计算时间
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

# 函数作为返回值
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

#### 4.4 lambda函数
语法上，匿名函数只能是单个表达式。语义上，它只是常规函数定义的语法糖。
```python
# lambda 表达式 作为返回值
def make_incrementor(n):
    return lambda x: x + n
plusFive = make_incrementor(5)  # plusFive = lambda x: x+5
print(plusFive(4))              # 9

# lambda 表达式的函数体最好只写单行

# lambda 表达式 作为参数
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])    # 排序键为第二列
pairs # [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
```

## 6、module & package

模块是包含 Python 定义和语句的文件。就是工具python文件
import 语句 _第一次_ 遇到模块名时执行

#### 6.1 基本导入

```python
# Fibonacci numbers module NAMED fibo.py
def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
```

```python
# 其他文件使用 fibo.py 中定义的语句
>>> import fibo
>>> fibo.fib(1000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987

>>> fibo.__name__
'fibo'
```

#### 6.2 部分导入& 重命名
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

#### 6.3 脚本执行模块
```python
# 执行
python fibo.py <arguments>

# 执行了module中的这部分内容
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
```
#### 6.4 dir()函数
函数列出所有类型的名称：变量、模块、函数等
```python
>>> import fibo
>>> dir(fibo)
['__name__', 'fib', 'fib2']
```
#### 6.5 包
```python
# 包类似于 Java Package 
from sound.effects import echo  # 导入包里的模块
from sound.effects.echo import echofilter  # 导入模块里的函数
```

## 7、输入输出格式化

### 7.1 格式化字符串
```python
# 变量格式化输出字符串,在字符串开头的引号/三引号前添加 `f` 或 `F`
# 控制长度，小数长度，添加其余字符 {变量:整数长度.小数长度[其余字符]}
>>> year = 2016
>>> event = 'Referendum'
>>> f'Results of the {year:10} {event:15}'
'Results of the 2016       Referendum     '

# 0填充  zfill(含符号和小数点的总长度)
>>> '12'.zfill(5)
'00012'
>>> '-3.14'.zfill(7)
'-003.14'

#  格式化字符串 str.format() 
>>> yes_votes = 42_572_654
>>> no_votes = 43_132_495
>>> percentage = yes_votes / (yes_votes + no_votes)
>>> '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
' 42572654 YES votes  49.67%'
# str.format() 格式化字面值
>>> import math
>>> print(f'The value of pi is approximately {math.pi:.3f}.')
The value of pi is approximately 3.142.
# str.format() 控制位置
>>> print('{0} and {1}'.format('spam', 'eggs'))
spam and eggs
>>> print('{1} and {0}'.format('spam', 'eggs'))
eggs and spam

# 直接变成字符串
>>> s = 'Hello, world.'
>>> str(s)
'Hello, world.'
>>> repr(s)
"'Hello, world.'"
>>> str(1/7)
'0.14285714285714285'
```

```python
# 字典格式化
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```

### 7.2 读写文件
```python
# 读文件  open() 返回一个 file object
# with open(filename, mode, encoding=None)
	# with : 即使发生异常文档也能正常关闭，没有要使用f.close()关闭文档
	# mode : w 只写入  a 打开文件追加  r+ 进行读写  省略 r 只读
	#        b 以二进制模式读取： 如 wb rb rb+
	# encoding 建议 "utf-8"
with open('workfile', encoding="utf-8") as f:
    read_data = f.read()

# f.read(size)   size 个字符（文本）或 size 个字节（二进制）
# f.readline()  读一行
# f.write(string or binary)  写入字符串
```
### 7.3 json读写
json 相对于普通text，可以区分数字类型
```python
# JSON文件必须以UTF-8编码
>>> import json
>>> x = [1, 'simple', 'list']
>>> json.dumps(x)       # 将json对象序列化保存为 text file
'[1, "simple", "list"]' 
```
## 8、异常

### 8.1 异常处理
```python
import sys
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
finally:
    print('Goodbye, world!')  # finally 同 Java
```
### 8.2 主动出发异常
```python
# 向上传递异常
def func():
    raise ConnectionError 
    
try:
    func()
except ConnectionError as exc:
    raise RuntimeError('Failed to open database') from exc
```
## 9、类
### 9.1 作用域和命名空间
```python
# nonlocal & global
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()                             # 普通的不会改变对象
    print("After local assignment:", spam) # test spam
    do_nonlocal()                          # nonlocal 会改变对象
    print("After nonlocal assignment:", spam) # nonlocal span
    do_global()                            # global 会改变全局对象，作用域中有时不会影响
    print("After global assignment:", spam) # nonlocal spam

scope_test()
print("In global scope:", spam)  # global spam
```
### 9.2 类定义
```python
# MyClass.i & MyClass.f 可以引用或赋值
class MyClass:
    """A simple example class"""   # Myclass.__doc__
    i = 12345
    def f(self):
        return 'hello world'
    def __init__(self, realpart, imagpart):  # 对象定义方法
        self.r = realpart
        self.i = imagpart

# 创建对象
x = MyClass(1,2)



# 方法的第一个参数常常被命名为 `self`。 这是一个约定
class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []    # create empty list for each dog
    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks
['roll over']
>>> e.tricks
['play dead']
```
### 9.3 数据类
```python
# dataclass 注解
from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    dept: str
    salary: int

>>>

>>> john = Employee('john', 'computer lab', 1000)
>>> john.dept
'computer lab'
>>> john.salary
1000
```
### 9.4 继承
```python
# 继承
class DerivedClassName(modname.BaseClassName):
	pass

# 多继承
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
```
### 9.5 变量
```python
# 自定义私有变量  __变量名  在类里会自动变为 _ClassName__变量名
# MappingSubclass 使用 update() 就是自己的方法，使用 __init__就是Mapping的updata()方法
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)
    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)
    __update = update   # private copy of original update()

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
```
### 9.6 迭代器 & 生成器
```python
#  for in 遍历底层调用的都是迭代器，需要用的时候官网
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end='')

# 迭代器 iterator : 
mytuple = ("apple","banana","cherry")
myit = iter(mytuple)                # iter() 将 元组变成一个迭代器
print(next(myit))                   # 使用 next() 可以一致访问迭代器的下一个元素
print(next(myit))
print(next(myit))
print(next(myit))                   # 报错

# 迭代器遍历
myit = iter(("apple","banana","cherry"))
for i in myit:
	print(i)

# 返回有限元素的迭代器元素个数，最快的方法
len(list(myit))

# 生成器 yield ，用于返回一个迭代器
def reverse(data):
    for index in range(data, -1, -1):
        yield index                       
# 使用推导式实现上述 reverse(data)
lambda x : (yield data[index] for index in range(len(x) -1 , -1, -1))

for char in reverse('golf'):
    print(char)  # f l o g

# 生成器表达式   类似列表推导式，只是由()包含，一般直接用于外部函数
sum(i*i for i in range(10))               # sum 285
data = 'golf'
list(data[i] for i in range(len(data)-1, -1, -1)) # ['f', 'l', 'o', 'g']
```
## 10、python 标准库
### 10.1 os & shutil 模块
```python
# os 模块，与操作系统交互
>>>import os
>>> os.getcwd()      # current working directory
'C:\\Python311'
>>> os.chdir('/server/accesslogs')   # Change working directory
>>> os.system('mkdir today')   #  mkdir in the system shell
0
>>> dir(os)
<returns a list of all module functions>
>>> help(os)
<returns an extensive manual page created from the module's docstrings>

# shutil 更高级的处理日常文件和目录管理任务
>>> import shutil
>>> shutil.copyfile('data.db', 'archive.db')
'archive.db'
>>> shutil.move('/build/executables', 'installdir')
'installdir'
```
### 10.2 glob 文件通配符
```python
# 在目录中使用通配符搜索创建文件列表
>>> import glob
>>> glob.glob('*.py') 
['primes.py', 'random.py', 'quote.py']
```
### 10.3 sys & [argparse](https://docs.python.org/3/howto/argparse.html) 处理命令行参数
```python
# 命令行参数作为列表存储在 sys 模块的 _argv_ 属性中
>>> import sys
>>> print(sys.argv)  
['demo.py', 'one', 'two', 'three']

# argparse 处理命令行参数
import argparse
parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)

# python top.py --lines=5 alpha.txt beta.txt
# args.lines 设为 5
# args.filenames 设为 ['alpha.txt', 'beta.txt']
```
### 10.4 [re](https://docs.python.org/zh-cn/3.11/library/re.html#module-re) 正则表达式工具
```python
>>> import re
>>> re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
['foot', 'fell', 'fastest']
>>> re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
'cat in the hat'
```
### 10.5 math & random & statistics
```python
# math 数学函数，cos log 等
import math
math.cos(math.pi / 4)

# random 随机选择
>>> import random
>>> random.choice(['apple', 'pear', 'banana'])  # 多选一
'apple'
>>> random.sample(range(100), 10)   # 随机抽10个数
[30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
>>> random.random()                 # 随机 0 - 1小数
0.17970987693706186
>>> random.randrange(6)             # 固定范围随机整数
4

# statistics  基本统计属性（均值，中位数，方差等）
>>> import statistics
>>> data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
>>> statistics.mean(data)   # 均值
1.6071428571428572
>>> statistics.median(data)  
1.25
>>> statistics.variance(data)
1.3720238095238095
```
### 10.6 互联网访问
 [`urllib.request`](https://docs.python.org/zh-cn/3.11/library/urllib.request.html#module-urllib.request "urllib.request: Extensible library for opening URLs.") 用于从URL检索数据
 [`smtplib`](https://docs.python.org/zh-cn/3.11/library/smtplib.html#module-smtplib "smtplib: SMTP protocol client (requires sockets).") 用于发送邮件

### 10.7 时间日期
```python
# datetime 模块提供了以简单和复杂的方式操作日期和时间的类
>>> from datetime import date
>>> now = date.today()
>>> now
datetime.date(2003, 12, 2)
>>> now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
'12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'

>>> # dates support calendar arithmetic
>>> birthday = date(1964, 7, 31)
>>> age = now - birthday
>>> age.days
14368
```

```python
import datetime as dt
######################################## date形式天数差
d1 = '2019-07-26'
d2 = '2020-08-01'
######## 法1
# （1）字符串-->时间格式date
date1 = dt.datetime.strptime(d1, "%Y-%m-%d").date()  ##datetime.date(2018, 1, 6)
print(date1)

#  (2) date 加减
date2 = date1 - dt.timedelta(days=1)
print(date2)
```


## 11、Python脚本
#### 11.1 可执行脚本
* 在BSD等类Unix系统上，Python脚本可以直接执行，就像shell脚本一样
```python
#!/usr/bin/env python3.5
```
使用 **chmod** 命令为脚本提供可执行模式或权限。
```shell
chmod +x myscript.py
```

#### 11.3 定制模块
Python提供了两个钩子来让你自定义它：`sitecustomize` 和 `usercustomize`。要查看其工作原理，首先需要找到用户site-packages目录的位置。
```python
>>> import site
>>> site.getusersitepackages()
'/home/user/.local/lib/python3.5/site-packages'
```
您可以在该目录中创建一个名为 `usercustomize.py` 的文件，并将所需内容放入其中。它会影响Python的每次启动，除非它以 [`-s`](https://docs.python.org/zh-cn/3.11/using/cmdline.html#cmdoption-s) 选项启动，以禁用自动导入。

`sitecustomize` 以相同的方式工作，但通常由计算机管理员在全局 site-packages 目录中创建，并在 `usercustomize` 之前被导入。有关详情请参阅 [`site`](https://docs.python.org/zh-cn/3.11/library/site.html#module-site "site: Module responsible for site-specific configuration.") 模块的文档。

## 12、关键字

### assert Keyword
```python
x = "hello"  
#if condition returns True, then nothing happens:  
assert x == "hello"  
#if condition returns False, AssertionError is raised:  
assert x == "goodbye"
```

