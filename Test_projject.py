def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
while True:
    try:
      num_1 = float(input("Enter a number: "))
      num_2 = float(input("Enter a number: "))
      print("+ - * /")
      print("(Enter 'stop' in choice to end loop.)")
      choice = input("Enter an operator you would like to carry out: ")
  
    except ZeroDivisionError:
       print("You can't divide by zero!")    

    except ValueError:
     print("Please enter a valid number")

    if choice == "+":
     print("Sum is", add(num_1,num_2))
    elif choice == "-":
     print("Difference is", subtract(num_1,num_2))
    elif choice == "*":
     print("Product is", multiply(num_1,num_2))
    elif choice == "/":
     print("Quotient is", divide(num_1,num_2))
    elif choice == "stop":
        break
    else:
     print("Please choose a valid operation!")