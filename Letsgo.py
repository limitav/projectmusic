#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 10:21:47 2021

@author: Avery
"""
import re
import os 

#Will be used for getting User Specified 
#userPathName = input("Enter the Folder You Want To Search\n")
#pathSlash= '/'
#userPath = pathSlash + userPathName
#print(os.listdir())

#Retrieves the current directory path.
dir_path = os.path.dirname(os.path.realpath(__file__))

#Loops through Directory 
for root, dirs, files in os.walk(dir_path):
    #Loops through files
    for file in files:
        # ADD YOUR CODE HERE: 
        #Ex: x = re.findall("Lucki", dirs)
        #print(x)
        if file.endswith('.py') :
            print(root + '/'+ str(file))



