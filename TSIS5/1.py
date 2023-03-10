import re
with open (file='row.txt',mode='r',encoding='utf8') as f:
    rowtxt = f.read()
patt='a[b]*'
text='egt sgt etg ad abbbbbbbbb ab egegeg egergeg efefaf etgrthrth'
print(re.findall(patt,text))
print(re.findall(patt,rowtxt))