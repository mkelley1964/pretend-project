#######################################################
# Name:       Katelyn Fairley
# Class:      CIS-2531-NET01
# Assignment: Homework 1
# Purpose:    Area of a triangle
#######################################################

print('Welcome to my program.\nPlease enter your full name:',end='')
full_name = str(input())
print('')
print('Hello', full_name)
print('')
print('This program will ask you to enter the base ',end='')
print('and the height of a triangle. The program will ',end='')
print('calculate and print the area of the triangle.')
print('')

print('Enter the length of the base: ', end='')
length_of_base = float(input())
print('')

while length_of_base < 1:
    print('ERROR: Re-enter the length of the base: ', end='')
    length_of_base = float(input())
    print('')

print('Enter the height of the triangle: ', end='')
height_of_triangle = float(input())
print(' ')

while height_of_triangle < 1:
    print('ERROR: Re-enter the height of the triangle: ', end='')
    height_of_triangle = float(input())
    print('')

area_of_triangle = (length_of_base * .5 ) *  height_of_triangle
print('The area of the triangle is', area_of_triangle)
print('')
print('Thank you and have a nice day.\nGood bye!')
