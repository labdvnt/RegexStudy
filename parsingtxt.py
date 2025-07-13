
import re

with open('words.txt', 'r') as f:
    words = f.read().splitlines()

#print(words)

#Task1 İçinde karar geçenler
for line in words:
    pattern = 'kara'
    match = re.search(pattern, line)
    if match:
        print(line)

print('------------------------------------------------')

#Task2 Başında kara geçenler '^'

for i in words:
    pattern = '^kara'
    match = re.search(pattern, i)
    if match:
        print(i)
print('------------------------------------------------')

#Task3 sonunda kara geçenler '$'

for p in words:
    pattern = 'kara$'
    match = re.search(pattern, p)
    if match:
        print(p)

print('------------------------------------------------')

#Task4 sadece kara olan başında veya sonunda bir şey olmasın 

for p in words:
    pattern = '^kara$'
    match = re.search(pattern, p)
    if match:
        print(p)
print(f'Sadece kara olanlar:{pattern} bulunamadı')


print('------------------------------------------------')

#Task5
#. any character örneğin '.kara' karadan önce herhangi birşey olabilir ama olmalı,  'kara.' karadan sonra herhangi bir şey olsun ama olmalı
# '.kara.' karadan önce ve sonra herhangi bir şey ve herhangi bir sayıda olabilir ama olmalı
#kara satirin ortasinda olsun. kara'dan önce ve kara'dan sonra  karekter limiti olmasin

for t in words:
    pattern = '.kara.'
    match = re.search(pattern, t)
    if match:
        print(t)

print('------------------------------------------------')

#Task6
# kara'dan önce sadece 2 karekter olsun. kara'dan sonra sadece 2 karekter olsun.
#'^..kara..$' burada '^..kara' demek anlamı karadan önce .. iki tane herhangi bir şey ^ bunlada bitiş başka bir şey gelmesin demek 
#'^..kara..$' burada 'kara..$' demek anlamı karadan önce .. iki tane herhangi bir şey $ bunlada bitiş başka bir şey gelmesin demek 
for f in words:
    pattern = '^..kara..$'
    match = re.match(pattern, f)
    if match:
        print(f)

print('------------------------------------------------')

#Task6
#Sadece k ile başlayıp r ile bitsin 

for f in words:
    pattern = '^kr$'
    match = re.match(pattern, f)
    if match:
        print(f)

print('------------------------------------------------')


#Task7
#Sadece k ile başlayıp r ile bitsin ortada sadece 1 karekte olsun

for f in words:
    pattern = '^k.r$'
    match = re.match(pattern, f)
    if match:
        print(f)

print('------------------------------------------------')

#Task8
#Sadece k ile başlayıp r ile bitsin ortada sadece 2 karekte olsun

for f in words:
    pattern = '^k..r$'
    match = re.match(pattern, f)
    if match:
        print(f)

print('------------------------------------------------')

#Task9
#Sadece k ile başlayıp r ile bitsin ortada sadece 3 karekte olsun

for f in words:
    pattern = '^k...r$'
    match = re.match(pattern, f)
    if match:
        print(f)

print('------------------------------------------------')


#Task10
#Sadece k ile başlayıp r ile bitsin ortada sadece 4 karekte olsun

for f in words:
    pattern = '^k....r$'
    match = re.match(pattern, f)
    if match:
        print(f)

print('------------------------------------------------')

#Task11
#Sadece k ile başlayıp r ile bitsin ortada sadece 5 karekte olsun

for f in words:
    pattern = '^k.....r$'
    match = re.match(pattern, f)
    if match:
        print(f)

print('------------------------------------------------')

#Task12
#Sadece k ile başlayıp r ile bitsin ortada sadece 12 karekte olsun

for f in words:
    pattern = '^k............r$'
    match = re.match(pattern, f)
    if match:
        print(f)

print('------------------------------------------------')


#Task13
#Sadece k ile başlayıp r ile bitsin ortada sadece 13 karekte olsun 
#burada 13 tane . yazmak zor olacak bunun yerine kaçtane oldugunu {} parentez içine yazarak da yapabiliriz

for f in words:
    pattern = '^k.{13}r$'
    match = re.match(pattern, f)
    if match:
        print(f)

print('------------------------------------------------')

#Task14
#Sadece k ile başlayıp r ile bitsin ortada sadece 13 , 14 , 15 , 16, 16, 18 karekter olsun 
#burada 13 tane . yazmak zor olacak bunun yerine kaçtane oldugunu {13,18} parentez içine yazarak da yapabiliriz bu da 13 ile 18 arası demek

for f in words:
    pattern = '^k.{13,18}r$'
    match = re.match(pattern, f)
    if match:
        print(f)

print('------------------------------------------------')