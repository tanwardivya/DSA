from collections import deque

def valid_parentheses_collections(string:str)->bool:
    stack = deque()
    for parenthesis in string:
        if parenthesis == "(":
            stack.append(")")
        elif parenthesis == "{":
            stack.append("}")
        elif parenthesis == "[":
            stack.append("]")
        elif len(stack) == 0 or stack.pop() != parenthesis:
            return False
    return len(stack) == 0

def main():
    string = "(]"
    result = valid_parentheses_collections(string)
    print(result)
    string2 = "()[]{}"
    result2 = valid_parentheses_collections(string2)
    print(result2)

if __name__ == "__main__":
    main()

