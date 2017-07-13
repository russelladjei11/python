
#Defines the function 'calculate' by using the math operators

def calculate(task, num1, num2):
        if task == 'add':
                return num1 + num2
        elif task == 'subtract':
                return num1 - num2
        elif task == 'multiply':
                return num1 * num2
        elif task == 'divide':
                return num1 / num2

value = calculate('subtract', 10, 15)
print(value)
