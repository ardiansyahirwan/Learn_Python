print('Please type a text ...')
text = input()
if '.txt' in text:
    hand = open(text)
    hand = hand.read()
else:
    hand = text
phara = hand.rstrip()
line = phara.split()
count = dict()
for word in line:
    if word not in count:
        count[word] = 1
    else:
        count[word] = count[word] + 1

print(count)
