import re
with open(file='row.txt',mode='r',encoding='utf8') as f:
    rowtxt=f.read()
patt='[A-Z]+[a-z]+'
text='erg drg srgEDG eth ERGdfb etgRGeth'
print(re.findall(patt,text))
print(re.findall(patt,rowtxt))