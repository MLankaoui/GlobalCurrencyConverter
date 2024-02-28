from dotenv import load_dotenv
import os

from exchange import exchange

load_dotenv()
api_key = os.getenv('API_KEY')

def main():
    print('Global Currency Conversion')

    name = input('Enter your full name: ').capitalize

    line_counter = 1

    welcome_to(name)

    options_message(name)

    while True:
        user_input = input(f"{line_counter} > ").lower()
        line_counter += 1

        if user_input == 'options':
            display_options()

        elif user_input == '1':
            user_currency = input('Please enter your currency (e.g., AED): ').upper()
            target_currency = input('Please enter the base currency (e.g., USD): ').upper()
            amount = input('Please enter the amount: ')

            exchange(user_currency, target_currency, amount)

        elif user_input == '2' or user_input == 'quit':
            print('Quitting...')
            exit(0)


def welcome_to(user_name):
    print(f'Hello Mr./Ms. {user_name}')


def options_message(name):
    print(f"Hello {name}, please enter 'options' to display the list of options")


def display_options():
    print("1) Get the amount of your currency needed to convert to a target currency")
    print("2) Quit to exit the program")



def options_message(name):
    print(f"Hello {name}, please enter 'options' to display the list of options")


def display_options():
    print("1) Get the amount of your currency needed to convert to a target currency")
    print("2) Quit to exit the program")

main()