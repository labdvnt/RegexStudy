# Star Wars Epsiode 3
# Revenge Of The Stih

#starwars3.txt

#Senaryoda ki boşlukları temizle
#tum satirlarin uzunluklarini cikar
#en uzun satir kacinci sirada ve icinde ne yaziyor


with open('starwars3.txt','r',encoding='utf-8') as f:
    SW=f.read().splitlines()

#print(SW)

#print(SW[0])
#Senaryoda ki boşlukları temizle 
print(f'Boşluklar temizlenmeden önce uzunluk: {len(SW)}')
while '' in SW:
    SW.remove('')
    
print(f'Boşluklar temizlenmeden önce uzunluk: {len(SW)}')

#Senaryoda ki boşlukları temizle OK




#Tum satirlarin uzunluklarini cikar

number = 0
lenght= []
for i in SW:
    lenght.append(len(i))
#    print(f'{number}. satirin uzunlugu: {len(i)} = {i}')
    number += 1
#print(lenght)

#Tum satirlarin uzunluklarini cikar OK

#en uzun satir kacinci sirada ve icinde ne yaziyor

en_uzun_satır = lenght.index(max(lenght))

print(max(lenght))
print(lenght.index(max(lenght)))
print(SW[en_uzun_satır])









