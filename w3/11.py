#Write a Python function that checks whether a word or phrase is palindrome or not. Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam
def palindrome(s):
    left = 0
    right = len(s) - 1
    while left <= right:
        if not s[left] == s[right]:
            return False
        left += 1
        right -= 1
    return True


s = str(input())
print(palindrome(s))