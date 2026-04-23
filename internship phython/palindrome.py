word = input("enter a word :")
if(word == word[::-1]):
    print("yes this word", word ," is a palindrone")
else:
    print("no this word is not ", word , "a palindrone")
