# split() digunakan untuk memisahkan list
words = 'His e-mail is q-lar@freecodecamp.org'
pieces = words.split()

# kita dapat melakukan looping untuk melihat kata yang sudah di pisah
# for word in pieces:
#     print(word)

pieces_third = pieces[3]
print(pieces_third)

# dari kata yang kita pisah, kita dapat memisahkannya menjadi lebih kecil lagi dengan memberikan parameter pada split
email = pieces_third.split('-')
print(email[1])
