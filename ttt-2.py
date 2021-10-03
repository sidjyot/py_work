# tic tac toe - 2 Grid and inputs 

x = input("Enter Cells: ")
print("---------")
for i in range(0,9,3):
	print(f"| {x[i]} {x[i + 1]} {x[i + 2]} |")
print("---------")
