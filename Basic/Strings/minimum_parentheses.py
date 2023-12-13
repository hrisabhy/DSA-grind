def minimum_parentheses(str):
    ob, cb = "(", ")"
    # Initialize a stack array to keep track of unclosed opening parentheses
    stack = []
    # Initialize a variable to track the number of closing parentheses
    count_cb = 0

    # Iterate through the input string
    for x in str:
        
        # check if current element is an opening parentheses
        if x  == ob:
            # if yes then push it to the stack
            stack.append(x)
        # If the character is a closing parentheses
        else:
            if len(stack) > 0: # If there is a matching opening parentheses in the stack
                # Remove the last opening parentheses from tthe stack
                stack.pop()
            else:
                # If there is no matching opening parentheses, increment the count of unmatched closing parentheses
                count_cb += 1

    # The total number of parentheses needed is the sum of unmatched closing parentheses and opening parentheses
    return count_cb + len(stack)
print(minimum_parentheses("(()())()((("))