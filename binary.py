#Erik Hansen
#9/8/2017
#binary.py - changing binary to base 10

binary = int(input('Enter an 8-digit binary number: '))
first = int(binary%10)
first1 = int(binary//10)
second  = int(first1%10)
second1 = int(first1//10)
third = int(second1%10)
third1 = int(second1//10)
fourth = int(third1%10)
fourth1 = int(third1//10)
fifth = int(fourth1%10)
fifth1 = int(fourth1//10)
sixth = int(fifth1%10)
sixth1 = int(fifth1//10)
seventh = int(sixth1%10)
seventh1 = int(sixth1//10)
eighth = int(seventh1%10)
eighth1 = int(seventh1//10)

base10 = (first*2**0+second*2**1+third*2**2+fourth*2**3+fifth*2**4+sixth*2**5+seventh*2**6+eighth*2**7)
