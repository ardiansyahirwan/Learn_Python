# Looping While countdown a new year
# repeat = 5

# print('countdown from')
# while repeat >= 0:
#     print(repeat)
#     repeat = repeat - 1
# print('HAPPY NEW YEAR')

# choose menu
repeat = True
while repeat:
   menu=input("""PILIH MENU ANDA
   1. Ayam
   2. Nasi Goreng
   3. Nasi Pecel
   (Tulis Nomer nya saja)
   """)
   
   match menu:
      case "1":
         order = "Menu yang ada pilih adalah Ayam"
      case "2":
         order = "Menu yang ada pilih adalah Nasi Goreng"
      case "3":
         order = "Menu yang ada pilih adalah Nasi Pecel"
      case _:
         order = "Kamu tidak memilih menu apapun"
      
   ask = input("Apakah anda akan pesan yang lain ? (Y/N)\n")
   if ask == 'y' or ask=='Y':
      repeat = True
   else :
      repeat = False
print(f"\n{'='*len(order)}")
print(order)