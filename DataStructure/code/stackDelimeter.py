# Stack ADT implementation
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if not self.is_empty() else None

    def peek(self):
        return self.items[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# Balanced Delimiter Checker with detailed comments
class DelimiterMatcher:
    def __init__(self):
        # Mapping of closing brackets to their corresponding opening brackets
        self.pairs = {')': '(', '}': '{', ']': '['}

    def is_matching(self, code_string):
        # Create an empty stack to hold opening brackets
        stack = Stack()

        # Traverse each character in the input string
        for char in code_string:
            if char in "([{":
                stack.push(char)
            elif char in ")]}":
                # Step 1: If the stack is empty, there's no opening bracket
                if stack.is_empty():
                    return False
                # Step 2: Pop the last opening bracket from the stack
                top = stack.pop()
                # Step 3: Get the expected matching opening bracket
                expected_opening = self.pairs[char]
                # Step 4: Compare the popped bracket with the expected one
                if top != expected_opening:
                    return False  # Mismatch found
        # Step 5: After processing all characters, if the stack is empty, all brackets matched correctly
        return stack.is_empty()


# Prefix to Postfix Converter
class PrefixToPostfixConverter:
    def __init__(self):
        pass

    def is_operand(self, ch):
        return ch.isalpha() or ch.isdigit()

    def convert(self, prefix_expr):
        stack = Stack()
        for char in reversed(prefix_expr):
            if self.is_operand(char):
                stack.push(char)
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                new_expr = op1 + op2 + char
                stack.push(new_expr)
        return stack.pop()


# Example Usage

def main():
    # Test DelimiterMatcher
    match = DelimiterMatcher()
    c_code = """
    #include <stdio.h>
    int main(){
        int a=10;
        if (a>5){
            printf("hello");
        } else {
            printf("Bye");
        }
        return 0;
    }
    """
    print("Delimiter check (C code):", "Balanced" if match.is_matching(c_code) else "Not Balanced")

    expr1 = "{[()()]}"
    print("Delimiter check ({[()()]}):", "Balanced" if match.is_matching(expr1) else "Not Balanced")

    expr2 = "(())()"
    print("Delimiter check ((())()):", "Balanced" if match.is_matching(expr2) else "Not Balanced")

    expr3 = "{[(])}"
    print("Delimiter check ({[(])}):", "Balanced" if match.is_matching(expr3) else "Not Balanced")

    # Test PrefixToPostfixConverter
    converter = PrefixToPostfixConverter()
    prefix_expr = "*+AB-CD"
    postfix_expr = converter.convert(prefix_expr)
    print("\nPrefix expression:", prefix_expr)
    print("Converted Postfix expression:", postfix_expr)


# Run the main function
if __name__ == "__main__":
    main()
