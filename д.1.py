# С клавиатуры вводятся поочередно N слов.  Напишите программу, которая соединяет эти слова в одну длинную строку,
# разделяя слова пробелами. Используйте операторы цикла.

stroka=[]
#N=int(imput())
i=True
while i!='stop':
    i=input()
    if i!='stop': stroka.append(i)
word = ' '.join(stroka)
print(word)