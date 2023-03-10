import re
text='setrYglkbluLlbgliuGligliGlhguhglhjGuydYgbSD'
patt='[A-Z]{1}[a-z0-9]*'
words=re.findall(patt,text)
a=''
for i in words:
    a+=i+' '
print(a)