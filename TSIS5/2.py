import re
with open(file='row.txt',mode='r',encoding='utf8') as f:
    rowtxt=f.read()
patt='ab{3}'
text='hello lll jbbhj bjhb lbl bhl b abbb ergaeg'
print(re.search(patt,text)[0])
print(re.search(patt,rowtxt))