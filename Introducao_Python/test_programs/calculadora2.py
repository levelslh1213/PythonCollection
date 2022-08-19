operators = ['+', '-', '/', '*', '%']

def get_input():
    while True: #enquanto for verdadeiro, loop infinito para pegar caracteres
      try:
        number1 = float(input("Tap your first number: "))
        number2 = float(input("Tap your first number: "))
        return number1, number2
      except ValueError:
        print('Invalid input. Please try Again')
        continue

def get_operator():
    while True:
        try:
            option = input("Chose your operation to do: ")
            if option in operators:
                return option
        except ValueError:
            print('Invalid Option. Please choose a valid input')
            continue

def calculate(option,number1, number2):
    if option == '+':
        return number1+number2
    elif option == '-':
        return number1-number2
    elif option == '/':
        return number1/number2
    elif option == '*':
        return number1*number2
    elif option == '%':
        return number1%number2


def start_application():
    option = get_operator()
    number1, number2 = get_input()
    print(calculate(option, number1, number2))

start_application()