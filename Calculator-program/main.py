from art import logo
print(logo)




def add(n1,n2):
  return n1+n2

def subtract(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2

operations={
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
}

num1=int(input("What's the first number? "))


for key in operations:
  print (key)

operation_symbol=input("Pick an operation from the line above: ")

num2=int(input("What's the second number? "))

initial_result=operations[operation_symbol](num1,num2)

print(f'Your result is {initial_result}')

calculation_is_over=False

while calculation_is_over==False:
    proceed=input("Do you want to keep calculating? Y/N ").upper()
    if proceed=="Y":
        for key in operations:
            print (key)
        operation_symbol=input("Pick an operation from the line above: ")
        num2=int(input("What's the second number? "))                
        new_result=operations[operation_symbol](initial_result,num2)
        initial_result=new_result
        print(f'Your new result is {new_result}.')
    elif proceed=="N":
       print("Thank you for using the calculator")
       calculation_is_over=True