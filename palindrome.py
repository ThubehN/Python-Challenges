word = input("please enter a word:")
#this is the user input
reversed_word = word[::-1]
def check_palindrome():# used string slice with reveresing
    print (reversed_word)
    if word == reversed_word:
        #determines if word is a palindrome or not
        print(True)
    else:
        print(False)

check_palindrome()