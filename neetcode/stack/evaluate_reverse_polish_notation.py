class EvaluateReversePolishNotation:
    def evaluate_reverese_polish_notation(self,tokens:list[str])->int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(c))
        return stack[0]

def main():
    tokens = ["2","1","+","3","*"]
    evaluator = EvaluateReversePolishNotation()
    result = evaluator.evaluate_reverese_polish_notation(tokens)
    print(result)


if __name__ == "__main__":
    main()
