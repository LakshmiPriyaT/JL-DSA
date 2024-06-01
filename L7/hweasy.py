def infix_to_postfix(infix_expr):
  """Converts infix expression to postfix notation using a stack.

  Args:
      infix_expr: The infix expression string.

  Returns:
      The postfix expression string.
  """
  precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
  stack = []
  postfix = []

  for char in infix_expr:
    if char.isdigit():
      postfix.append(char)  # Append operands directly
    elif char == '(':
      stack.append(char)  # Push opening parenthesis onto stack
    elif char == ')':
      while stack and stack[-1] != '(':
        postfix.append(stack.pop())  # Pop operators until encountering '('
      stack.pop()  # Pop the '(' itself
    else:
      while stack and precedence[char] <= precedence[stack[-1]]:
        postfix.append(stack.pop())  # Pop operators with higher or equal precedence
      stack.append(char)  # Push current operator onto stack

  while stack:
    postfix.append(stack.pop())  # Append remaining operators

  return ''.join(postfix)

# Example usage
infix_expression = input("Enter an infix expression (e.g., 2 + 3 * 4): ")
postfix_expression = infix_to_postfix(infix_expression)
print("Postfix expression:", postfix_expression)