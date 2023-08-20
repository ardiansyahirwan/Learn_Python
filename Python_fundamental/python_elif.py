food = input("Whats your favorite food ?\n")
country = input("\nwhere is the food come from ?\n")

if "sushi" in food and 'japan' in country:
   print(f"Ohh thats {food}, I know it's from {country}")
elif 'indonesia' in country:
   print(f"Really ? {food} from {country} right ? I'm from {country} too")
elif food.isdigit() or country.isdigit():
   print("Oh noo, its a Number, Please re-input again.")
else:
   print(f"So your favorite food is {food} and it's from {country}") 

