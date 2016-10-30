#Have a function factorial(number), take the number parameter been passed and return the factorial of it.
#For example: if number is 4, it should return (4 * 3 * 2 * 1) which is 24.

def factorial(num):
	factorial = 1
	for i in range(1, num+1):
		factorial = factorial * i
	return factorial

print(factorial(10))		