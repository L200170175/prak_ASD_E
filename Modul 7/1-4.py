import re

f = open('Indonesia.txt', 'r', encoding = 'latin1')
teks = f.read()
f.close()

q = open('KEI.html', 'r', encoding = 'latin1')
kei = q.read()
q.close()

#1
pola = r'\s(me\w+)'
cocok = re.findall(pola, teks)
print(cocok)
print(len(cocok), "\n")

#2
pola1 = r'\s(di\w+)'
cocok1 = re.findall(pola1, teks)
print(cocok1)
print(len(cocok1), "\n")

#3
pola2 = r'(di \w+)'
cocok2 = re.findall(pola2, teks)
print(cocok2)
print(len(cocok2), "\n")

#4
pola3 = r'(title="\w+")'
cocok3 = re.findall(pola3, kei)
print(cocok3)
print(len(cocok3), "\n")

pola4 = r'(/wiki/\w+)'
cocok4 = re.findall(pola4, kei)
print(cocok4)
print(len(cocok4), "\n")

pola5 = r'(">\w+</a></td>)'
cocok5 = re.findall(pola5, kei)
print(cocok5)
print(len(cocok5))
=====================================================================
wiki = open('KEI.html', 'r', encoding='latin1')
teks = wiki.read()
wiki.close()

cari = re.findall(r'">([\w+]+)</a></td>\n<td>([0-9.]+)</td>\n<td>([0-9.]+)</td>\n<td>([0-9.]+)</td>\n<td>([0-9.]+)</td>\n<td>([0-9.]+)</td>\n<td>([0-9.]+)</td>', teks)

listbaru = []

for i in cari:
    a = (i[0],float(i[4]))
    listbaru.append(a)

print(listbaru)
