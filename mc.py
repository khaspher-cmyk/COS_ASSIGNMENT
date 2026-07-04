def mathematical_calculator():
    print("=== MATHEMATICAL CALCULATOR (MC) ===")
    print("Welcome! Type 'OFF' at any prompt to exit.")
    
    while True:
        # 1. Get the first number or check for OFF/Clear
        user_input1 = input("\nEnter first number (or 'OFF' to quit): ").strip()
        
        if user_input1.upper() == 'OFF':
            print("Shutting down calculator. Goodbye!")
            break
        if user_input1.upper() == 'C':
            print("Cleared!")
            continue
            
        try:
            num1 = float(user_input1)
        except ValueError:
            print("Invalid input. Please enter a valid number, 'C' to clear, or 'OFF' to quit.")
            continue

        # 2. Get the operator
        operator = input("Enter operator (+, -, *, /, \\, ^, %): ").strip()
        
        if operator.upper() == 'OFF':
            print("Shutting down calculator. Goodbye!")
            break
        if operator.upper() == 'C':
            print("Cleared!")
            continue

        # 3. Get the second number
        user_input2 = input("Enter second number: ").strip()
        
        if user_input2.upper() == 'OFF':
            print("Shutting down calculator. Goodbye!")
            break
        if user_input2.upper() == 'C':
            print("Cleared!")
            continue
            
        try:
            num2 = float(user_input2)
        except ValueError:
            print("Invalid input. Starting over.")
            continue

        # 4. Selection Control Statements to process the math
        if operator == '+':
            result = num1 + num2
            print(f"Result: {num1} + {num2} = {result}")
        elif operator == '-':
            result = num1 - num2
            print(f"Result: {num1} - {num2} = {result}")
        elif operator == '*':
            result = num1 * num2
            print(f"Result: {num1} * {num2} = {result}")
        elif operator == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"Result: {num1} / {num2} = {result}")
        elif operator == '\\':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                # '//' is Python's integer (floor) division
                result = num1 // num2
                print(f"Result: {num1} \\ {num2} = {int(result)}")
        elif operator == '^':
            # '**' is Python's exponentiation operator
            result = num1 ** num2
            print(f"Result: {num1} ^ {num2} = {result}")
        elif operator == '%':
            if num2 == 0:
                print("Error: Modulo by zero is not allowed.")
            else:
                result = num1 % num2
                print(f"Result: {num1} % {num2} = {result}")
        else:
            print("Invalid operator selected. Please use +, -, *, /, \\, ^, or %.")

# Run the calculator
mathematical_calculator()
