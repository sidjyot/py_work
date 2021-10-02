#  cars.py
cars = ['bmw', 'audi', 'toyota', 'subaru']
#  cars.sort(reverse=True)
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
#  print(sorted(cars, reverse=True))
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

cars.reverse()
print(cars)
cars.reverse()
print(cars)

print(len(cars))
