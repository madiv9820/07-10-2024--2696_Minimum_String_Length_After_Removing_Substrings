# 2696. Minimum String Length After Removing Substrings

__Type:__ Easy <br>
__Topics:__ String, Stack, Simulation <br>
__Companies:__ J.P. Morgan, Yelp <br>
__LeetCode Link:__ [Minimum String Length After Removing Substrings](https://leetcode.com/problems/minimum-string-length-after-removing-substrings/description/)
<hr>

### Question

You are given a string `s` consisting only of __uppercase__ English letters.<br><br>
You can apply some operations to this string where, in one operation, you can remove __any__ occurrence of one of the substrings `"AB"` or `"CD"` from `s`.<br><br>
Return _the ___minimum___ possible length of the resulting string that you can obtain_.<br><br>
__Note__ that the string concatenates after removing the substring and could produce new `"AB"` or `"CD"` substrings.
<hr>

### Examples

__Example 1:__

__Input:__ s = "ABFCACDB" <br>
__Output:__ 2 <br>
__Explanation:__ We can do the following operations: <br>
- Remove the substring "ABFCACDB", so s = "FCACDB".
- Remove the substring "FCACDB", so s = "FCAB".
- Remove the substring "FCAB", so s = "FC".

So the resulting length of the string is 2.<br>
It can be shown that it is the minimum length that we can obtain.

__Example 2:__

__Input:__ s = "ACBBD" <br>
__Output:__ 5 <br>
__Explanation:__ We cannot do any operations on the string so the length remains the same.
<hr>

### Constraints:

- `1 <= s.length <= 100`
- `s` consists only of uppercase English letters.
<hr>

### Hints:

- Can we use brute force to solve the problem?
- Repeatedly traverse the string to find and remove the substrings “AB” and “CD” until no more occurrences exist.