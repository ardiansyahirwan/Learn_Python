import re

# matches dengan karakter non angka \D
text = 'Tahun 2023 ini akan menjadi tahun pemilu'

# \D untuk karakter non angka
regex_pattern = r'\d\S+'
matched = re.findall(regex_pattern, text)

# replace angka dengan huruf atau sebaliknya
replace_text = re.sub(regex_pattern, ' xxxx ', text)

print(f"hasil dari pencarian menggunakan RegEx adalah : {matched}")
print(f"hasil dari pencarian menggunakan RegEx adalah : {replace_text}")


# Memecah kalimat menjadi kata-kata
text = "Ini adalah contoh kalimat"
words = re.split(r'\s', text)  # Pola untuk mencocokkan spasi sebagai pemisah
print(words)  # Output: ['Ini', 'adalah', 'contoh', 'kalimat']

s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
print(lst)
