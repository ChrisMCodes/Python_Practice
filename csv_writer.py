#!/usr/bin/env python3

'''
This is just a practice script so that I can remember how to create and read CSV files.

Feel free to use it to make your own CSV files!
'''

import os
import csv

# Create a file with data in it
def create_file(filename):
  cont_adding = 'yes'
  with open(filename, "w") as file:
    headers = input("Please enter the column headers for your data, separated by commas (example: 'Name, DOB, Department'): ") 
    file.write(headers + "\n")
    
    while cont_adding == 'yes':
      # prompt user for data
      new_data = input("Please input your data, separated by commas: ")
      answer = input("Would you like to keep adding data? yes/no ")
      if answer.lower() == "yes" or answer.lower() == "y":
        file.write(new_data + "\n")
        cont_adding = "yes"
      else:
        file.write(new_data)
        cont_adding = "no"


# Read the file contents and format the information about each row

def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open(filename) as file:
    # Read the rows of the file into a dictionary
    reader = csv.reader(file)
    # Process each item of the dictionary
    for row in reader:
      for item in row:
        return_string += item
      return_string += "\n"
  return return_string

# test call. Comment this out once you're ready to use this code!
print(contents_of_file("sample_data.csv"))
