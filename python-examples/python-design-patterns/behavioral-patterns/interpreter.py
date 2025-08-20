"""
Purpose: Define a grammar and interpreter for a language.

Pros:
- Makes it easier to customize or extend the language syntax.
- Provides a way to evaluate sentences in known language.

Cons:
- Complex grammars can be hard to maintain.
- Not efficient for complex languages.

When to use:
- For simple languages or DSLs needing evaluation.
"""
class Expression:
    def interpret(self, context):
        pass

class TerminalExpression(Expression):
    def __init__(self, data):
        self.data = data

    def interpret(self, context):
        return self.data in context

class OrExpression(Expression):
    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2

    def interpret(self, context):
        return self.expr1.interpret(context) or self.expr2.interpret(context)

class AndExpression(Expression):
    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2

    def interpret(self, context):
        return self.expr1.interpret(context) and self.expr2.interpret(context)

# Example
john = TerminalExpression("John")
married = TerminalExpression("Married")
john_and_married = AndExpression(john, married)
print(john_and_married.interpret(["John", "Married"]))
print(john_and_married.interpret(["John"]))
# Output:
# True
# False
