num1 = input("1st number: ")
num2 = input("2nd number: ")
op = input("Operation: ")

class Operations:
	def add(self):
		calAdd = int(num1) + int(num2)
		print(str(calAdd))
	def sub(self):
		calSub = int(num1) - int(num2)
		print(str(calSub))
	def mul(self):
		calMul = int(num1) * int(num2)
		print(str(calMul))
	def div(self):
		calDiv = int(num1) / int(num2)
		print(str(calDiv))

if op == "+":
	if num1 == "" and num2 == "":
		print("Error: no value on '1st number' and '2nd number'")
	elif num1 == "":
		print("Error: no value on '1st number'")
	elif num2 == "":
		print("Error: no value on '2nd number'")
	else:
		Operations().add()
elif op == "-":
	if num1 == "" and num2 == "":
		print("Error: no value on '1st number' and '2nd number'")
	elif num1 == "":
		print("Error: no value on '1st number'")
	elif num2 == "":
		print("Error: no value on '2nd number'")
	else:
		Operations().sub()
elif op == "*":
	if num1 == "" and num2 == "":
		print("Error: no value on '1st number' and '2nd number'")
	elif num1 == "":
		print("Error: no value on '1st number'")
	elif num2 == "":
		print("Error: no value on '2nd number'")
	else:
		Operations().mul()
elif op == "/":
	if num1 == "" and num2 == "":
		print("Error: no value on '1st number' and '2nd number'")
	elif num1 == "":
		print("Error: no value on '1st number'")
	elif num2 == "":
		print("Error: no value on '2nd number'")
	else:
		Operations().add()
else:
	print("Error: no chosen operation, please try again.")