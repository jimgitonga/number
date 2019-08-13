# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 11:22:56 2019

Ask the user to enter a
number between 10 and 20
(inclusive). If they enter a
number within this range,
display the message “Thank
you”, otherwise display the
message “Incorrect
answer”.
"""
while True:
    number=int(input('enter a number between (10-20): '))
    if number in range(10,20):
        
        print('thank you')
    else:
        print('incorrect number')