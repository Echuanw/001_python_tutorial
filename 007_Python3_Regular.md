
> re reference : [re module & Regular Expression](https://docs.python.org/3/library/re.html#)

## 1 Metacharacters

### 1.1 basic character

```sql
--    " . " : Match any single character, exclude "\r\n"                                            
--    " * " : Match many of the preceding expression；0 or any number
--   " () " : Group the regular expression within the parentheses
--    " \ " : 转义符，"\n"匹配换行符。序列"\\"匹配"\"，"\("匹配"("。                        \. 或 \* \? \+ 都需要转义
--    " ? " : Match zero or one of the preceding expression, e.g. "do(es)?" can match "do" or "does"
--    " + " : Match one or many of the preceding expression, e.g. "zo+" can match "zo" or "zoo", but can not match "Z+"

--  " xyz " : 占位n，表示字符集合
--  " x|y " : 占位1，匹配表达式x或y

--   序列"\\"匹配"\"
--   " \s " : 匹配空格
--   " \r " : 匹配一个回车符。等效于 \x0d 和 \cM。
--   " \n " : 换行符匹配。等效于 \x0a 和 \cJ。
--   " \f " : 换页符匹配。等效于 \x0c 和 \cL。
--   " \t " : 制表符匹配。与 \x09 和 \cI 等效。
--   " \v " : 垂直制表符匹配。与 \x0b 和 \cK 等效。
```



### 1.2 字符组[]

```sql
-- " [xyz] " : Match any character enclosed in the brackets,    占位1，匹配x, y, z中的一个
--" [^xyz] " : Match any character not enclosed in the brackets,占位1，不是xyz集合中的字符就行
-- " [a-z] " : 占位1，区间，匹配a至z范围的字符
```

### 1.3 repeat times

```sql
--   " {n} " : 匹配前面表达式n次
-- " {n,m} " : 最少匹配n次且最多匹配m次,m不写表示无穷次数
```

### 1.4 WDS

```sql
--     序列"\\"匹配"\"
--    " \d " : 匹配数字，等价于[0-9]
--    " \D " : 匹配非数字，等价于[^\d]
--    " \w " : 匹配任意字母数字，等价于[a-zA-Z0-9]
--    " \W " : 匹配非字母数字，等价于[^\w]
--    " \s " : 匹配空白字符，等价于[\t\r\n\f\v],注意其中包含空格
--    " \S " : 匹配非空白字符，等价于[^\s]
```

### 1.6 边界

```sql
--    " \b " : 匹配一个字边界，即字与空格间的位置。 \W 为边界，没有字符也算 [^a-zA-Z0-9]
```

### 1.7 start and end

```sql
--     " $ " : Matches the end of the string，edf$
--     " ^ " : Matches the start of the string，^abc
```

## 2 greedy mode

* `'*'`，`'+'`，`'?'`  are all **greedy**; they match as much text as possible.
* Adding `"?"` after a quantifier makes it a **non-greedy** (or lazy) quantifier.

```sh
{m,n}?
{m,}?
??
*?
+? 
```


## 3 Use of Regular Expression

Python provides the `re` module to support regular expression related operations. The following are the core functions in the re module.

| function                                     | illustrate                                                                                                                                                       |
| -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `compile(pattern, flags=0)`                  | Compiling a regular expression returns a regular expression object                                                                                               |
| `match(pattern, string, flags=0)`            | Matches a string with a regular expression and returns the matching object if successful, otherwise None is returned.                                            |
| `search(pattern, string, flags=0)`           | The first occurrence of the regular expression pattern in the search string returns a matching object successfully, otherwise None is returned.                  |
| split(pattern, string, maxsplit=0, flags=0)  | Split string with pattern delimiter specified by regular expression return list                                                                                  |
| sub(pattern, repl, string, count=0, flags=0) | Use the specified string to replace the pattern matching the regular expression in the original string. You can use count to specify the number of replacements. |
| fullmatch(pattern, string, flags=0)          | The exact match (from the beginning to the end of the string) version of the match function                                                                      |
| `findall(pattern, string, flags=0)`          | Finds all patterns in a string that match a regular expression and returns a list of strings                                                                     |
| `finditer(pattern, string, flags=0)`         | Finds all patterns in a string that match a regular expression and returns an iterator                                                                           |
| purge()                                      | Clear cache of implicitly compiled regular expressions                                                                                                           |
| re.I / re.IGNORECASE                         | Ignore case matching tags                                                                                                                                        |
| re.M / re.MULTILINE                          | multi-line match tag                                                                                                                                             |

> **Note:** These functions in the re module mentioned above can also be replaced by regular expression objects in actual development. If a regular expression needs to be used repeatedly, then compile the regular expression through the compile function first. Formula and create a regular expression object is undoubtedly a wiser choice.

Below we will tell you how to use regular expressions in Python through a series of examples.

### 3.1 re and match object

```python
"""
    regular rxpression object can call function without parttern
"""
import re
text = "Hello, welcome to Python."
re_obj = re.compile(r'(Hello), (welcome)')
match = re_obj.search(text)
if match:
    print("Full match:", match.group())     # output: Full match: Hello, welcome
    print("Full match:", match.group(0))     # output: Full match: Hello, welcome
    print("Full match:", match.group(1))     # output: Full match: Hello
    print("Full match:", match.group(2))     # output: Full match: welcome
```

The match object is the result object. When you use methods like `re.match()`, `re.search()`, or `re.finditer()` to find matches, the returned object is a match object.

```python
"""
* match.group()        : return Full match
* match.group(num)     : return group match, group 0 return full match.
* match.start()        : return Start index
* match.end()          : return End index
* match.span()         : return Span
"""
import re

text = "Python is great, and Python is easy to learn."
match = re.search(r'Python', text)
if match:
    print("Matched text:", match.group())   # output: Matched text: Python
    print("Start index:", match.start())    # output: Start index: 0
    print("End index:", match.end())        # output: End index: 6
    print("Span:", match.span())            # output: Span: (0, 6)
```

### 3.2 Find 

* `re.search(pattern, string)`         find the first occurrence of a string or return None
* `re.findall(pattern, string)`        return list composited by all match string 
* `re.finditer(pattern, string)`        return iterator composited by all match string 

```python
"""
 `re.search(pattern, string)`         find the first occurrence of a string or return None
"""
import re

text = "Hello, welcome to the world of Python."
match = re.search(r'Python', text)

if match:
    print("Found:", match.group())  # 输出: Found: Python
else:
    print("Not found.")
```

```python
"""
re.findall(pattern, string)       # return list composited by all match string 
"""
import re

text = "The rain in Spain stays mainly in the plain."
matches = re.findall(r'in ', text)
print("Matches found:", matches)   # 输出: Matches found: ['in ', 'in ', 'in ', 'in ']
```

```python
"""
re.finditer(pattern, string)       # return iterator composited by all match string 
"""
import re

text = "The rain in Spain stays mainly in the plain."
matches = re.finditer(r'in', text)

for match in matches:
    print("Match found at index:", match.start())  #  Match found at index: 6 ....
```


### 3.3 Match

* `re.match(r'regular_expression', string)`
* `re_obj.match(string)`

```python
"""
Vaildate username and password is vaild and provide corresponding prompt messages
- **Username**: Must consist of letters, digits, or underscores, and have a length of 6 to 20 characters.
- **password**: Must be a 5 to 12 digit number, with the first digit not being 0.
"""
import re

def main():
    username = input('please input username: ')
    passwd = input('please input passwd: ')
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)       # use re.match(pattern, string)
    if not m1:
        print('please input vaild username.')
    re_obj = re.compile(r'^[1-9]\d{4,11}$')                # use re_obj.match(string), last is equivalent to this
    m2 = re_obj.match(passwd)
    if not m2:
        print('please input vaild passwd.')
    if m1 and m2:
        print('you input is vaild !!!')

if __name__ == '__main__':
    main()
```

### 3.4 Split

* `re.split(pattern, string)`   split string by pattern, return list 

```python
"""
`re.split(pattern, string)`   split string by pattern, return list 
"""
import re

def main():
    poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
    sentence_list = re.split(r'[，。, .]', poem)
    print(sentence_list)                           # ['窗前明月光', '疑是地上霜', '举头望明月', '低头思故乡','']
    while '' in sentence_list:
        sentence_list.remove('')
    print(sentence_list)                           # ['窗前明月光', '疑是地上霜', '举头望明月', '低头思故乡']


if __name__ == '__main__':
    main()
```

### 3.5 Replace

* `re.sub(pattern, replace_word, modify_string)`      Replace parts of a string that match a regular expression pattern.

```python
"""
`re.sub()`      Replace parts of a string that match a regular expression pattern.
"""
import re

def main():
    sentence = '你丫是傻B吗? 我操你大爷的. Fuck you.'
    purified = re.sub('[操肏艹]|fuck|shit|傻[B比屄逼叉缺吊屌]|煞笔',
                      '*', sentence, flags=re.IGNORECASE)  #  flags=re.IGNORECASE 不区分大小写
    print(purified)  # 你丫是*吗? 我*你大爷的. * you.

if __name__ == '__main__':
    main()
```


### 3.6 group

* `match(r'()', string)`

```python
import re
text = "Hello, welcome to Python."
re_obj = re.compile(r'(Hello), (welcome)')
match = re_obj.search(text)
if match:
    print("Full match:", match.group())     # output: Full match: Hello, welcome
    print("Full match:", match.group(0))     # output: Full match: Hello, welcome
    print("Full match:", match.group(1))     # output: Full match: Hello
    print("Full match:", match.group(2))     # output: Full match: welcome
```