# disini kita punya kumpulan data, yang nanttinya kita akan hitung jumlah masing masing data

# kita tampung data pembelilnya dalam list

pembeli = list()
pembeli = ['freya', 'adel', 'flora', 'freya', 'adel',
           'cristy', 'olla', 'adel', 'adel', 'gracia', 'haruka']

# untuk menghitung hasil siapa yang paling banyak beli kita pakai dictionary
jumlah_akhir = dict()

# kita cek satu persatu namanya menggunakan looping
for key in pembeli:
    # jika keynya ngga ada di jumlah akhir maka masukin ke jumlah akhir
    if key not in jumlah_akhir:
        jumlah_akhir[key] = 1
    else:
      #  jika ada maka keynya di tambah satu
        jumlah_akhir[key] = jumlah_akhir[key] + 1

print(jumlah_akhir)


# CARA SINGKAT
for key in pembeli:
    # jika key nya ngga ada di jumlah akhir maka masukin ke jumlah akhir
    if key not in jumlah_akhir:
       # kalo ada brarti 1, kalo ngga ada brarti 0, 0 nya itu default
        jumlah_akhir[key] = jumlah_akhir.get(key, 0) + 1

print(jumlah_akhir)
