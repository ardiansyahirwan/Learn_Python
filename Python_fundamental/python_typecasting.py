# try and except
try:
   # Assert Exception
   fruits = 6
   alphabet = input('Type word ...\n')
   assert ("0123456789" not in alphabet), "Just receive word not a number"
except:
   print("just receive an word not number")
else:
   # Raise and Exception
   print(f"run else section")
   if fruits > 5:
      raise Exception(f"Fruits must be < 5 . Now fruits is: {format(fruits)}")