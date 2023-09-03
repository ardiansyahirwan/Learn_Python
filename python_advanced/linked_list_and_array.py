# from array import *

# # define array
# py_array = array('I',[1,2,3])
# print(py_array)

# # calculate array length
# print(f"Panjang array nya adalah : {len(py_array)}")

# # search index value from array
# try:
#    print(f"Index dari element array 1 adalah : {py_array.index(1)}")
# except ValueError:
#    print("Element tidak ada di dalam array")
   
# # change value
# py_array[0] = 400
# print(f"sekarang nilai index ke 0 di ubah jadi 400\n{py_array}")

# # add new value into array, will placed in end of array
# py_array.append(4)
# print(f"menambahkan value {4} ke variable\n{py_array}")

# # add new value more than one value
# py_array.extend([22,23,24])
# print(py_array)

# # insert value into index
# py_array.insert(0,4)
# print(py_array)

# # remove value from array
# py_array.remove(400)
# print(py_array)

# # remove value using index
# py_array.pop(6)
# print(py_array)


# List
food_lists = ["ayam goreng","sate ayam","soto",10,11,12,True]

# remove one of data in list
food_lists.remove(True)
print(food_lists)

# remove where index is ..
food_lists.pop(1)
print(food_lists)
# remove all
print(food_lists.clear())









# # change list
# food_lists[0] = "bakpau goreng"
# print(food_lists)

# # change more than one value
# food_lists[3:6]=["gulai","rendang","ayam pop"]
# print(food_lists)












# # add one value into list
# food_lists.append("nasi goreng")
# print(food_lists)

# # add with specified index
# food_lists.insert(0,"bakso")
# print(food_lists)
# food_lists.extend(["martabak","batagor"])
# print(food_lists)










# # Accessing List
# print(food_lists[1])
# # or

# # output is "ayam goreng","sate ayam","soto",10,11
# print(food_lists[0:5])