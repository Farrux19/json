import os
os.system("cls")

f = open("1-text","r")
matn = f.read()

ikki = matn.split()
bir = ikki[-1]
uch = ""

for i in range(2):
    uch += bir + " "
print(uch)