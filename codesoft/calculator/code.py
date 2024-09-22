def calculator():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
   
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    operation = input("\nEnter the operation (1/2/3/4): ")
    
   
    if operation == '1':
        result = num1 + num2
        print(f"\n{num1} + {num2} = {result}")
    elif operation == '2':
        result = num1 - num2
        print(f"\n{num1} - {num2} = {result}")
    elif operation == '3':
        result = num1 * num2
        print(f"\n{num1} * {num2} = {result}")
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"\n{num1} / {num2} = {result}")
        else:
            print("\nError: Division by zero is not allowed.")
    else:
        print("\nInvalid operation. Please choose a valid option.")


calculator()