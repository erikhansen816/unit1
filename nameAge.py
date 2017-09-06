#Erik Hansen
#9/1/2017
#ageName.py - showing letters in name and next age

name = input('Enter your first and last name: ')
age = int(input('Enter your age: '))
firstname, lastname = name.split()
print('Your first name has', len(firstname), 'letters')
print('Your last name has', len(lastname), 'letters')
print('Next year you will be', age+1, 'years old')