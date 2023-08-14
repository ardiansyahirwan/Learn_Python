# Arbitrary non-keyword arguments, *args
# if you dont know how much parameter that your function receive, they are return tuple
def product(*product_kind):
    return product_kind[2]
print(product("Food", "Beverages", "Medicine"))

# keyword arguments
def product_keyword(food ,beverages ,medicine):
   return f"Product key is {food}"
print(product_keyword(beverages = "susu",medicine = "Paracetamol", food="basreng"))

# arbirary keyword argument, *kwargs
# if you dont know how much keyword arguments that your function receive, they are return dictionary
def product_kwargs(**product):
   return f"product is {product['susu']}"
print(product_keyword(food = "nasi Goreng",beverages = "susu",medicine = "Paracetamol"))

# Pass Arguments
def product_pass():
   pass
print(product_pass)

# positional argument
def positional_argument(merk,type):
   """function yang parameternya harus sesuai letaknya dengan argumennya"""
   print(f"merk nya adalah :{merk}\ntypenya :{type}")
positional_argument("Lenovo","laptop")
positional_argument("laptop","Lenovo")
print(positional_argument.__doc__)

# anonymous function
code = lambda x : x + 10
print(code(10))