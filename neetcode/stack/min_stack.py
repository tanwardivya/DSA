class MinStack:
    def __init__(self)->bool:
        self.stack = []
        self.minstack = [] 

    def push(self, val:int):
        self.stack.append(val)
        val = min(val,self.minstack[-1] if self.minstack else val)# provides the min val either from the minstack if it is empty return the min element from the min stack otherwise give value self.minstack[-1] this means it does not pop the value just see the value and return
        self.minstack.append(val)
    
    def pop(self)->None:
        self.stack.pop()
        self.minstack.pop()
    
    def top(self)->int:
        return self.stack[-1]

    def get_min(self)->int:
        return self.minstack[-1]

def main():
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-1)
    print(min_stack.get_min())
    min_stack.pop()
    print(min_stack.get_min())
    print(min_stack.top())

if __name__ == "__main__":
    main()
