import re
with open(file='row.txt',mode='r',encoding='utf8') as f:
    rowtxt=f.read()
patt='[a-z]+[_]'
text='srtgrtg srghsrhrth rghrhr rtghrgd_ rthtKKV_'
print(re.findall(patt,text))
print(re.findall(patt,rowtxt))