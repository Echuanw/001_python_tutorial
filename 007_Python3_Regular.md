## 7、输入输出格式化


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
