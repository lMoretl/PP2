import re
text='setrYglkbluLlbgliuGligliGlhguhglhjGuydYgb'
patt='[A-Z]{1}[a-z0-9]*'
words=re.findall(patt,text)
print(words)