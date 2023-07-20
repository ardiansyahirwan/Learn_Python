# foods = ['Ayam Goreng', 'Nasi Kotak', 'Nasi Goreng']

# for food in foods:
#     print('Saya suka', food)
# print('Done !!')

# smallest = None
# print("Before:", smallest)
# for number_smallest in [3, 41, 12, 9, 74, 15, 2]:
#     if smallest is None or number_smallest < smallest:
#         smallest = number_smallest
#     print("Loop:", number_smallest, smallest)
# print("Smallest:", smallest)

# biggest_so_far = None
# for number in [2, 57, 3, 6, 8, 200, 298, 199, 340]:
#     if biggest_so_far is None or number > biggest_so_far:
#         biggest_so_far = number
#     print('Number now :', number, 'Biggest so far :', biggest_so_far)
# print('Biggest', biggest_so_far)

# Counting a Loop
# jumlah_loop = 0
# print('jumlah pengulangan', jumlah_loop)
# for buah in ['Belimbing', 'Jambu Kristal', 'Matoa', 'Mangga Alpukat']:
#     jumlah_loop = jumlah_loop + 1
#     print('perulangan ke-', jumlah_loop, 'adalah buah', buah)
# print('jumlah perulangan adalah :', jumlah_loop)

count = 0
sum = 0
print('count before', count)
for number in [3, 4, 7, 8, 7, 8, 9, 9]:
    count = count + 1
    sum = sum + number
print('count after:', count)
print('total of array', sum)
print('average', sum/count)
