#Erik Hansen
#9/7/2017
#stringAnalysis.py - counting words and characters and finding letters

sentence = str(input('Enter a sentence: '))
spaces = ' '
words = sentence.count(spaces)+1
characters = len(sentence)
letters = characters-sentence.count(spaces)
print('Your sentence has',words,'words and',characters,'characters and',letters,'letters')
lettersearch = str(input('Enter a character to search for: '))
print('Your sentence has',sentence.count(lettersearch),'of the character',lettersearch)
wordsearch = str(input('Enter a word to search for: '))
print('Your sentence has',sentence.count(wordsearch),'of the word',wordsearch)


