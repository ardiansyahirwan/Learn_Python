# kondisional dalam python tidak menggunakan tanda bukan kurung seperti dalam bahasa pemrograman lain, akan tetapi diakhiri dengan titik dua dan ada indentasinya
makan = input('sudah makan ? (Y/N) ')
try:
    makan = str(makan)
except:
    makan = 'Y'
if makan == 'Y' or makan == 'y':
    print('oh udah makan yaudah')
else:
    print('mau makan apa ?')
