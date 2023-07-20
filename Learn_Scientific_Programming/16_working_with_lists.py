daftar_buah = ['Pisang', 'Apel', 'Anggur', 'Jambu Kristal', 'Mangga']

# menggabungkan lists menggunakan "+"
buah_impor = ["Peach", "Pomegranete", "Kiwi"]
daftar_buah = daftar_buah + buah_impor

# potong atau slice lists menggunakan " : "
# contoh kita ingin mengambil buah apel dan anggur
daftar_buah = daftar_buah[1:3]

# gunakan dir() untuk mengetahui daftar commands dari tipe data yang kita gunakan
# append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort
dir(daftar_buah)

# Append
# menambahkan data di akhir list
daftar_buah.append('Ayam')

# clear
# menghapus semua yang ada di dalam list
daftar_buah.clear()
daftar_buah.append('water melon')


# cek apakah ada data yang kita cari di list tersebut
cek = 'water melon' in daftar_buah
print(cek)

daftar_buah.append('apel')
daftar_buah.append('manggis')

# menyortir list sesuai abjad gunakan perintah sort()
daftar_buah.sort()
print(daftar_buah)

# Build in functiom in List
# len() jumlah atau panjang list
print(len(daftar_buah))

# max() nilai tertinggi dalam lists
angka = [34, 20, 56, 70, 34, 88, 89, 100]
print(max(angka))

# min() nilai terkecil dalam lists
angka.append(15)
print(min(angka))

# sum() jumlah keseluruhan nilai dalam list
print(sum(angka))

# sum(angka) / len(angka) untuk mencari average atau rata-rata
print(sum(angka) / len(angka))
