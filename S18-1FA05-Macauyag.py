import math

# Finding coordinates
x1 = float(input("Enter x1 : "))
y1 = float(input("Enter y1 : "))
x2 = float(input("Enter x2 : "))
y2 = float(input("Enter y2 : "))

# Solving for distance
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Displaying results
print("The distance is :", round(distance, 2))

#Reflection and Evaluation
#Guide questions:
#How did the math library help simplify your program? : It helped simplify the program by providing built-in functions like math.sqrt() for calculating the square root and math.pow() for exponentiation, which made the code cleaner and easier to read.
#What functions were easier to use because of the library? : The functions that were easier to use because of the library were math.sqrt() and math.pow().
#How would the program be more difficult without math.sqrt() and math.pow()? : The program would be more difficult without these functions because we would have to implement our own square root and exponentiation functions, which would be more complex and error-prone.