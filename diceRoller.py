#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 17:52:07 2021

@author: corey
"""
'''
ToDOs
1) Limit to standard die
2) When showing the user the final total, show them how many of EACH dice they rolled
3)Catch errors. Terminal will throw an error if you don't type '' around your
    input. Users won't like that.
'''

import random

#function for the rolling of the dice
def roll_dice():
    print("\nHow many sides are on the dice you would like to roll?")
    dice_type = int(input(""))#user can input any number for the "die" to roll
    standard_die = [4, 6, 8, 10, 20, 100]
    if dice_type in standard_die:
        print('\n... rolling a d{0} ...'.format(dice_type))
        dice_roll = (random.randint(1, dice_type))
        print("\nYou rolled a {0}!".format(dice_roll))
        return dice_roll
    else:
        print("Please choose a standard dice")
        return 0
        roll_dice()
    
#method for getting a new dice roll
def wants_new_roll():
    print("\nDo you want to roll some dice?\nYes or No?")
    choices = ["Y", "N"]
    user_choice = input('')
    user_choice_useable = user_choice[0].upper()
    if user_choice_useable in choices:
        if user_choice_useable == "Y":
            return True
        else:
            return False

#method to be called for the user to roll die        
def user_roll():
    while wants_new_roll() == True:
        print("\nHow many dice do you want to roll?")
        num_die = int(input(''))
        print("Alright we will roll {0} dice. Please tell us how many sides are on each die".format(num_die))
        total_rolled = 0 
        for i in range(num_die):
            total_rolled += roll_dice()
        print("\nYou rolled a {0} dice for a total of {1}.".format(num_die, total_rolled))
    print("\nThank you for using our dice roller!")
    print("\nFeel free to use our dice roller any time!")

user_roll()
            
