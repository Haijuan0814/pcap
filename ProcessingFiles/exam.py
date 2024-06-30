

from datetime import datetime
d1 = datetime(2019,11,2,11,27,22)
d2 = datetime(2019,11,2,0,0,0)
#print(d1 -d2)


import sys
#print(sys.path)
#print(dir())

import math
# Initialize the number of items to choose from
n = 7
# Initialize the number of possibilities to choose
k = 1
# Print total number of possible combinations
##print (math.comb(n, k))#
#print (math.sqrt(13))
#print (math.isqrt(13))

# ----------------------------------------
class MyClass:
    pass

obj = MyClass()
print(obj.__class__.__name__)   # 输出: MyClass，对象的类名
print(obj.__module__)


import my_module
obj2 = my_module.MyClass1()
print(obj2.__module__)
print(obj2.__class__.__name__)
#print(__name__)

# ----------------------------------------
def f(x):
    try:
        x=x/x
    except:
        print('a' , end = '')
    else:
        print('b' , end = '')
    finally:
        print('c' , end = '')

f(1)
f(0)

print('\n')
print('\n')
# ----------------------------------------
class A:
    def __str__(self):
        return 'a'
class B():
    def __str__(self):
        return 'b' 
class C(A , B):
    pass
o = C()
print(o)

print('\n')


# ----------------------------------------
class Ex(Exception):
    def __init__(self , msg):
        Exception.__init__(self , msg + msg)
        self.args = (msg,'hhh')

try:
    raise Ex('ex')
except Ex as e:
    print(e)
    print("Exception args:", e.args)
except (ValueError, TypeError):
    print('xxxx')
except Exception as e:
    print(e)


List1= [False for i in range(1,10)] 
list2 = List1[-1:1:-1]
print(list2)
    


def fun(x, y, z):
    return x + 2 * y + 3 * z
 
 
print(fun(0, z=1, y=3))

print(1,0,2,3,4,5)


temps = [[0.0 for h in range(24)] for d in range(31)]
highest = -100.0
 
for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp
 
print("The highest temperature was:", highest)

for i in range(1):
    print("#")
else:
    print("#")



nums = [1, 2, 3]
vals = nums
del vals[1:2]

print(nums)
print(vals)
print('\n')

# ----------------------------------------
t = [[3-i for i in range (3)] for j in range (3)]
print(t)
 
my_list = [1, 2, 3, 4]
print(my_list[-3:-2])



d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}
 
for item in (d1, d2):
    print(item)

colors = (("green", "#008000"), ("blue", "#0000FF"))

colors_dictionary = dict(colors)
print(colors_dictionary)


my_list = [1, 2]
 
for v in range(2):
    my_list.insert(-1, my_list[v])
 
print(my_list)


my_list = [10, 8, 6, 4, 2]
new_list = my_list[:]
print(new_list)
new_list = my_list[1:]
print(new_list)
new_list = my_list[1::]
print(new_list)
new_list = my_list[:-1]
print(new_list)
new_list = my_list[::-1]
print(new_list)


s1 = 'Where are the snows of yesteryear?'
s2 = s1.split()
s3 = sorted(s2)
print(s3[1])


i = 250
while len(str(i)) > 72:
    i *= 2
else:
    i //=2
print(i)
 

lst = [[c for c in range(r)] for r in range(3)]
print(lst)


from random import randint
for i in range(10):
    print(randint(1,5))




x = 5 
f = lambda x:1+2
print(f(x))

x = 5//2
func = lambda x:+3
print(func(x))

my_l = [[i+j for i in range(1,5,1)] for j in range(-1,6,3)]
print(my_l)


def myfunc(n):
    res = ord('A')
    for i in range(0,n,2):
        yield chr(res)
        res+=2
 
y = [x for x in myfunc(10)]
 
print(y)