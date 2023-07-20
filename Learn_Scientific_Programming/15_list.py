daftar_buah = ['Pisang', 'Apel', 'Anggur', 'Jambu Kristal', 'Mangga']
# daftar_buah[0] = 'Stoberi'
# print(range(len(daftar_buah)))
# for buah in daftar_buah:
#     print('Saya jual buah', buah)

for i in range(len(daftar_buah)):
    try:
        i = i + 1
        buah = daftar_buah[i]
    except:
        exit()
    print('Saya jual buah', buah)
