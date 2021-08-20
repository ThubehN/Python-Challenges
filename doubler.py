#create a function that takes in an array of numbers and returns a new array
#where every element of the original array is multiplied by 2

#create a function
#allow user to enter numbers
#whatever numbers entered should be multiplied by 2
#return the original numbers multiplied by 2

def doubler():
    number_list = input ("please enter number\n")
    multiplied_number = [int(number)*2 for number in number_list]
    print(multiplied_number)

doubler()