import re
reg=r"[^А-я \n]"

y=[]
N=[]
count1=0
count2=0
start=open('text.txt','r',encoding='utf-8')
finish=open('text1.txt','w',encoding='utf-8')
for n,line in enumerate(start):
    print('Text:',line)
    count = sum(map(lambda x : 1 if ',' in x else 0, line))
    if re.findall(reg,line) and count>1:
        count1+=1

        finish.write('Содержит:{}'.format(line))
        y.append(n)
    else:
        count2+=1
        finish.write('Не содержит:{}'.format(line))
        N.append(n)
print('Содержит ошибку строчек',count1,'Не содержит ошибку строчек',count2)
start.close()
finish.close()


