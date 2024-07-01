def main_function():
    print('''
    Welcome to BasicCalculator: 
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    ''')
    num = int(input('Choose any of the above: '))

        # using if and elif statements

        #    ADDITION

    if num == 1:
        print('Enter the two numbers you want to add:\n')
        a = float(input('a = ')) 
        b = float(input('b = '))
        print(round(a + b , 3))

        #   SUBTRACTION   

    elif num == 2:
        print('Enter the two numbers you want to substract:\n')
        a = float(input('a = ')) 
        b = float(input('b = '))
        print(round(a - b , 3))

        #   MULTIPLICATION

    elif num == 3:
        print('Enter the two numbers you want to multiply:\n')
        a = float(input('a = ')) 
        b = float(input('b = '))
        print(round(a * b , 3))

        #   DIVISION

    elif num == 4:
        print('Enter the two numbers you want to divide:\n')
        a = float(input('a = ')) 
        b = float(input('b = '))
        if b == 0:
            print('Division by zero is not allowed.')
        else:    
            print(round(a / b , 3))

        # using while statements to make the program work again

while True:
    main_function()
    user_input = input('Do you want to run the program again? yes / no :').strip().lower()  
    if user_input not in ['yes' , 'y']:
        print('Exiting...')
        break