 #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
# HIGA_Project.py is the final assignment in Robert Radloff's EE160 class, Spring 2025.
#
# Created by Scott Higa, 2025-05-09
# Last edit: 2025-05-09
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

import csv
import matplotlib.pyplot as plt
import numpy as np

with open("final.csv", "r") as file:
# 'with' is a condensed try/expect statement
# open the csv with the intention to read
# 'as' is similar to the assignment operator, "=". We're renaming the execution of this code to 'file'

    csv_reader = list(csv.reader(file))
# csv.reader is used to read data from the csv file by row. We are changing this to a list.

row3 = csv_reader[2]
# setting row3 to read the 2nd index, line 3 of the csv

sorted_row3 = sorted(row3)
# setting sorted_row3 to the sorted() function.  We don't need a key as it defaults to alphabetical/ascending order.

print(sorted_row3)
# printing the alphabetically sorted sorted_row3

with open("final.csv", 'r') as file:    # Open csv file with intention to read
    tc1 = (csv.reader(file))   # Column "Header" for the first row is "Robert".  The Column headers are actually in line 3

    next(tc1)  #Skip index 0
    next(tc1)  #Skip index 1
    next(tc1)  #Skip index 2

    for line in tc1:    # For each line in the time column
        print (line[13])  # Print the 0 index

print (" ")

with open("final.csv", 'r') as file:    #Opening csv file with intention to read
    csv_reader = csv.reader(file)       #Setting a variable for the read file
    next(csv_reader)                    #Skipping index 0
    next(csv_reader)                    #Skipping index 1
    next(csv_reader)                    #Skipping index 2
    column_index = 13                   #Setting variable for the column index we want

    column_values = [float(row[column_index]) for row in csv_reader]
# Creating an integer list of the 0 column. For each row in column 0...

    max_value = max(column_values)  #variable for max value in column
    min_value = min(column_values)  #variable for min value in column

    print ("Max:",(max_value))
    print ("Min:",(min_value))
    print (" ")

