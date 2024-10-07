class Solution:
    def minLength(self, s: str) -> int:
        # Initialize an empty stack to keep track of characters
        stack = []
        
        # Iterate through each character in the input string
        for character in s:
            # If the stack is empty, just add the current character
            if len(stack) == 0:
                stack.append(character)
                continue

            # Check if the current character forms "AB" with the top of the stack
            if character == 'B' and stack[-1] == 'A':
                stack.pop()  # Remove the 'A' from the stack, effectively removing "AB"
            # Check if the current character forms "CD" with the top of the stack
            elif character == 'D' and stack[-1] == 'C':
                stack.pop()  # Remove the 'C' from the stack, effectively removing "CD"
            else:
                stack.append(character)  # If no pair is found, add the current character to the stack
        
        # Return the length of the remaining characters in the stack
        return len(stack)

# Time Complexity: O(n)
# The loop iterates through the string once, and each character is pushed or popped from the stack at most once.

# Space Complexity: O(n)
# In the worst case, where no "AB" or "CD" pairs are found, the stack could store all characters from the input string.