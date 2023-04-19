import docx
import os
paths = []
folder = os.getcwd()
for root, dirs, files in os.walk(folder):
    for file in files:
        if file.endswith('docx') and not file.startswith('~'):
            paths.append(os.path.join(root, file))
for path in paths:
    doc = docx.Document('1.docx')
text = []
text2=[]
text3=[]
l=0
for paragraph in doc.paragraphs:
    te=text.append(paragraph.text)
    
    for i in text[l]:
        text2.append(i)
       
    l=l+1
print('\n'.join(text))
print('текст=',text2)
print('длина=',len(text2))
print('Символ=',chr(769))

d = [i for i, ltr in enumerate(text2) if ltr == '́']
print('Позиция секретных символов',d)
for o in d:
    
    o=int(o)
    o=o-1
    print('Позиция буквы:',o)
    mes=text2[o]
    text3.append(mes)
mes1=(''.join(text3))
print('Секоетное сообщение:',mes1)





