import os
os.system("cls")

f =open("3-text", "r")
matn = f.read()
    
son = ''
son1 = ''
for i in matn:
    if i.isdigit():
        son1 += i
    elif son1:
        son += son1 + '+'
        son1 = ''
        
son += son1
print(son)