#Метелкина Таисия, БКЛ-153.
import re

name = 'new.txt'

def first(name): 
    f = open (name, 'r', encoding = 'utf-8')
    string = f.read()
    f.close()
    regex = '[А-ЯЁ]\. [А-ЯЁ][А-ЯЁа-яё-]+' 
    name_1 = re.findall (regex, string)
    if name != None:
        for element in name_1:
            print (element) # 1 задание
            
def second (name):
    f = open (name, 'r', encoding = 'utf-8')
    string = f.read()
    f.close()
    name_2 = re.findall ('[А-ЯЁ](?:\.|[а-яё-]+)(?: )?(?:[А-ЯЁ]\. )?[А-ЯЁ][А-Яа-яё-]+', string)
    if name_2 != None:
        for element in name_2:
            print (element) #2 задание

def main():
    val1 = first (name)
    val2 = second (name)
    
if __name__ == '__main__' :
    main()
