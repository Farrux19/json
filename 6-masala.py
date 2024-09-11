import os
os.system("cls")

a = input("FAYL nomi:  ")
lis = list(i for i in a if i.isalpha())

f = open("New.1.txt","w")
lis.sort(reverse=True)
f.write(' '.join(lis))

f.close()

f1 = open("New.2.txt","w")
lis.sort()
f1.write(' '.join(lis))

f1.close()