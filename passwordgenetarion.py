import random

print("Welcome to Password Generation!")
print("===============================")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%¨&*()_+,.0123456789"

number = int(input('Input amount of passwords to genetate: '))

length = int(input('Input your length passwords: '))

print('\nhere are your passwords: ')

for pwds in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)    
    print(passwords)