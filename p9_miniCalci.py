Num1 = int(input("enter the first 1st number: "))
operator = input("enter your operator '+,-,/,*,%': ")
Num2 = int(input("enter the first 2st number: "))

if operator == '+':
    print(f"the sum of {Num1} + {Num2} is {Num1 + Num2}")
elif operator == '-':
    print(f"the difference of {Num1} - {Num2} is {Num1 - Num2}")
elif operator == '*':
    print(f"the product of {Num1} * {Num2} is {Num1 * Num2}")
elif operator == '/':
    if Num2 == 0 :
        print("invalid input the denominator cannot be 0 change the input ")
    else:
        print(f"the divided of {Num1}  {Num2} is {Num1 // Num2}")
elif operator == '%':
    print(f"the modulus of {Num1} % {Num2} is {Num1 % Num2}")
else:
    print(f" you have selected an invalid operator check it")