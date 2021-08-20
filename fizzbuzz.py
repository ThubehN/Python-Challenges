arr =[]

def numbers():
    max = int (input("please enter a number\n"))
    for number in range(max):
         if (number%4 == 0 or number%6==0) and not (number%4 == 0 and number%6==0):
            print(number)
numbers ()