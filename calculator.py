def add(a, b):
	return a + b
def subtract(a, b):
	return a - b
def multiply(a, b):
	return a * b
def divide(a, b):
	return a / b
def square(num):
	return num * num
def power(a, b):
	return a ** b
	
while True:
	print("1.  Add")
	print("2.  Subtract")
	print("3.  multiply")
	print("4.  divide")
	print("5.  Square")
	print("6.  power")
	print("7.  Exit")
	print("-" * 30)
		
	choice = int(input("Enter Choice:  "))
	if choice == 7:
		break
	
	if choice == 1:
		num1 = float(input("Enter First Number:  "))
		num2 = float(input("Enter Second Number:  "))
		print("Result:", add(num1, num2))
	elif choice == 2:
		num1 = float(input("Enter First Number:  "))
		num2 = float(input("Enter Second Number:  "))
		print("Result:", subtract(num1, num2))
	elif choice == 3:
		num1 = float(input("Enter First Number:  "))
		num2 = float(input("Enter Second Number:  "))
		print("Result:", multiply(num1, num2))
	elif choice == 4:
		num1 = float(input("Enter First Number:  "))
		num2 = float(input("Enter Second Number:  "))
		if num2 == 0:
			print("Result: Cannot divide by Zero")
		else:
			print("Result:", divide(num1, num2))
	elif choice == 5:
		num = float(input("Enter Number:  "))
		print("Result:", square(num))
	elif choice == 6:
		num1 = float(input("Enter First Number:  "))
		num2 = float(input("Enter Second Number:  "))
		print("Result:", power(num1, num2))
	else:
		print("Invalid Choice")
