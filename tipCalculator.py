#Erik Hansen
#9/6/2017
#tipCalculator.py - Shows amount to tip

price = float(input('Price of meal (in dollars): '))
percent = float(input('% to tip: '))
tip = price*(percent/100)

print('You should tip ', round(tip,2),'dollars')
