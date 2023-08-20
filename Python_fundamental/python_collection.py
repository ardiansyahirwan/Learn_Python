py_list = list()
# or
py_list2 = []
print(type(py_list))
print(type(py_list2))

py_dict = dict()
# or
py_dict2 = {}
print(type(py_dict))
print(type(py_dict2))

py_tuple = tuple("ayam")
# or
py_tuple2 = ()
print(type(py_tuple))
print(type(py_tuple2))

py_sets = set()
print(type(py_sets))

py_list.append('ayam')
py_dict["amimals"] = 'ayam'
py_sets.add("ayam")
print(py_list,py_dict,py_tuple,py_sets)