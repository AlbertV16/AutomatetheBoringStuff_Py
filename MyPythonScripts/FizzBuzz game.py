# FizzBuzz game
def FizzBuzz1(number):
    
    for i in range(1, number + 1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

def FizzBuzz(number):
    for i in range(1, number + 1):
        output = ''
        if i % 3 == 0:
            output += 'Fizz'
        if i % 5 == 0:
            output += 'Buzz'
        if output == '':
            output = i
        print(output)
            
FizzBuzz(100)
