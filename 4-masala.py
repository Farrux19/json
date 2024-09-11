import os
os.system("cls")

f = open("2-text","r")
matn = f.read()
uch = 0
for i in matn:
    if i.isdigit():
        uch += 1
print(uch)