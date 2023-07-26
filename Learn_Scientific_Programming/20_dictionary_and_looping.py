import re

print('Please type a text ...')
text = input()
if '.txt' in text:
    hand = open(text)
    hand = hand.read()
else:
    hand = text
# phara = hand.rstrip()
# line = phara.split()
count = dict()
# menggunakan RegEx untuk memisahkan kalimat \s cocok untuk karakter spasi newline dan tab
for word in re.split(r'\s', hand):
    if word not in count:
        count[word] = 1
    else:
        count[word] = count[word] + 1

for nama, nilai in count.items():
    print(nama, 'jumlahnya : ' + str(nilai))
