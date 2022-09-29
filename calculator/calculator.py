def add(x ,y):
    return x + y
def sub(x ,y):  
    return x - y  
def mult(x ,y):
    return x * y    
def div(x ,y):  
    return x / y     
def calculation():
    first_number = int(input("enter the first number : "))
    result = 0
    cont = True
    op = {
    "+":add,
    "-":sub,
    "*":mult,
    "/":div
    }
    while(cont == True ):
        for n in op:
            print(n)
        operation = input("pikc the next operation : ")      
        num2 = int(input("enter the next number : "))
        calculation = op[operation] 
        result = calculation(first_number, num2)
        print(result)
        next = input(f"enter'y' if u want to continue with {result}, or 'n' if u don't : ")   
        if next == "y":
            first_number = result
        else:
            cont = False
  
calculation()

        
    

