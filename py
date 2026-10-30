import math
a = 5
b = 10
c = 7

a += 3
b *=2
c %= 4

result = math.sqrt(a**2 + b**2 + c**2)
print(round(result, 2)) 



x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))
is_even = x % 2 == 0
is_positive = y > 0
is_in_range = 10 <= z <= 50
final_condition = is_even and is_positive and is_in_range
print(final_condition)

score = int(input("Enter base score: "))
score =+ 5 # bonus points
score -= 10 # late penalty
score = max(0, min(100, score))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F" 
print(f"Final score: {score},Grade:{grade}")


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number:"))
operation = input("Enter operation (+, -, *, /, %, **,):")
if operation =="+":
    result = num1 = num2
elif operation == "-":
    result = num1 - num2
elif operation =="*":
    result = num1 * num2
elif operation =="/":
    try:
        result = num1 / num2
    except ZeroDivisionError: 
         print("Error: Cannot divide by zero") 
         result = None 
elif operation == "%":
    try:
         result = num1 % num2
    except ZeroDivisionError:
         print("Error: Cannot module by zero")
         result = None
elif operation == "*":
    result = num1 ** num2
else:
    print("Invalid operation")
    result = None

# TODO: Print result
if result is not None:
    print(f"Result: {result}")4
    
