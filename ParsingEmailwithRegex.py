import re


#email.txt dosyasini listeye donustur

with open('email.txt') as f:
    email=f.read().splitlines()
#print(len(email))

#her satiri gor listede
#for line in email:
#    print(line)

#her satiridaki emailleri listele
emailler1=[]
for t in email:
    pattern = r"([.\w-]+)(@)([.\w-]+)"
    match=re.search(pattern,t)
    if match:
        emailler1.append(match.group(0))
print(emailler1)