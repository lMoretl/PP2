import re
with open(file='row.txt',mode='r',encoding='utf8') as f:
    rowtxt=f.read()
text='gdht srhh srth. srth'
print(re.sub('[,\.\s]',':',text))
print(re.sub('[,\.\s]',':',rowtxt))