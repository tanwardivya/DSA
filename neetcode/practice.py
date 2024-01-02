from collections import defaultdict
from collections import Counter
#List = [1, 2,  3, "GFG", 2.3]
#print(List)

# Defining the dictictionary
#d = defaultdict(int)
     
#L = [1, 2, 3, 4, 2, 4, 1, 2,5.5,"gd"]
     
# Iterate through the list for keeping the count
#for i in L:
         
    # The default value is 0
    # so there is no need to
    # enter the key first
    #d[i] += 1
         
#print(d[1])

#defining a counter with sequence of items
# count = Counter(['B', 'B', 'A', 'B', 'C', 'A', 'B', 'B', 'A', 'C'])
# print(count)
# #with dictionary
# count.update({'A' : 1}) 
# print(count)


def method1():
    global variable1
    variable1 = "hi"
    print(variable1)

def method2():
    variable1 = "HELLO"
    print(variable1)

method1()
method2()
# print(variable1)

class ABC:
    # All variables are called class variable if they are defined with self.
    # Within the class if you have to call class variable and method it should be called using self.
    def __init__(self, x, y) -> None:
        self.a = x
        self.b = y
        
    def method1(self, a, b):
        x = 7
        y = 8
        print(a,b) #Local variable
        print(self.a, self.b) #Class Variable
    
    def method2(self, a, b):
        self.method1(a=a, b= b) #Call class method 
    
    def method3(a, b):
        print(a,b)

    def __eq__(self, __value: object) -> bool:
        return isinstance(__value, ABC) and __value.a == self.a and __value.b == self.b

array = [[1,3],[3,4], [2,1], [0,9]] 



#How to access method1
abc1 = ABC(x=4, y=5) #Class ABC constructor require two parameter x, y 
a = 2
b = 3
abc1.method1(a=a,b=b)
abc2 = ABC(x=4, y=5) 
if abc1 == abc2:
    print(True)
abc2.method1(a=a,b=b)
abc2.method2(a,b)
# abc.method1(b=b, a=a)
# abc.method1(2,3)
