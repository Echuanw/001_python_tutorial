## 1 OOP

### 1.1 Define class and use

```python
"""
define class 
__init__  : used to init when creat instances
"""
class Student(object):
	"""A simple student class"""   # Myclass.__doc__
	
	identity = "student"           # Class variable

    # init : bind two attributes: name and age
    # first parameter is self
    def __init__(self, name, age):   
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s is learning %s.' % (self.name, course_name))

    def watch_movie(self):
        if self.age < 18:
            print('%s is watching movie.' % self.name)
        else:
            print('%s is watching cartoon.' % self.name)
```

```python
"""
use class create instance
"""
def main():
    stu1 = Student('echuan', 38)    # create student instance
    # stu do study job
    stu1.study('Python Design')
    # stu do watch movie job
    stu1.watch_movie()
    stu2 = Student('echo', 15)
    stu2.study('Mind')
    stu2.watch_movie()

if __name__ == '__main__':
    main()
```

### 1.2 Nonlocal & Global

```python
"""
    local   : defined inside the function
    nonlocal: defined outside the function, but it's not a global var. so if it changed, it means modity outside local var.
    global  : scope spans the entire module.to use a variable inside a function, need to use the global declaration
"""
print("#####LOCAL TEST######:")
def local_test():
    def do_local():
        spam = "local spam in do_local() function"  # do_local()'s local spam, can't access out of do_local()
    spam = "local spam"
    do_local()                           # local variable in function can't access out of scope
    print("After local assignment:", spam) # local spam
local_test()


print("\r\n#####NONLOCAL TEST######:")
def nonlocal_test():
    def do_nonlocal():
        nonlocal spam                        # defined outside the do_nonlocal(), but is not a global var
        spam = "nonlocal spam in do_nonlocal() function"
    spam = "local spam"                      # if outside var not exists, raise Error
    do_nonlocal()                            # do_nonlocal() use outside var, so outside var changed
    print("After nonlocal assignment:", spam)# nonlocal spam in function
nonlocal_test()


print("\r\n#####GLOBAL TEST######:")
def global_test():
    def do_local():
        spam = "local spam in do_local()" 
    def do_nonlocal():
        nonlocal spam  
        spam = "nonlocal spam in do_nonlocal()"
    def do_global():
        global spam                          # use global mean it's global var
        spam = "global spam in do_global()"
    spam = "local spam"
    do_local()                                
    print("After local assignment:", spam)    # local spam
    do_nonlocal()                             
    print("After nonlocal assignment:", spam) # nonlocal spam in function
    do_global()     
    print("After global assignment:", spam)   # this spam isn't global var, it's local var

global_test()
print("In global scope:", spam)  # global spam in function
```

### 1.3 Access issue

We usually **set the properties of the object to private** or protected, which simply means that **external access is not allowed**, and the methods of the object are usually public ( public), because public methods are messages that the object can accept. 
In Python, there are only **two access permissions** for attributes and methods, namely **public and private**. 
If you want the attribute to be private, you can **start the attribute with two underscores** when naming it.


```python
"""
python has two access permission
	* public
	* private, start the attribute with two underscores
"""
class Test:
    def __init__(self, foo):        # private __foo attribute
        self.__foo = foo

    def __bar(self):                # private __bar method
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')            # private attribute can init ,but can not read by default way
    # test.__bar()                    # AttributeError: 'Test' object has no attribute '__bar'
    print(test.__foo)               # AttributeError: 'Test' object has no attribute '__foo'

if __name__ == "__main__":
    main()
```

Python just **changes the name of private properties and methods** to hinder access to them. In fact, if you know the rules for changing names, you can still access them.

```python
"""
access private attribute and method by change name
For reference only.
"""
class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')
    test._Test__bar()                  # special way to access private attribute and method
    print(test._Test__foo)


if __name__ == "__main__":
    main()
```

### 1.4 @property decorator and `__slots__`

`@property`: we do **not recommend** **setting attributes as private**, there are **problems** if the attributes are **directly exposed to the outside world**.
* Our previous **suggestion** was to name the properties **starting with a single underscore**. It just a **Implication**, you also can access the properties py its name when you know them.
* but we still recommend using the **@property** to wrap the getter and setter methods to make access to the properties safe and convenient

`__slots__` : if we need to limit the custom type object to only be bound to certain attributes, we can limit it by defining the __slots__ variable in the class
* Python is a dynamic languages, so a instance can use `obj.attribute = xxx` to create many properties. so we use `__slots__` to limit properties.

