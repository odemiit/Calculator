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

#Ask the user for the first number
num1 = int(input("What's the first number?: "))

#Loop through the calc operations dictionary and print out each symbol
for symbol in calc_operations:
  print(symbol)
  
repeat = True

while repeat:
  #Ask the user for what operation they want based on the symbols
  operation_symbol = input("Pick an operation: ")
  
  #Ask the user for the second number
  num2 = int(input("What's the next number?: "))
  
  #Perform the function based on the symbol picked and print out the answer
  answer = calc_operations[operation_symbol](num1, num2)
  print(f"{num1} {operation_symbol} {num2} = {answer}")

  to_continue = input(f"Type 'y' to continue calculating with {answer},\
 or type 'n' to exit: ")

  if to_continue == "n":
    repeat = False
  elif to_continue == "y":
    num1 = answer