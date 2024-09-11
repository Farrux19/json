import os
os.system("cls")

a = input("FAYL nomi:  ")
lis = list(a)

f = open("new1.txt","w")
lis.sort(reverse=True)
f.write(' '.join(lis))#join metodi listni elementlarini birlashtiradi va yagona satr qiladi

f.close()

f1 = open("new2.txt","w")
lis.sort()
f1.write(' '.join(lis))

f1.close()