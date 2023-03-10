import re
import string
text='setrYglkbluLlbgliuGligliGlhguhglhjGuydYgbSD'
patt='[A-Z]{1}[a-z0-9]*'
words=re.findall(patt,text)
a=''
print(len(words))
for  i in words:
    if i != words[len(words)-1]:
        a+=i.lower()+'_'
    else:
        a+=i.lower()
print(a)