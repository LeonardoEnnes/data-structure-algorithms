'''
Link: https://leetcode.com/problems/reverse-words-in-a-string-iii/description/

557. Reverse Words in a String III
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:
Input: s = "Mr Ding"
Output: "rM gniD"
 
Constraints:
- 1 <= s.length <= 5 * 104
- s contains printable ASCII characters.
- s does not contain any leading or trailing spaces.
- There is at least one word in s.
- All the words in s are separated by a single space
'''

def reverseWords(s):
    response = ''
    l, r = 0, 0

    while r < len(s):
        if s[r] != ' ':
            r += 1
        else:
            response += s[l:r+1][::-1]
            r += 1
            l = r 

    response += ' '
    response += s[l:r + 2][::-1]
    return response[1:]

print(reverseWords("Let's take LeetCode contest"))