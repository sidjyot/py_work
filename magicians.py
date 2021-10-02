#  magicians.py
#  Chapter 4 - Using for loop to manipulate lists. Try it with 3 pizzas and 3 animals

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	# print(magician)
	print(f"{magician.title()}, that was a great trick!")
	print(f"I can't wait to see your next trick,  {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")	