# sort the tuples

studies_value = {'math': 100, 'history': 90}
studies_value['bahasa'] = 97

# ubah nilai dictionary
studies_value['math'] = 80
# or
studies_value.update({'math': 75})

# kita looping dan kita sort
for k, v in sorted(studies_value.items()):
    print(k, v)


# print
print(studies_value)
