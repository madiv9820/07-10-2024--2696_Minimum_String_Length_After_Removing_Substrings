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