# Efficient Pair Removal from Strings: Two Approaches

## Solution 1:- Using str.replace()

### Intuition
- Continuously remove pairs "AB" and "CD" from the string until no more pairs can be found.

### Approach
1. Loop until no "AB" or "CD" is found in the string.
2. Use `str.replace()` to remove all occurrences of "AB" or "CD".
3. Return the length of the modified string.

### Complexity
- #### Time complexity:
    - ___O(n * m)___: Where _n_ is the string length and _m_ is the number of times pairs can be found and replaced.

- #### Space complexity:
    - ___O(n)___: A new string is created for each replacement.

### Code
```python3 []
class Solution:
    def minLength(self, s: str) -> int:
        # Indicates whether it's the first iteration of the loop
        first_Time = True
        # This flag checks if any "AB" or "CD" has been found in the string
        does_AB_or_CD_Found = False

        # Continue the loop until no "AB" or "CD" is found
        while first_Time or does_AB_or_CD_Found:
            first_Time = False  # Set first_Time to False after the first loop iteration
            
            # Check for "AB" in the string
            if "AB" in s:
                does_AB_or_CD_Found = True  # Set the flag to True since we've found "AB"
                s = s.replace('AB', '')  # Replace all occurrences of "AB" with an empty string
            
            # Check for "CD" in the string
            elif "CD" in s:
                does_AB_or_CD_Found = True  # Set the flag to True since we've found "CD"
                s = s.replace('CD', '')  # Replace all occurrences of "CD" with an empty string
            else:
                does_AB_or_CD_Found = False  # If neither "AB" nor "CD" is found, set the flag to False

        # Return the length of the modified string
        return len(s)

# Time Complexity: O(n * m), where n is the length of the string and m is the number of times "AB" or "CD" can be found and replaced.
# In the worst case, if the string keeps getting modified with replacements, we might need to traverse it multiple times.
# Space Complexity: O(n), where n is the length of the final string, since a new string is created with each replacement.
```
## Solution 2:- Using Stack Approach
### Intuition
- Use a stack to keep track of characters and efficiently remove pairs as they are encountered.

### Approach
1. Traverse each character in the string.
2. If the current character forms a pair with the top of the stack ("AB" or "CD"), pop the stack.
3. Otherwise, push the character onto the stack.
4. Return the length of the stack as the modified string length.

### Complexity
- #### Time complexity:
    - ___O(n)___: Each character is processed once.

- #### Space complexity:
    - ___O(n)___: The stack may store all characters in the worst case.

### Code
```python3 []
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
```