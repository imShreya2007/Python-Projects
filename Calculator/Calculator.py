import ast
import operator

print("Calculator....")
print("Type 'exit' to quit.")
print("Supported operators: +  -  *  /  %  **  ( )")

# Allowed operators mapping
allowed_operators = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow
}

def evaluate_expression(expr):
    def eval_node(node):
        if isinstance(node, ast.Constant):  # numbers
            return node.value
        elif isinstance(node, ast.BinOp):  # operations
            op_type = type(node.op)
            if op_type in allowed_operators:
                return allowed_operators[op_type](
                    eval_node(node.left),
                    eval_node(node.right)
                )
            else:
                raise ValueError("Unsupported operator")
        else:
            raise ValueError("Invalid expression")

    parsed = ast.parse(expr, mode='eval')
    return eval_node(parsed.body)

while True:
    expression = input("\nEnter Your Calculation: ").strip()

    if expression.lower() == 'exit':
        print("Goodbye!")
        break

    try:
        result = evaluate_expression(expression)
        print("Result:", result)
    except Exception:
        print("Invalid expression. Please try again.")
