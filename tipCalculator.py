#Erik Hansen
#9/6/2017
#tipCalculator.py - Shows amount to tip

price = float(input('Price of meal (in dollars): '))
tip = float(input('% to tip: '))
print('You should tip ', price*(tip/100),'dollars')