with open("final.csv", 'r') as file:
    csv_reader = csv.reader(file)

    next(csv_reader)  # Skipping index 0
    next(csv_reader)  # Skipping index 1
    next(csv_reader)  # Skipping index 2

    time_index = 0  # Accessing index 0 by setting to variable
    tc1_index = 13  # Accessing index 13 by setting to variable

    data = list(csv_reader) # Since we can only iterate through the reader once, we need to extract all data as a list and set to a variable

    time_values = [int(row[time_index]) for row in data]  #Creating an integer list for all values in time column.
    tc1_values = [float(row[tc1_index]) for row in data]    #Creating a float list for all values in tc1 column.

    # Creating plot for TC1 vs. Temp
    plt.plot(time_values,tc1_values, color = 'red', label = 'Temp vs. Time' )
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.title('TC1 Temp vs. Time')
    plt.legend()
    plt.grid(True)
    plt.show()

    tc2_index = 14  # Accessing index 14 by setting to variable.  Values for TC2
    tc2_values = [float(row[tc2_index]) for row in data]  # Creating a float list for all values in TC2 column.

    # Creating plot for TC2 vs. Temp
    plt.plot(time_values,tc2_values, color = 'blue', label = 'Temp vs. Time' )
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.title('TC2 Temp vs. Time')
    plt.legend()
    plt.grid(True)
    plt.show()

    #Converting integer list to an array to divide each value in list by the max value
    array_tc1_values = np.array(tc1_values)
    normal_tc1_values = array_tc1_values / max_value    # Setting this new array to a new variable

    # Creating plot for Normal TC1 vs. Temp
    plt.plot(time_values,normal_tc1_values, color = 'green', label = 'Temp vs. Time' )
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.title('Normal TC1 Temp vs. Time')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Converting integer list to an array to divide each value in list by the max value
    array_tc2_values = np.array(tc2_values)
    normal_tc2_values = array_tc2_values / max_value    # Setting this new array to a new variable

    # Creating plot for Normal TC2 vs. Temp
    plt.plot(time_values, normal_tc2_values, color='orange', label='Temp vs. Time')
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.title('Normal TC2 Temp vs. Time')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Creating Scatterplot of Normal TC1 vs. Normal TC2
    plt.scatter(normal_tc1_values, normal_tc2_values, color='c', label=' ')
    plt.xlabel('Normal TC1')
    plt.ylabel('Normal TC2')
    plt.title('TC1 & TC2 Temp Correlation')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Creating a new array and subtracting the array for TC2 from TC1
    array_difference = np.subtract(array_tc1_values, array_tc2_values)

    # Creating plot of TC1 & TC2 Difference vs. Time
    plt.plot(time_values,array_difference, color = 'maroon', label = 'Temp vs. Time' )
    plt.xlabel('Time')
    plt.ylabel('TC1 & TC2 Difference')
    plt.title('TC1 & TC2 Difference vs. Time')
    plt.legend()
    plt.grid(True)
    plt.show()

    #Correlation Between Bell Jar Press (Torr) and Exhaust Press (Torr), Index for Bell Jar is 48 and Index for Exhaust Press is 49
    bell_jar_press_index = 48   #Setting column index for bell jar press
    exhaust_press_index = 49    #Setting column index for exhaust press

    bell_jar_press_values = [float(row[bell_jar_press_index]) for row in data]  #Creating a float list for all values in bell jar press column.
    exhaust_press_values = [float(row[exhaust_press_index]) for row in data]    #Creating a float list for all values in exhaust press column.

    array_bell_jar_press_values = np.array(bell_jar_press_values)   # changing bell jar press float list to an array
    array_exhaust_press_values = np.array(exhaust_press_values)     # changing exhaust press float list to an array

    max_bell_jar_press_values = max(bell_jar_press_values)  # Setting max to all bell jar values
    max_exhaust_press_values = max(exhaust_press_values)    # Setting max of all exhaust press values

    normal_bell_jar_press_values = array_bell_jar_press_values / max_bell_jar_press_values  # Finding array of normal values of bell jar press by dividing float list array by the max value in the bell jar press column
    normal_exhaust_press_values =  array_exhaust_press_values/ max_exhaust_press_values     # Finding array of normal values of exhaust press by dividing float list array by the max value in the exhaust press column

    # Creating plot of Bell Jar Press & Exhaust Press Correlation
    plt.plot(normal_bell_jar_press_values,normal_exhaust_press_values, color = 'indigo', label = ' ' )
    plt.xlabel('Bell Jar Press')
    plt.ylabel('Exhaust Press')
    plt.title('Bell Jar Press & Exhaust Press Correlation')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Not sure what the relationship between the bell jar press and exhaust press is.  Shape is erratic.

    print ("done")

    # Correlation Between Inlet Valve Open and Inlet Valve Closed, Index for Inlet Valve Open is 26 and Index for Inlet Valve Closed is 27
    inlet_valve_open_index = 26  # Setting column index for inlet valve open
    inlet_valve_closed_index = 27  # Setting column index for inlet valve closed

    inlet_valve_open_values = [int(row[inlet_valve_open_index]) for row in data]  # Creating a float list for all values in inlet valve open column.
    inlet_valve_closed_values = [int(row[inlet_valve_closed_index]) for row in data]  # Creating a float list for all values in inlet valve closed column.

    # it's all 0's and 1's so no need to divide by max value

    # Creating plot of inlet valve open and inlet valve close Correlation
    plt.plot(inlet_valve_open_values, inlet_valve_closed_values, color='pink', label=' ')
    plt.xlabel('Inlet Valve Open')
    plt.ylabel('Inlet Valve Closed')
    plt.title('Inlet Valve Open/Closed Correlation')
    plt.legend()
    plt.grid(True)
    plt.show()

    # It's a function w/ a slope of -1.  There's definitely a correlation between these two columns. If one is "1" then the other is "0" and vice versa!!!

    print("All Done")


    #Scratch Work


#import pandas
#import math
#with open('final.csv') as file:
#    csv_reader = csv.reader(file, delimeter = ",")
#    line_count = 0
#    id_max =0
#    value_max = -math.inf
#    for row in csv_reader:
#        if line_count == 0:
#Max_time = max(Time)
#print (Max_time)
#Using "Time" as an argument since the column I want has a () in it. We can't use the "read" csv function because we want to take the date from a column and append to a new list.  #DictReader will convert each row to a dictionary.  Column header will be used as key instead of index#.
# Trying pandas...
#var2 = read_csv("final.csv")
#Vibrator = var2["Vibrator"].tolist()
#print(Vibrator)
#file = csv.DictReader('final.csv')
#time = []
#for column in file:
#    time.append(column[0])
#print(time)
#def column_header
#bruh = pd.read_csv('final.csv', skiprows=1)
# reading csv with pandas and skipping to row3
#def column_values (column_name):
    # the def function is used to describe a function
#    if column_name in bruh.columns:
#        return file[column_name].dropna().tolist()
#    else:
#        raise ValueError(f"Column '{column_name}' not found in the data.")
# the def function is used to describe a function
#values = column_values("Time(min)")
#print(values[:7000])
#import operator
#var1 = open('final.csv','r')
# Setting var1 to open the csv file with the intention to read
#csv1 = csv.reader(var1, delimiter = ",")
#sort = sorted(csv1, key=operator.itemgetter(0))
#for eachline in sort:
#    print (eachline)
#import pandas as pd
#var1 = pd.read_csv('final.csv')
# Read the CSV file with pandas and setting to the variable var1
#var2 = pd.DataFrame
