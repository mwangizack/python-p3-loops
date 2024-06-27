#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    count = 10
    while count >= 0:
        if count == 0:
            print("Happy New Year!")
        else:
            print(count)
        count -= 1

def square_integers(int_list):
    # code goes here!
    int_list = [int * int for int in int_list]
    return int_list

def fizzbuzz():
    # code goes here!
    for i in range(101):
        if i > 0:
            if i % 3 == 0 and i % 5 == 0:
                print('FizzBuzz')
            elif i % 3 == 0:
                print('Fizz')
            elif i % 5 == 0:
                print('Buzz')
            else:
                print(i)
    
