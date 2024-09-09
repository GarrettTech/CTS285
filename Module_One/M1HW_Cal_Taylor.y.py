#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Garrett Taylor
Fall 2024 Systems Analysis & Design (CTS-285-0001)
M1HW1 Calc
menu based calculator broken up into multiple functions to handle inputs, proccessing then outputs.
Created on Wed Aug 21 12:10:43 2024

@author: garrettintech
"""
import Module_One.M1HW1_functions as f

exit_Menu = 5


def main():
    
    #choice initialized to control my loop
    choice = 0
    #while loop for the menu
    while choice != exit_Menu:
        
        #menu Function
        f.display_Menu()
        choice = int(input("Enter your choice: "))
        
        #display file function
        if choice == 1:
            x,y = f.get_nums()
            
            results = f.addition(x, y)

            f.display_Add(x, y, results)
           
        elif choice == 2 :
            
            x,y = f.get_nums()
            
            results = f.subtraction(x,y)
            
            f.display_Sub(x, y, results)
           
            
        elif choice == 3:
            
            x,y = f.getnums()
            
            
            
         
        
        elif choice == exit_Menu:
            print("Exiting program..Thank you")
      
        else:
            print("Enter a valid option from the list above!")

   
if __name__ == "__main__":
    main()