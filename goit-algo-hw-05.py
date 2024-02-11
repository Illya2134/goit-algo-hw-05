#Перше завдання
def caching_fibonacci():
    cache = {}  

    def fibonacci(n):
        nonlocal cache

        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

fibonacci_function = caching_fibonacci()

print(fibonacci_function(6))




#Друге завдання
from typing import Callable  

def generator_numbers(text: str):
    text_list = text.split(' ')
    numbers = filter(lambda x: x.isdigit() or'.' in x and x.replace('.', '').isdigit(), text_list)
    
    for number in numbers:
        yield float(number)
     
    

def sum_profit(text: str, func: Callable):
    numbers_generator = func(text)
    total_sum = sum(numbers_generator)
    return total_sum
   
text = "Загальний дохід працівника складається 100 з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")



#Четверте завдання
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found!"
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated"
    else:
        return "Contact not found!"

@input_error        
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found!"
        
def show_all(contacts):
    for name, phone in contacts.items():
        return f'{name}: {phone}'



def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            if (change_contact(args, contacts)) is not None:
                print(change_contact(args, contacts))
        elif command == "phone":
            if show_phone(args, contacts) is not None:
                print(show_phone(args, contacts))
        elif command == "all":
            if show_all(contacts) is None:
                print("Add the contacts first!")
            else:
                print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
 