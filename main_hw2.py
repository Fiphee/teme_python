def get_sum(*args, **kwargs):
    my_sum = 0
    for num in args:
        num_type = type(num).__name__
        if num_type == 'int' or num_type == 'float':
            my_sum += num
    return my_sum


def sum_of_numbers_up_to(n):
    if n == 0:
        return n
    return n + sum_of_numbers_up_to(n-1)


def sum_of_even_numbers_up_to(n):
    if n == 0:
        return n
    if n % 2 == 0:
        return n + sum_of_even_numbers_up_to(n-2)
    return sum_of_even_numbers_up_to(n-1)


def sum_of_odd_numbers_up_to(n):
    if n <= 0:
        return n
    if n % 2 == 1:
        return n + sum_of_odd_numbers_up_to(n-2)
    return sum_of_odd_numbers_up_to(n-1)


def check_integer(user_typed=None):
    if user_typed == None:  # for interactive play function below.
        user_input = input('Check if integer: ')
    else:
        user_input = user_typed
    if user_input == '':
        return 0
    elif user_input.isdigit():
        return int(user_input)
    elif user_input[0] == '-' and user_input[1:].isdigit():
        return int(user_input)
    return 0


def recursive(n):
    if n == 0:
        return n, 0, 0
    results = recursive(n-1)
    odds = results[1]
    evens = results[2]
    if n % 2 == 1:
        odds += n
    else:
        evens += n
    n += results[0] 
    return n, odds, evens
    
recursive_results = recursive(10)
print(f'Sums: {recursive_results[0]}, Odd sums: {recursive_results[1]}, Even sums: {recursive_results[2]}')


###############################################
###  Interactive version below, call play() ###
###############################################


def _valid_input(get_input):
    if get_input != '0':
        check = check_integer(get_input)
        if check == 0:
            return [False, check]
        return [True, check]
    return [None, None]


def _decision_after_validity(func, valid_num, valid_txt):
    if valid_num[0] == None:
        print("It's... 0")
        return 'stop'
    elif not valid_num[0]:
        print('Invalid number, try again')
    else:
        if valid_num[1] < 0:
            print('Number invalid (under 0), try again')
            return 'continue'
        result = func(valid_num[1])
        print(valid_txt + f'{result}')
        return 'stop'


def play():
    print('Welcome, type "help" to see available commands!')
    while True:
        print()  # empty line to make the text less cluttered
        user_typed = input('>:')
        if user_typed.lower() == 'check':
            get_number = input("Type something to check if it's an integer: ")
            result = check_integer(get_number)
            if result == 0 and get_number != '0':
                print(f'{get_number} is not an integer')
            else:
                print(f'{get_number} is an integer!')
        elif user_typed.lower() == 'sum':
            run = True
            while run:
                get_number = input("Sum up all the numbers up to: ")
                valid_num = _valid_input(get_number)
                result_txt = f'Sum of all numbers up to {get_number} is '
                decision = _decision_after_validity(
                    sum_of_numbers_up_to, valid_num, result_txt)
                if decision == 'stop':
                    run = False
                elif decision == 'continue':
                    continue

        elif user_typed.lower() == 'sum even':
            run = True
            while run:
                get_number = input("Sum up all even numbers up to: ")
                valid_num = _valid_input(get_number)
                result_txt = f'Sum of even numbers up to {get_number} is '
                decision = _decision_after_validity(
                    sum_of_even_numbers_up_to, valid_num, result_txt)
                if decision == 'stop':
                    run = False
                elif decision == 'continue':
                    continue

        elif user_typed.lower() == 'sum odd':
            run = True
            while run:
                get_number = input("Sum up all odd numbers up to: ")
                valid_num = _valid_input(get_number)
                result_txt = f'Sum of odd numbers up to {get_number} is '
                decision = _decision_after_validity(
                    sum_of_odd_numbers_up_to, valid_num, result_txt)
                if decision == 'stop':
                    run = False
                elif decision == 'continue':
                    continue

        elif user_typed.lower() == 'calc':
            run = True
            typed_numbers = []
            print("Type numbers you would like to add to eachother")
            print("and type 'done' for the result")
            while run:
                typed = input('plus: ')
                if typed == 'done':
                    result = get_sum(*typed_numbers)
                    print(result)
                    run = False
                elif typed == 'show':
                    print(typed_numbers)
                else:
                    valid = _valid_input(typed)
                    if not valid[0] or valid[0] == None:
                        try:
                            typed = float(typed)
                        except:
                            pass
                        typed_numbers.append(typed)
                    else:
                        typed_numbers.append(valid[1])

        elif user_typed == 'help':
            print("'check' - Type a number and check if it's an integer")
            print("'sum' - Find the sum of all the numbers up to the number you type")
            print(
                "'sum even' - Find the sum of all the EVEN numbers up to the number you type")
            print(
                "'sum odd' - Find the sum of all the ODD numbers up to the number you type")
            print(
                "'calc' - Calculate the sum of all the numbers you type after this command")
            print("'quit' - Exit the application")

        elif user_typed == 'quit':
            print('Thank you for playing!')
            break


# individual tests

# print(get_sum())
# print(sum_of_numbers_up_to())
# print(sum_of_even_numbers_up_to())
# print(sum_of_odd_numbers_up_to())
# print(check_integer())

play()
