import random, string, secrets, uuid
import os
from time import sleep

def clear():
    os.system('cls' if os.name=='nt' else 'clear')


print('Please choose the type of password you want to generate:')
print("1. 6 character password")
print("2. 8 character password")

length_choice = input()

if length_choice == "1":
    clear()
    print("1. Simple")
    print("2. Complex")
    print("3. Sophisticated")

    type_choice = input()

    if type_choice == "1":
        clear()
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(6))
        print(result_str)