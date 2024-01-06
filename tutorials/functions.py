# Type of functions

# 
"""
1. Function without parameter without return
2. Function with parameter without return
3. Function without parameter with return
4. Function with parameter with return
"""

def abcd():
    print('Function without parameter without return')

def abc(x):
    print('Function with parameter without return')
    print(x)

def wxyz():
    print('Function without parameter with return')
    return 4

def xyz(x):
    print('Function with parameter with return')
    return x

def main():
    abcd()
    abc(4)
    result = wxyz()
    print(result)
    result = xyz(9)
    print(result)

if __name__ == '__main__':
    main()