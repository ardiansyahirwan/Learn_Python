# library yang digunakan
import datetime as dt

def say_about_independence_day():
   # Mendapatkan waktu hari ini
   today = dt.date.today()
   # variabel hari kemerdekaan indonesia
   INDONESIA_INDEPENDENCE = dt.date(year=1945,month=8,day=17)
   INDONESIA_INDEPENDENCE_THIS_YEARS = dt.date(year=today.year,month=8,day=17)

   # Cek apakah hari ini hari kemerdekaan Indonesia
   if today == INDONESIA_INDEPENDENCE_THIS_YEARS:
      years = INDONESIA_INDEPENDENCE_THIS_YEARS.year - INDONESIA_INDEPENDENCE.year
      return f"Selamat Hari Kemerdekaan Indonesia yang ke-{years}"
      
   else:
   # jika sudah terlewat, hitung berapa harinya setelah kemerdekaan
      if today.month >= INDONESIA_INDEPENDENCE_THIS_YEARS.month and today.day > INDONESIA_INDEPENDENCE.day:
         day = today - INDONESIA_INDEPENDENCE_THIS_YEARS
         return f"{day.days} hari setelah Hari Kemerdekaan Indonesia"
         
      else:   
   # Jika belum, kurang berapa hari lagi
         day = INDONESIA_INDEPENDENCE_THIS_YEARS - today
         return f"{day.days} hari lagi sebelum Hari Kemerdekaan Indonesia"
      
      
