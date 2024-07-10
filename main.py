#Calculator

#Add Function: Takes 2 numbers and adds them together
def add(n1, n2):
  return n1 + n2
  
#Subtract Function: Takes 2 numbers and subtracts one from the other
def subtract(n1, n2):
  return n1 - n2
  
#Multiply Function: Takes 2 numbers and multiplies them together
def multiply(n1, n2):
  return n1 * n2
  
#Divide Function: Takes 2 numbers and divides one by the other
def divide(n1, n2):
  return n1 / n2

#A Dictionary to store the functions
calc_operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

#Ask the user for the first and second number
num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))

#Loop through the calc operations dictionary and print out each symbol
for symbol in calc_operations:
  print(symbol)
#ask the user for what operation they want based on the symbols
operation_symbol = input("Pick an operations from the line above: ")