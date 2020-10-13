#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""2) Max Difference
You’re given a sequence of integers on a single line via standard input, each
separated by a single space. Print the maximum difference (in absolute value)
between any two numbers in the sequence on a single line on standard output.
Assumptions
1. Each number is separated by a single space.
2. The numbers can be positive, zero, or negative.
Example
Input:
1 9 2 -7 10 4 3
Output:
17
Explanation
The largest absolute difference between any two input numbers is |-7-10| = 17."""


enter_integers_sequence= input('enter integers on a single line seperated by a space to find the maximum difference(in absolute value) between any two numbers: ')
print("You entered these integers: " + enter_integers_sequence)
#splitting the strings values input 
values_list=enter_integers_sequence.split(" ")
#first change the string values in a string list to integers for computation and add those integers to a list named integers_list
integers_list=[]
for items in values_list:
    items=int(items)
    integers_list.append(items)
integers_list
#finding max from the list of integers
max_int=max(integers_list)
#printing the max value in string so that it can concatinated with the string text
print("Max integer in the list is: " + str(max_int))
#finding min from the list of integers
min_int=min(integers_list)
#printing the min value in string so that it can concatinated with the string text
print("Min integer in the list is: " + str(min_int))
absolute_value= abs(max_int-min_int)
print("The absolute value is: "+str(absolute_value))

