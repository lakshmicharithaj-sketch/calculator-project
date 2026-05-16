def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    
    while True:
        try:
            num1 = float(input("\nEnter first number: "))
            choice= input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))
            
            if choice == '+':
                result = num1 + num2
            elif choice == '-':
                result = num1 - num2
            elif choice == '*':
                result = num1 * num2
            elif choice == '/':
                if num2 == 0:
                    print("Error: Division by zero!")
                    continue
                result = num1 / num2
            else:
                print("Invalid operator!")
                continue
            
            print(f"Result: {num1} {choice} {num2} = {result}")
        
        except ValueError:
            print("Invalid input! Enter numbers only.")
        
        again = input("\nCalculate again? (yes/no): ")
        if again.lower() != 'yes':
            break

calculator()