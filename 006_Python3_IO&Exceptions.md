## 1 Dir Operation


## 2 File Operation

### 1.1 File description

we often encounter scenarios where data is [persisted](https://baike.baidu.com/item/%E6%95%B0%E6%8D%AE%E6%8C%81%E4%B9%85%E5%8C%96) , and the most direct and simple way to achieve data persistence is to save the data to a file.

| operating mode | specific meaning                                                   |
| -------------- | ------------------------------------------------------------------ |
| `'r'`          | read (default)                                                     |
| `'w'`          | Write (the previous content will be truncated first)               |
| `'x'`          | Writing, an exception will be generated if the file already exists |
| `'a'`          | Append, writes content to the end of an existing file              |
| `'b'`          | binary mode                                                        |
| `'t'`          | text mode (default)                                                |
| `'+'`          | Update (can both read and write)                                   |

![](assets/note_image/image-20240902193324693.png)

### 1.2 Read and write text files

```python
"""
Read text files
"""
import time

def main():
    # read total file
    with open('致橡树.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    # for_in loop read
    with open('致橡树.txt', mode='r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()

    # read by line 
    with open('致橡树.txt') as f:
        lines = f.readlines()
    print(lines)
    

if __name__ == '__main__':
    main()
```

### 1.3 Read and write binary files

```python
"""
read image file by read and write binary 
"""
def main():
    try:
        with open('guido.jpg', 'rb') as fs1:
            data = fs1.read()
            print(type(data))  # <class 'bytes'>
        with open('吉多.jpg', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('指定的文件无法打开.')
    except IOError as e:
        print('读写文件时出现错误.')
    print('程序执行结束.')


if __name__ == '__main__':
    main()
```

### 1.4 Read and write JSON files

| JSON                | Python       |
| ------------------- | ------------ |
| object              | dict         |
| array               | list         |
| string              | str          |
| number (int / real) | int / float  |
| true / false        | True / False |
| null                | None         |

|Python|JSON|
|---|---|
|dict|object|
|list, tuple|array|
|str|string|
|int, float, int- & float-derived Enums|number|
|True / False|true / false|
|None|null|



```python
"""
use json module in Python to save the dictionary or list to a file in JSON format.
"""
import json


def main():
    mydict = {
        'name': '骆昊',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('保存数据完成!')


if __name__ == '__main__':
    main()

```

The json module mainly has four important functions, namely:

- `dump`- Serialize Python objects into files in JSON format
- `dumps`- Process Python objects into JSON-formatted strings
- `load`- Deserialize JSON data in the file into objects
- `loads`- Deserialize the contents of the string into a Python object



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

### 10.2 glob 文件通配符
```python
# 在目录中使用通配符搜索创建文件列表
>>> import glob
>>> glob.glob('*.py') 
['primes.py', 'random.py', 'quote.py']
```