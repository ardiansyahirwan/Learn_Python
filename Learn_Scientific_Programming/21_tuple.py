math_value = tuple()
math_value = (10, 20, 30)
# tuple adalah salah satu collection dalam python yang nilainya tidak bisa diubah

# kamu juga bisa menulis tuple dengan cara ini
(history_value, english_value) = (70, 80)

# kita juga bisa mengkombinasi tuple dengan dictionary
studies_value = {'math': 70, 'english': 85, 'history': 90}
for (k, v) in studies_value.items():
    print(k, v)


# cetak tuple
print(math_value, history_value, english_value)
