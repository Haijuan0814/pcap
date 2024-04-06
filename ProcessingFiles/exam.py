

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
