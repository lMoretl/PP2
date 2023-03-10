import re
with open(file='row.txt',mode='r',encoding='utf8') as f:
    rowtxt=f.read()
patt='a.*?b'
text='erg drg srgEDG eth ERGdfb etgRGeth wrergagwsfgdsfb argRGb'
print(re.findall(patt,text))
print(re.findall(patt,rowtxt))