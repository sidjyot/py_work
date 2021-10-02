# players - Slicing a list
# players = ['charles', 'martina', 'michael', 'florence', 'eli']

# print("Here are the first three players on my team:")
# for player in players[:3]:
# 	print(player.title())

# Copying a list - using slicing a list with [:]
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]  # this is the key step

# friend_foods = my_foods  # this is wrong assignment

my_foods.append('canoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
