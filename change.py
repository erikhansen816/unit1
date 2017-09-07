#Erik Hansen
#9/7/2017
#change.py - cents to different coins

cents = int(input('Input a number of cents: '))
quarters = cents//25
remainder1= cents%25
dimes = remainder1//10
remainder2 = remainder1%10
nickels = remainder2//5
remainder3 = remainder2%5
pennies = remainder3//1
print('Quarters: ',quarters)
print('Dimes: ',dimes)
print('Nickels: ',nickels)
print('Pennies: ',pennies)
