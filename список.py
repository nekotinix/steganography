
original_list = ['python', 'programming']
new_list = []
spisok3=[]
code='11111111'
for word in original_list:
    new_word = ''
    for letter in word:
        new_letter = '0' # заменяем букву на её верхний регистр
        new_word += new_letter # добавляем измененную букву в новое слово
    new_list.append(new_word)

print(new_list) # Output: ['PYTHON', 'PROGRAMMING'
for i in range(len(new_list)):
    for j in range(len(new_list[i])):
        print('dlina v elemente spiska',len(new_list[i]))
        print('text',new_list[i][j])
        spisok3.append(len(new_list[i]))
print(spisok3)
x=list(dict.fromkeys(spisok3))
print(x)