```python
class Person(object):

    # the `Person` object to only bind the specied : _name, _age, _gender
    __slots__ = ('_name', '_age', '_gender')
    
	# use single underscore
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # wap getter method
    @property
    def name(self):                  # use : obj.name 
        return self._name
    @name.setter
    def name(self, name):            # use : obj.name = 'xxx'
        self._name = name
    
    # wap getter method
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, age):
        self._age = age
	
    def play(self):
        if self._age <= 16:
            print(f'{self._name} is {self._age} years old and now he is playing Flying Chess .')
        else:
            print(f'{self._name} is {self._age} years old and not he is playing Cards.')

def main():
    person = Person('王大锤', 22)
    person.play()
    person._name = '王二觉'    # we still can access properties by them name   
    person._age = 15    
    person.play()
    person.name = '王大锤'      # but we use @property, can be more safe and convenient
    person.age = 22     
    person.play()
    # person._is_gay = True    # After __slots__ Setting, raise AttributeError: 'Person' object has no attribute '_is_gay'

if __name__ == '__main__':
    main()
```

### 1.5 Static methods and class methods

* Static methods
	* use `@staticmethod` decorator to mark a method，Similar to tools methods, with no class parameter.
	* can called by Class or Instance
* Class methods
	* use `@classmethod` decorator to mark a method. Receives the class as the first parameter, usually named `cls`. It can access and modify the class's state.(like modify class variable)
	* can called by Class or Instance

```python
"""
Static methods
    * Similar to tools methods
    * no class parameter
"""
from math import sqrt

class Triangle(object):            

    __slots__ = ('_a', '_b', '_c')
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) *
                    (half - self._b) * (half - self._c))

def main():
    a, b, c = 3, 4, 5
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        print(t.perimeter())
        print(t.area())
    else:
        print('无法构成三角形.')
if __name__ == '__main__':
    main()
```

```python
"""
Class methods
"""
from time import time, localtime, sleep

class Clock(object):
    """Digit Clock"""

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """show oclock"""
        return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)

def main():
    # Create an instance through a class method and get the system time
    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()

if __name__ == '__main__':
    main()
```

### 1.6 Relationship between classes

In object-oriented programming, class is a blueprint for objects that we want to create. One class can be related to another class or not. Generally, there are some relations between classes in oop, which are :

- Aggregation   (**has-a**)
	- two objects where each object can exist without another object.
	- For example, the relationship between employee and department. An employee can stand alone without a department, so does the department.
	- ![400](assets/note_image/image-20240902173017250.png)
- Composition   (**has-a**)
	- between classes where both classes are dependent on each other.
	- For example, the relation between Laptop and its Processor. A laptop cannot exist without its processor.
	- ![400](assets/note_image/image-20240902173200606.png)
- Inheritance   (**Is-a**)
	- between classes where parent class is a general class and child class is a specific class.
	- For example, the relation between cat, dog, and its general class, which is animal.
	- ![400](assets/note_image/image-20240902173207028.png)

![600](assets/note_image/image-20240902185831174.png)

### 1.7 Encapsulation

Hide all implementation details that can be hidden, and only expose simple programming interfaces to the outside world.

After we create the object, we only need to send a message (call the method) to the object to execute the code in the method. That is to say, we You only need to know the name of the method and the parameters passed in (the external view of the method), but do not need to know the implementation details inside the method (the internal view of the method).

### 1.8 Inheritance and Polymorphism

* Inheritance
	*  Let subclass ingerit properties and methods directly from super class.
* Polymorphism
	* After inheriting the methods of parent class, subclass can implement a new version of these method.(Method Overwride)We call this method different subclass objects will showdifferent behaviors.


```python
from abc import ABCMeta, abstractmethod

# create a abstract class, can't create instance
class Pet(object, metaclass=ABCMeta):
    """宠物"""
    def __init__(self, nickname):
        self._nickname = nickname
    @abstractmethod         # abstract method, subclass need overwrite
    def make_voice(self):
        """发出声音"""
        pass

# Inheritance syntax:  subclass(superclass)
class Dog(Pet):
    """狗"""
    def make_voice(self):
        print('%s: 汪汪汪...' % self._nickname)


class Cat(Pet):
    """猫"""
    def make_voice(self):
        print('%s: 喵...喵...' % self._nickname)

def main():
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()

if __name__ == '__main__':
    main()
```


```python
"""
Inheritance 
"""
# Single
class DerivedClassName(modname.BaseClassName):
	pass

# Mutiple
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
```
### 1.9 dataclass

maybe it used to connect data for database

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


