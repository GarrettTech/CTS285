#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 12:11:47 2024

@author: garrettintech
"""

def display_Menu():
    print("---------Menu----------")
    print("1) Addition")
    print("2) Subtract")
    print("3) Division")
    print("4) Multiplication")
    print("5) Exit")
    print("-----------------------")
    
def get_nums(): 
    x = float(input('Enter 1st number: ')) 
    y = float(input('Enter 2nd number: ')) 
    return x, y

def addition(x,y):
    return x + y
    
     
def display_Add(x,y,results):
    print(f' {x} + {y} is {results}') 
    
    
def subtraction(x,y):
    return x - y

def display_Sub(x,y,results):
    print(f' {x} - {y} is {results}') 
    


        
    
    
            
        
        
        
        
        
        

    
    


    